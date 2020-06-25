from django import forms
from .models import Session

class MyDateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local" # <input type="datetime-local" ... />

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M" # Output format (will be rendered as value="..." in HTML)
        super().__init__(**kwargs)

class SessionCreateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['location', 'time', 'length', 'link']

    time = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"], # How to parse the POST form data
        widget=MyDateTimeInput()
    )
