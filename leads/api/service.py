from multiprocessing.forkserver import connect_to_new_process

from django.core.exceptions import ValidationError
from .models import Person

class PersonService:

    @staticmethod
    def createPerson(name, email, content):
        if not name or name.strip() == '':
            raise ValidationError('Nome não pode ser vazio')
        if not email or email.strip() == '':
            raise ValidationError('Email não pode ser vazio')
        if not content or content.strip() == '':
            raise ValidationError('Mensagem não pode ser vazia')

        return Person.objects.create(name=name, email=email, content=content)

    @staticmethod
    def getAll():
        return Person.objects.all()

    @staticmethod
    def getById(pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise ValidationError(f'Usuario com ID {pk} não existe')

    @staticmethod
    def updatePerson(pk, name, email, content):
        person = PersonService.getById(pk)

        if not name or name.strip() == '':
            raise ValidationError('Nome não pode ser vazio')
        if not email or email.strip() == '':
            raise ValidationError('Email não pode ser vazio')
        if not content or content.strip() == '':
            raise ValidationError('Mensagem não pode ser vazia')

        person.name = name
        person.email = email
        person.content = content
        person.save()
        return person

    @staticmethod
    def deletePerson(pk):
        person = PersonService.getById(pk)
        person.delete()