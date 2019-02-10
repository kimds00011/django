from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status','created_at', 'updated_at']

    actions = ['make_published','make_Draft', 'make_Withdrawn']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

# admin.site.register(Post, PostAdmin)

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update 활용
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count)) #django message framework 활용
    # make_published.short_description = '지정 포스팅을 Published상태로 변경 합니다.'#make_published를 바꿈
    def make_Draft(self, request, queryset):
        updated_count = queryset.update(status='d') #QuerySet.update 활용
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count)) #django message framework 활용
    def make_Withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w') #QuerySet.update 활용
        self.message_user(request, '{}건의 포스팅을 Withdrawn상태로 변경'.format(updated_count)) #django message framework 활용    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']