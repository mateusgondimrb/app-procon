from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=180, label="", required=True, widget=forms.TextInput(attrs={'class': 'searchfield'}))

