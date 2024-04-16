from django import forms
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Response, Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'content': forms.Textarea(attrs={'class': 'form-control ckeditor'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        
    # def clean_my_field(self):
    #     data = self.cleaned_data['my_field']
    #     if len(data) < 5:
    #         raise forms.ValidationError("Минимальная длина поля должна быть не менее 5 символов.")
    #     return data
        


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add response...'}),
        }
        lables = {
            'text': '',
        }