from django import forms
import datetime


class HitStatQueryForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
