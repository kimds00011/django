from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    print(repr(request.user.is_authenticated))

    qs = Post.objects.all()

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)
    # messages.error(request, '에러메시지 테스트')

    response = render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q':q,
    })
    #httpResponse 인스턴스 인데, render를 통해서, 좀더 쉽게 템플릿을 통한 렌더링이 가능
    response
    return response

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)

    
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

def post_new(request):
    if request.method == 'POST': #method 가 POST인지 아닌지 구분 먼저 하고 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post) #post.net_absolute_url() => post_detail
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
    
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST': #method 가 POST인지 아닌지 구분 먼저 하고 
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post) #post.net_absolute_url() => post_detail
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
    