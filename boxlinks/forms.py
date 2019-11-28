from django import forms
from .models import Links,User

class LinksForm(forms.ModelForm):
   """
   新規データ登録画面用のフォーム定義
   """
   class Meta:
       model = Links
       fields =['priority', 'link', 'memo','user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['user_name']


