from django import forms

class ArticleForm(forms.Form):
	user = forms.CharField(max_length=10)
	content = forms.CharField()