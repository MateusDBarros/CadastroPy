from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.PersonCreate.as_view(), name='person-view-create'),
    path('person/<int:pk>/', views.PersonRetrieveUpdateDestroy.as_view(), name='update')
]