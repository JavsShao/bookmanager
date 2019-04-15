from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from book.models import *


def index(request):

    # 准备上下文：定义在字典中(测试数据)
    context = {'title':'测试模板处理数据'}

    return render(request, 'Book/index.html', context)

def booklist(request):
    '''
    显示书籍列表信息
    :param request:
    :return:
    '''
    books = BookInfo.objects.all()
    context = {'books':books}
    return render(request, 'Book/booklist.html', context)

def peoplelist(request):
    '''显示人物信息'''
    peoples = PeopleInfo.objects.all()
    books = BookInfo.objects.all()
    people_context = {'peoples':peoples}
    book_context = {'books':books}
    return render(request, 'People/peoplelist.html', people_context, book_context)
