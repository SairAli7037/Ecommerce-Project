from django.urls import path
from authcart.views import *
urlpatterns = [
      path('signup/',signup),
      path('login/',handlelogin),
      path('logout/',handlelogout),
      path('activate/<uidb64>/<token>/',ActivateAccountView.as_view(),name='activate'),
      path('request-reset-email/',RequestResetEmailView.as_view(),name='request-reset-email'),
      path('set-new-password/<uidb64>/<token>',SetNewPasswordView.as_view(),name='set-new-password'),
]