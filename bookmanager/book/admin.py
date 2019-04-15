from django.contrib import admin

from book.models import *

# Register your models here.


@admin.register(PeopleInfo)
class PeopleInfoAdmin(admin.ModelAdmin):

    # 列的展示
    list_display = ['id', 'name', 'readcount']

    # 右侧栏过滤器
    list_filter = ['book', 'gender']

    # 搜索框
    search_fields = ['name']

class PeopleInfoTabularInline(admin.TabularInline):
    model = PeopleInfo  # 要关联的类型
    extra = 2   # 附加编辑的数量

class BookInfoAdmin(admin.ModelAdmin):

    # 页数大小
    list_per_page = 2
    # 操作选项的位置
    actions_on_top = True
    actions_on_bottom = True
    # 列表中的列
    list_display = ['id', 'name', 'title', 'readcount', 'commentcount']

    # fields = ['name', 'pub_date']
    fieldsets = (
        ('基本', {'fields':['name', 'pub_date']}),
        ('高级',{
            'fields':['readcount', 'commentcount'],
            'classes':('collapse',) # 是否折叠显示
        })
    )

    inlines = [PeopleInfoTabularInline]




admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(PeopleInfo)


