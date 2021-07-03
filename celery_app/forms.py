import datetime

from django import forms
from django.utils import timezone


class TaskForm(forms.Form):
    email = forms.EmailField(initial='test@gmail.com')
    text = forms.CharField(initial="It's a test", max_length=400)
    date = forms.DateTimeField(initial=timezone.now(), help_text='Enter date and time (not > 2 days)')

    def clean_date(self):
        dt = self.cleaned_data['date']
        dt_now = timezone.now()
        if dt <= dt_now or dt > (dt_now + datetime.timedelta(days=2)):
            raise forms.ValidationError("The date must be in the future, but no more than two days!")
        return dt
