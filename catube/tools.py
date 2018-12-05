# -*- coding:utf-8 -*-

from pages.models import *
from django.db.models import Q
import random

BASE_DIR = 'D:/Code/web/catube/src/'
MEDIA_PATH = 'D:/Code/web/catube/media/'
SAVING_PATH = MEDIA_PATH + 'result/'
NUM_PER_LINE = 5

def arrange(attribute,type):
    if type=='h':
        item_by_tag = {}
        try:
            latest = Item.objects.all()
            for i in latest:
                if i.tag in item_by_tag:
                    item_by_tag[i.tag].append(i)
                else:
                    item_by_tag[i.tag]=[]
                    item_by_tag[i.tag].append(i)
        except:
            item_by_tag.clear()
        alltags=[]
        for t in item_by_tag.keys():
            alltags.append(t)
            length=len(item_by_tag[t])
            if length > NUM_PER_LINE:
                item_by_tag[t]=item_by_tag[length-NUM_PER_LINE,:]
        return item_by_tag, alltags

    elif type=='t':
        try:
            tags=Item.objects.values('tag').distinct()
            if len(tags) >=NUM_PER_LINE:
                return random.sample(tags, NUM_PER_LINE) # 随机挑选5个标签
            else:
                return tags
        except:
            return []

    elif type=='p':
        out = []
        try:
            myown = Item.objects.filter(owner=Id.objects.get(name=attribute))
            for i in myown:
                out.append({
                    'title':i.title,
                    'data': i.file,
                    'type':i.type,
                    'description':i.description,
                    'number':i.number
                })
            lines=len(out)//NUM_PER_LINE
            leftout=len(out)%NUM_PER_LINE
            tmp=[]
            for j in range(0,lines):
                tmp.append(out[j:j+NUM_PER_LINE])
            if leftout:
                tmp.append(out[NUM_PER_LINE*lines:])
            out=tmp
            return out
        except:
            out.clear()
            return out
    elif type=='c':
        out = []
        try:
            item_of_tag = Item.objects.filter(tag=attribute)
            for i in item_of_tag:
                out.append({
                    'title': i.title,
                    'data': i.file,
                    'type': i.type,
                    'description': i.description,
                    'owner': i.owner.name
                })
            lines = len(out) // NUM_PER_LINE
            leftout = len(out) % NUM_PER_LINE
            tmp = []
            for j in range(0, lines):
                tmp.append(out[j:j + NUM_PER_LINE])
            if leftout:
                tmp.append(out[NUM_PER_LINE * lines:])
            out = tmp
            return out
        except:
            out.clear()
            return out

    elif type=='s':
        out = []
        try:
            similar = Item.objects.filter(
                Q(title__icontains=attribute)|Q(description__icontains=attribute)
            )
            for i in similar:
                out.append({
                    'title': i.title,
                    'data': i.file,
                    'type': i.type,
                    'description': i.description,
                    'owner': i.owner.name
                })
            lines = len(out) // NUM_PER_LINE
            leftout = len(out) % NUM_PER_LINE
            tmp = []
            for j in range(0, lines):
                tmp.append(out[j:j + NUM_PER_LINE])
            if leftout:
                tmp.append(out[NUM_PER_LINE * lines - 1:])
            out = tmp
            return out
        except:
            out.clear()
            return out

    else:
        return None


def statics(item):
    likes=len(Behavior.objects.filter(type ='l',aim = item))
    clicks=len(Behavior.objects.filter(type='c',aim = item))
    return {'like':likes, 'click':clicks}

def homeview(username):
    data, tags = arrange(username,'h')
    quick_peek={'user':username,'content':{}}
    for t in tags:
        quick_peek['content'][t]=[]
        for i in data[t]:
            quick_peek['content'][t].append({
                                            'data':i.file,
                                            'title':i.title,
                                            'type':i.type,
                                            'description':i.description,
                                            'owner':i.owner.name
                                            })
    return quick_peek