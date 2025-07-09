from django import forms
from .models import Aduan

class AduanForm(forms.ModelForm):
    class Meta:
        model = Aduan
        fields = ['nama', 'kategori', 'isi', 'gambar']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Anda'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tulis aduan...'}),
            'gambar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }