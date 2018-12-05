# -*- coding: utf-8 -*-
import time
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from pages.models import *
from .tools import *


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def homepage(request):
    user = request.session['username']
    return render(request, 'homepage.html', homeview(user))


def video_display(request):
    return render(request, 'play.html')


def img_display(request):
    return render(request, 'img.html')


def profile(request):
    return render(request, 'profile.html',perform_profile(request))

def my_sharing(request):
    return render(request, 'my_sharing.html',perform_profile(request))


def load_upload(request):
    tags = arrange(request.session['username'], 't')
    return render(request, 'file_upload.html', {'tags': tags})


def withdraw(request):
    request.session['username']=''
    return render(request, 'index.html', {'error': '您已退出登录'})


def settings(request):
    return render(request, 'setting.html')


def category_view(request):
    return render(request, 'bycategory.html',by_category(request))


def search(request):
    return render(request, 'search.html',perform_search(request))


#######################################################################


def perform_login(request):
    usrn = request.POST.get('username')
    pwd = request.POST.get('password')
    try:
        client = Id.objects.get(name=usrn)
    except:
        return render(request, 'index.html', {'error': '用户' + usrn + '不存在'})
    if client.pwd == pwd:
        request.session['username'] = usrn
        request.session.set_expiry(0)  # 关闭浏览器失效
        return homepage(request)
    else:
        return render(request, 'index.html', {'error': '用户名和密码不匹配' })


def perform_register(request):
    usrn = request.POST.get('username')
    pwd = request.POST.get('password')
    try:
        client = Id.objects.get(name=usrn)
        if client:
            return render(request, 'signup.html', {'error': '岛奴名已被占用'})
    except:
        new_client = Id(name=usrn, pwd=pwd)
        new_client.save()
        request.session['username'] = usrn
        request.session.set_expiry(0)  # 关闭浏览器失效
        return homepage(request)


def perform_upload(request):
    try:
        file = request.FILES.get('file')
        type = request.POST.get('type')
        title = request.POST.get('title')
        description = request.POST.get('description')
        if request.POST.get('ctag'):
            tag = request.POST.get('ctag')
        else:
            tag = request.POST.get('tag')
        owner = Id.objects.get(name= request.session['username'])

        item = Item(file=file,
                    type=type,
                    title=title,
                    description=description,
                    tag=tag,
                    owner=owner)
        item.save()

        """
        Another way of saving file:
        item=request.FILES.get('newfile')
        #提交含有文件的表单，其中的文件内容都在request.FILES, 按form中各项的name属性get
        file=open(os.path.join('media','upload',COMPLETED),'wb')
        #下面写入文件
        for chunk in item.chunks():
            file.write(chunk)
        file.close()
        """
        return homepage(request)
    except:
        return HttpResponse('Failed performing sharing, please try again.')


def perform_profile(request):
    try:
        username=request.GET['user']
        content=arrange(username,'p')
        return {'name':username,'content':content}
    except:
        username=request.session['username']
        content = arrange(username, 'p')
        return {'name': '你', 'content': content}


def perform_password(request):
    username=request.session['username']
    original=Id.objects.get(name=username).pwd

    if request.POST.get('ori-pass') != original:
        return render(request, 'setting.html',{'error':'密码不正确'})
    else:
        Id.objects.filter(name=username).update(pwd=request.POST.get('new-pass'))
        return render(request, 'setting.html', {'error': '修改成功'})


def perform_clean_content(request):
    username = request.session['username']
    try:
        Item.objects.filter(owner=Id.objects.get(name=username)).delete()
        return render(request, 'setting.html', {'error': '您上传的内容已清空'})
    except:
        return homepage(request)


def perform_clean_account(request):
    perform_clean_content(request)
    Id.objects.get(name=request.session['username']).delete()
    return withdraw(request)


def by_category(request):
    tag=request.GET.get('tag')
    data=arrange(tag,'c')
    return {'tag':tag, 'content':data}


def perform_search(request):
    keyword=request.GET.get('keyword')
    data=arrange(keyword,'s')
    return {'result':keyword+'的搜索结果如下', 'content':data}


def perform_delete(request):
    target=request.GET.get('number')
    Item.objects.filter(number=int(target)).delete()
    return HttpResponseRedirect('/my_sharing')

def perform_like(request):
    pass


def perform_play(request):
    pass
