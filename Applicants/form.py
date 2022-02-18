from django import forms
from.models import applicant
class applyingForm(forms.ModelForm):
    class meta:
        model=applicant
        fields = "__all__"