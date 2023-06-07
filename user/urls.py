from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import utils


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile_page, name='profile'),

    # PASSWORD RESET
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='user/password_reset.html',
        email_template_name='user/password_reset_email.html',
        subject_template_name='user/password_reset_subject.txt'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'
    ), name='password_reset_complete'),


    # Communications Limited
    path('subscription/', utils.subscriptions, name='subscription'),
    path('package/<int:pk>/', utils.package_detail, name='package-detail'),
    path('apply/<int:pk>/', utils.package_application, name='package-application'),
    path('remove/<int:pk>/', utils.subscription_removal, name='remove-package'),
]
