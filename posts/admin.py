from csv import list_dialects
from django.contrib import admin

from .models import Post,Comment
# 왜 posts.models를 하지 않는가? - 이미 같은 posts폴더에 있기 때문이다.
# from support.models import FAQ
# Register your models here.
class CommentInline(admin.TabularInline) :
    # StackedInline 과 TabularInline의 차이 : 세로 - 가로
    model = Comment
    extra = 0
    min_num = 1
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글' #복수형 이름 바꿀때 사용

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin) :
    list_display = ('id','iamge','content','created_at','view_count','writer')
    # list_editable = ('content',)
    list_filter = ('created_at',)
    search_fields = ('id','writer__username' )
    search_help_text = '게사판 번호, 작성자 검색이 가능합니다!'
    readonly_fields = ('created_at',)
    inlines = [CommentInline]

    actions =['make_published']
    def make_published(modeladmin, request, queryset) :
        for item in queryset :
            item.content = '운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()
# admin.site.register(Comment)


    
