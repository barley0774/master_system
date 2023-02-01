from django import forms
from .models import Category

class TermForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category
    term = forms.CharField(max_length=100)
    category = forms.ChoiceField(label='カテゴリ', widget=forms.Select, choices=list(category_choice.items()))
    text = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label="画像", required=False)