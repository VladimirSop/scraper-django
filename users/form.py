from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        Model = User
        fields = ('username', 'password')