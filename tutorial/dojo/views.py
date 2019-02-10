import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post


# Create your views here.

# 3개 뷰 한번에 하기 
# def mysum(request, x, y=0, z=0):
#     #request: HttpRequest
#     return HttpResponse(int(x)+int(y)+int(z))

# #다수 추가할때 
# def mysum(request, numbers):
#     #numbers = "1234/1234/1234/123/412/341234"
#     result = sum(map(int, numbers.split("/")))
#     return HttpResponse(result)

#step4#



post_detail = DetailView.as_view(model=Post)
#step3#
# class DetailView(object):
#     def __init__(self,model):
#         self.model = model

#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(self.model, id=kwargs['id'])

#     def get_template_name(self):
#         return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)

#     def dispatch(self, request, *args, **kwargs):
#         return render(request, self.get_template_name(),{
#             self.model._meta.model_name: self.get_object(*args, **kwargs),
#         })
#     @classmethod
#     def as_view(cls, model):
#         def view(request, *args, **kwargs):
#             self = cls(model)
#             return self.dispatch(request, *args, **kwargs)            
#         return view

# post_detail = DetailView.as_view(Post)


#step2#
# def generate_view_fn(model):
#     def view_fn(request, id):
#         instance = get_object_or_404(model, id=id)
#         instance_name = model._meta.model_name
#         template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
#         return render(request, template_name, {
#             instance_name: instance,
#         })
#     return view_fn

# post_detail = generate_view_fn(Post)

# def post_detail(request, id):
#     return render(request, 'dojo/post_detail.html', {
#         'Post' : Post,
#     })

#함수에서 항상 http reqeust 인자를 받음 (21 장고폼에 기존 방법 있음)
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
    
            # 방법1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법2)
            '''
            post = Post(title=form.cleaned_data['title'],
                        content = form.cleaned_data['content'])
            post.save()
            '''

            # 방법3
            # )
            '''
            post = Post.objects.create(title=form.cleaned_data['title'],
                                       content = form.cleaned_data['content'])
            '''

            # 방법4)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')  # namespace:name 추천 하지만 지금은 url로 
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })
        
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')  # namespace:name
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })

#다수지만 빈공백이 생겼을때 
def mysum(request, numbers):
    #numbers = "1234/1234/1234/123//412/341234"
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    #lambada s: int(s or 0)  숫자가 거짓(공백)이면 0으로 치환
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요.{}. {}살이시네요'.format(name,age))


def post_list1(request):
    'FBV: 직접 문자열로 HTML형식 응답하기'

    name = '공유'
    return HttpResponse('''
    <h1>daniel</h1>
    <p>{name}</p>
    <p>하단 Test</p>'''.format(name=name))



def post_list2(request):
    'FBV: 템플릿을 통해 HTML형식 응답하기'

    name = '공유'
    response = render(request, 'dojo/post_list.html', {'name':name})
    return response


def post_list3(request):
    'FBV: JSON 형식 응답하기'

    return JsonResponse({
        'message': '안녕, 파이썬&장고',
        'items' : ['파이썬','장고','Celery','Azure','AWS']
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    'FBV: 엑셀 다운로드 응답하기'

    #filepath = '/Users/kimdaesung/Documents/Study/Django/Django_tutorial/tutorial/Education.xls'
    filepath = os.path.join(settings.BASE_DIR, 'Education.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')#'text/html'
        #필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
