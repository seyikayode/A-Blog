from django.urls import path
from django.contrib.auth import views
from .views import register, profile
urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', register, name='signup'),
    path('profile/', profile, name='profile'),
    path('password_reset/', views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done')
]

