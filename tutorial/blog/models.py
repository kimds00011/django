import re
from django.conf import settings
from django.urls import reverse
from django.forms import ValidationError
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')



class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    #작성자 CharField 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.CharField(max_length = 20, verbose_name='작성자')  위에 settings AUTH_USER_MODEL을 사용하기떄문에 제거
    # author = models.CharField(max_length = 20, default = 'anonymous') 
    # default = 'anonymous'를 넣어줘도 되긴 하지만 author은 사용자가 직접 넣게 할 것이기 때문에 default는 어울리지 않음

    #길이 제한 이 있는 문자열
    title = models.CharField(max_length=100,verbose_name='제목',help_text='제목을 입력해주세요') 
    # choices = (
    #     ('제목1', '제목1 레이블'),#('저장될 값', 'UI에 보여질 레이블')
    #     ('제목2', '제목2 레이블'),
    #     ('제목3', '제목3 레이블'),
    # ))
    content = models.TextField(verbose_name='내용') #길이 제한이 없는 문자열
    #방법1
    # photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
    #이미지 파일 user가 이미지를 안올릴루도 있기 때문에 blak=True, upload 위치 설정 처음에 / 쓰면 안됨
    # photo_thumbnail = ImageSpecField(source='photo', processors=[Thumbnail(300,300)],format='JPEG',options={'qulity':60})
    #방법2
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',processors=[Thumbnail(300, 300)],format='JPEG',options={'quality': 60})
    
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,blank=True,
        validators=[lnglat_validator],help_text='경도,위도 포맷으로 입력')
    tag_set = models.ManyToManyField('Tag', blank=True)#다른 APP과 relation을 걸을때는 app이름.Tag로 해주면 됨 
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add -> 현재 하나의 Post레코드가 최초 저장
    updated_at = models.DateTimeField(auto_now=True) #해당 레코드가 갱신 될떄마다 자동저장
    
    class Meta:
        ordering = ['-id'] # - 내림차순, default 오름차순
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) # 장고 2부터는 Foreignkey 에 대해서 on_delete 지정 해줘야 함 
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)#unique옵션은 같은 테그값이 중복되지 않도록

    def __str__(self):
        return self.name
