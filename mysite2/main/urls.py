from django.urls import path

from .views import (
    DasboardView
)

app_name = 'main'

urlpatterns = [
    path('dash-board/', DasboardView.as_view(), name='Dash_board'),
    # path('log-out/', LogOutView.as_view(), name='log_out'),
    #
    # path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),
    #
    # path('sign-up/', SignUpView.as_view(), name='sign_up'),
    # path('activate/<code>/', ActivateView.as_view(), name='activate'),
    #
    # path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    # path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    # path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),
    #
    # path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),
    #
    # path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    # path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    # path('change/email/', ChangeEmailView.as_view(), name='change_email'),
    # path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
]
