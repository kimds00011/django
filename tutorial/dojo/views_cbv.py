import os
from django.conf import settings
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse


class PostlistView1(View):
    'CBV : 직접 문자열로 HTML형식 응답하기'

    # def get(self, request):
    #     name = '공유'
    #     html = '''
    #     <h1>daniel</h1>
    #     <p>{name}</p>
    #     <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''.format(name=name)
    #     return HttpResponse(html)

    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)
    def get_template_string(self):
        return '''
        <h1>daniel</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''

post_list1 = PostlistView1.as_view()



class PostlistView2(TemplateView):
    template_name = 'dojo/post_list2.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context
#super은 python3 에서만 지원 

post_list2 = PostlistView2.as_view()
    

class PostlistView3(View):
    'CBV: JSON형힉 응답하기'

    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
            'message':'안녕, 파이썬&장고',
            'item' : ['파이썬','장고', 'Celery', 'Azure', 'AWS'],
        }
post_list3 = PostlistView3.as_view()

# class ExceldownloadView(View):
#     'CBV: 엑셀 다운로드 응답하기'
    
#     def get(self, request):
#         excel_path = '/Users/kimdaesung/Documents/Study/Django/Django_tutorial/tutorial/Education.xls'
#         filename = os.path.basename(self.excel_path)
#         with open(excel_path, 'rb')as f:
#             response = HttpResponse(f, content_type='application/vnd.ms-excel')
#             response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
#             return response

# excel_download = ExceldownloadView.as_view()




