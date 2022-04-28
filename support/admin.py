from django.contrib import admin
from .models import FAQ
# Register your models here.

@admin.register(FAQ)
class FAQModelAdmin(admin.ModelAdmin) :
    # list_display = ('qus','category','ans','writer','created_at','writer2','modify_date') #2차미션에 만들어 놓은 것
    list_display = ('title','category','modify_date') # 제목, 카테고리, 최종수정일만 띄운 것
    search_fields = ('title',) #검색 필드. 튜플로 들어가야해서 ,를 남겨야 함
    search_help_text = '제목 검색이 가능합니다!' #검색 필드 텍스트
    list_filter = ('category',) #필터필드 만드는 거 이것도 마찬가지로 ,있어야함
    

    # inlines = [CommentInline]