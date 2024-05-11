from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    content = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'class': 'w-full py-4 px-6 rounded-md border'
    }))

    class Meta:
        model = ConversationMessage
        fields = ('content',)
