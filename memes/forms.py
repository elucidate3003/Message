from django import forms
from .models import Home,Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ('user','message','photo')
        
