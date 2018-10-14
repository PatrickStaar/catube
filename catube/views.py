# -*- coding: utf-8 -*-
import time
from django.shortcuts import render
from django.http import HttpResponse
from pages.models import *
from .tools import *


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request,'signup.html')


def homepage(request):
    user=request.session['username']
    return render(request, 'homepage.html',homeview(user))


def video_display(request):
    return render(request,'play.html')


def img_display(request):
    return render(request,'img.html')


def profile(request):
    return render(request,'profile.html')


def load_upload(request):
    tags=arrange(request.session['username'],'t')
    return render(request, 'file_upload.html',{'tags':tags})

#######################################################################


def perform_login(request):
    usrn=request.POST.get('username')
    pwd=request.POST.get('password')
    try:
        client=Id.objects.get(name=usrn)
    except:
        return render(request, 'index.html', {'error': '用户' + usrn + '不存在'})
    if client.pwd == pwd:
        request.session['username']=usrn
        request.session.set_expiry(0)  # 关闭浏览器失效
        return homepage(request)
    else:
        return render(request,'index.html',{'error':'用户名和密码不匹配'+client.pwd+pwd })


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
    FILENAME = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    FORMAT = '.mp4'
    COMPLETED = FILENAME + FORMAT
    # DEFAULT_PATH='/upload/'

    if request.method == 'POST':
        item = request.FILES.get('newfile')
        date = request.POST.get('date')
        name = item.name
        dbitem = Item(data=date, name=name, video=item)
        dbitem.save()
        vd = Item.objects.all()
        content = {'vd': vd, }
        """
        item=request.FILES.get('newfile')
        #提交含有文件的表单，其中的文件内容都在request.FILES, 按form中各项的name属性get
        file=open(os.path.join('media','upload',COMPLETED),'wb')
        #下面写入文件
        for chunk in item.chunks():
            file.write(chunk)
        file.close()
        """
        return render(request, 'showing.html', content)
    else:
        return HttpResponse('Bad Entry')


def perform_like(request):
    pass


def perform_play(request):
    pass


def perform_zoom(request):
    pass


def perform_logout(request):
    pass


def perform_check(request):
    pass


def video(request,type='all'):
    vd = Item.objects.filter(type__exact="vid")
    content = {'vd': vd, }
    return render(request, 'showing.html', content)


def delete(request):
    id = request.GET.get('id')
    item = Item.objects.get(id=id)
    item.delete()
    vd = Item.objects.all()
    content = {'vd': vd, }
    return render(request, 'showing.html', content)


def clean(request):
    Item.objects.all().delete()
    vd = Item.objects.all()
    content = {'vd': vd, }
    return render(request, 'showing.html', content)


# def process(request):
#     video = request.GET.get('video')
#     num, out_name = detect(video)
#
#     numfile=savearr(num,out_name+'.txt')
#
#     save1 = Num(name=video, num=numfile)
#     save1.save()
#     item = Video.objects.get(video=video)
#     item.status = '处理完成'
#     item.save()
#
#     vd = Video.objects.all()
#     content = {'vd': vd, }
#     return render(request, 'showing.html', content, )


# def result(request):
#     video = request.GET.get('video')
#     item = Video.objects.get(video=video)
#     date = item.data
#     item2 = Num.objects.get(name=video)
#     num = item2.num
#     list2 = readfromfile(num) #num.strip('[]').split(',')
#     date = getTime4Clip(beginning_formated=date, frameInterval=1.0,
#                         number_arr=resultCompress(list2, type='MAX'))
#     points = date.keys()
#     values = date.values()
#     vd = Video.objects.all()
#     content = {'vd': vd, 'video': video, 'date': points, 'val': values}
#     return render(request, 'result.html', content)

def check_upload(request):
    FILENAME = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    FORMAT = '.mp4'
    COMPLETED = FILENAME + FORMAT
    # DEFAULT_PATH='/upload/'

    if request.method == 'POST':
        item = request.FILES.get('newfile')
        date = request.POST.get('date')
        name = item.name
        dbitem = Item(data=date, name=name, video=item)
        dbitem.save()
        vd = Item.objects.all()
        content = {'vd': vd, }
        """
        item=request.FILES.get('newfile')
        #提交含有文件的表单，其中的文件内容都在request.FILES, 按form中各项的name属性get
        file=open(os.path.join('media','upload',COMPLETED),'wb')
        #下面写入文件
        for chunk in item.chunks():
            file.write(chunk)
        file.close()
        """
        return render(request, 'showing.html', content)
    else:
        return HttpResponse('Bad Entry')