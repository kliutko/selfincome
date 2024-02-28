from django.urls import path
from .views import ProfileUpdateView, ProfileDetailView, UserRegisterView, UserLoginView, UserLogoutView, \
    UserPasswordChangeView, UserForgotPasswordView, UserPasswordResetConfirmView, UserForgotPasswordView, \
    UserPasswordResetConfirmView, UserConfirmEmailView, EmailConfirmationSentView, EmailConfirmedView, \
    EmailConfirmationFailedView, ProfileFollowingCreateView, ArticleBySignedUser

app_name = 'users'

urlpatterns = [
    path('edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/follow/<str:slug>/', ProfileFollowingCreateView.as_view(), name='follow'),
    path('articles/signed/', ArticleBySignedUser.as_view(), name='articles_by_signed_user'),

    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),

    path('<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),

]

