from django.contrib.auth.forms import AuthenticationForm

class CustonAuthenticationForm(AuthenticationForm):
    class Meta:
        model= AuthenticationForm
        fiels = ["username", " password"]


    