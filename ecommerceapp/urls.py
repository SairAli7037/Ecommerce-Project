from django.urls import path
from ecommerceapp.views import *

urlpatterns = [
    path('',index),
    path('contact/',contact),
    path('about/',about),
    path('checkout/',checkout),
    path('handlerequest/',handlerequest),
    path('profile/',profile),
]