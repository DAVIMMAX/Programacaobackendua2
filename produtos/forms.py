from django import forms
from .models import Produto

class produtoForm(forms.ModelForm):

    validade = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model= Produto
        fields = ['nome', 'preco', 'validade']

