from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('save-email',views.saveEmail.as_view(),name='saveEmail')
]