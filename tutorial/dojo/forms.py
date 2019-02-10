from django import forms
from .models import Post

'''
def min_length_3_validator(value):
    if len(value) <3 :
        raise forms.ValidationError('3글자 이상 입력해주세요.')
'''
'''        
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        self.instance = Post.objects.create(**self.cleaned_data)
        if commit:
                self.instance.save()
        return self.instance
'''

class PostForm(forms.ModelForm):
        class Meta:
                model = Post
                #fields = '__all__'
                fields = ['title', 'content', 'user_agent']
                widgets = {
                        'user_agent':forms.HiddenInput,
                }

