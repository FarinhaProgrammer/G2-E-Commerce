from django import forms

class SearchForm(forms.Form):
    result = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Type Something to Search...", 'type': 'search', 'class': 'search'}), label='')