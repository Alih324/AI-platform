from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Write your article...',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Share your thoughts...',
            }),
        }

    def clean_content(self):
        content = self.cleaned_data['content'].strip()
        if len(content) < 2:
            raise forms.ValidationError('Comment is too short.')
        return content
