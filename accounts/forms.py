from django import forms

class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    #render normal text field but of type password
    password = forms.CharField(widget=forms.PasswordInput)
