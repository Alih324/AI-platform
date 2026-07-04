from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your message...',
            }),
        }

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_subject(self):
        return self.cleaned_data['subject'].strip()

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        if len(message) < 10:
            raise forms.ValidationError('Message must be at least 10 characters long.')
        return message
