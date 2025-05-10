from django import forms

class NewsForm(forms.Form):
    news = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type or paste your news text here...',
        'rows': 5,
    }), required=False)
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), required=False)
