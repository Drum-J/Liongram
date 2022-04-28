from django.contrib import admin
from .models import FAQ,Inquiry,Answer
# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    # extra = 0
    min_num = 1
    max_num = 1
    verbose_name = '답변'
    # verbose_name_plural = '답변' #답변을 1개만 달려고 복수형은 없앴고, 최소,최대 갯수를 1개로 고정시켰다.

@admin.register(FAQ)
class FAQModelAdmin(admin.ModelAdmin) :
    # list_display = ('qus','category','ans','writer','created_at','writer2','modify_date') #2차미션에 만들어 놓은 것
    list_display = ('title','category','modify_date') # 제목, 카테고리, 최종수정일만 띄운 것
    search_fields = ('title',) #검색 필드. 튜플로 들어가야해서 ,를 남겨야 함
    search_help_text = '제목 검색이 가능합니다!' #검색 필드 텍스트
    list_filter = ('category',) #필터필드 만드는 거 이것도 마찬가지로 ,있어야함
    

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin) :
    list_display = ('title','category','created_at','writer') 
    search_fields = ('title','email','phone') 
    search_help_text = '제목,이메일,전화번호 검색이 가능합니다!' 
    list_filter = ('category',)

    inlines = [AnswerInline]