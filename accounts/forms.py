from django import forms
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm

# password reset karne wala form  iska code base samjha nahi aa raha 

class SetPasswordForm(BaseSetPasswordForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
from django import forms
from .models import Attendance
