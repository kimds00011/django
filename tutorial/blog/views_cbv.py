from django import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse, reverse_lazy


post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)
#blog/forms.py에 구현해야 되지만 지금은 여기에 만듬(기본 모델 폼이기 때문에 지워도 상관 없는 class 들임)
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'

# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     # success_url = '/...'
post_new = CreateView.as_view(model=Post)
# post_new = CreateView.as_view(model=Post, success_url='/blog/')
#success가 있으면 get_absolute_url 이 없어도 이동하게 됨
post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
