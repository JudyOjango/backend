from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

### 🔹 REGISTER USER ###
@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    """Handles user registration."""
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)


### 🔹 LOGIN USER ###
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    """Authenticates user and returns JWT tokens."""
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {"id": user.id, "username": user.username},
            }
        )
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


### 🔹 LOGOUT USER (Blacklist Refresh Token) ###
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Logs out user and blacklists refresh token."""
    try:
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)
        token.blacklist()  # ✅ Add to blacklist
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


### 🔹 FORGOT PASSWORD ###
@api_view(["POST"])
@permission_classes([AllowAny])
def forgot_password_view(request):
    """Handles password reset requests."""
    email = request.data.get("email")

    try:
        user = User.objects.get(email=email)
        new_password = user.make_random_password()
        user.set_password(new_password)
        user.save()

        send_mail(
            "Password Reset",
            f"Your new password is: {new_password}",
            "noreply@threatmonitor.com",
            [email],
            fail_silently=False,
        )

        return Response({"message": "A new password has been sent to your email"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "No account found with this email"}, status=status.HTTP_404_NOT_FOUND)
