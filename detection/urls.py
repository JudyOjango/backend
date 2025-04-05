from django.urls import path
from auth_app.views import login_view, register_view, logout_view, forgot_password_view
from detection.views import threat_list, threat_detail

urlpatterns = [
    path("api/auth/login/", login_view, name="login"),
    path("api/auth/register/", register_view, name="register"),
    path("api/auth/logout/", logout_view, name="logout"),
    path("api/auth/forgot-password/", forgot_password_view, name="forgot_password"),
    path("api/threats/", threat_list, name="threat_list"),
    path("api/threats/<int:pk>/", threat_detail, name="threat_detail"),
]
