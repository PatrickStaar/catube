# -*- coding:utf-8 -*-

from pages.models import *
import random

BASE_DIR = 'D:/Code/web/catube/src/'
MEDIA_PATH = 'D:/Code/web/catube/media/'
SAVING_PATH = MEDIA_PATH + 'result/'

def arrange(username,type):
    if type=='h':
        item_by_tag = {}
        try:
            latest = Item.objects.all()
            for i in latest:
                item_by_tag[i.tag] = i
        except:
            item_by_tag.clear()

        for t in item_by_tag.keys():
            length=len(item_by_tag[t])
            if length >6:
                item_by_tag[t]=item_by_tag[length-6,:]
        return item_by_tag, item_by_tag.keys()

    elif type=='t':
        try:
            tags=Item.objects.values_list('tag').distinct()
            return random.sample(tags, 5) # 随机挑选5个标签
        except:
            return []
    else:
        return None


def statics(item):
    likes=len(Behavior.objects.filter(type ='l',aim = item))
    clicks=len(Behavior.objects.filter(type='c',aim = item))
    return {'like':likes, 'click':clicks}

def homeview(username):
    data, tags = arrange(username,'h')
    quick_peek={'user':username,'content':{},'tag':tags}
    for t in tags:
        for i in data[t]:
            quick_peek['content'][t].append({'data':i,'static':statics(i)})
    return quick_peek
