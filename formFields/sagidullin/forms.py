from django import forms

class section(forms.Form):
    Heading = forms.CharField()
    URL = forms.URLField()
    Content = forms.CharField(widget=forms.Textarea)
    Publication = forms.CharField(widget=forms.CheckboxInput)
    Category = forms.ChoiceField(choices=((1, 'Javapon'), (2, 'Djangopon'), (3, 'Pythonpon')))