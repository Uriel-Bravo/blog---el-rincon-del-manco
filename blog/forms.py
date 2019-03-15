from django import forms
from blog.models import Post, Category

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'category', 'title', 'subtitle', 'image', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CategoryForm(forms.ModelForm):

    class Meta():
        model = Category
        fields = ('name',)
