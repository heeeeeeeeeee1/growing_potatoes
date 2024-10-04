from .models import Movie # 여기 잘 모르겠음
from django import forms # 여기 잘 모르겠음

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'