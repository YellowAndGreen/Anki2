import os

from .models import Card, WordList
import datetime
import json
from django.contrib.auth.models import User
import logging


# 更新到期卡片的due
def update_due():
    logger = logging.getLogger(__name__)
    now = datetime.datetime.now()
    deadline = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=23, minute=59, second=59)
    count = 0
    for card in Card.objects.all():
        # 若时间仍在今天或以前，则更新至明天
        if card.due <= deadline:
            card.due = datetime.datetime(year=now.year, month=now.month, day=now.day + 1)
            card.interval = -1
            card.save()
            count += 1
    logger.error(f"{now}:已更新{count}个到期单词")


# 生成新的每日列表
def update_due_list():
    logger = logging.getLogger(__name__)
    # 首先删除之前的due表
    WordList.objects.filter(name="due").delete()
    now = datetime.datetime.now()
    deadline = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=23, minute=59, second=59)
    cards = filter(lambda card: card.due <= deadline, Card.objects.all())
    id_list = [{'id': card.id} for card in cards]
    wordlist = WordList(owner=User.objects.all()[0], name="due", wordlist=json.dumps(id_list)
                        , len_list=len(id_list))
    wordlist.save()
    logger.error(f"{now}:新列表已生成！共有{len(id_list)}张卡片")


# 自动备份数据库
def backup_db():
    command = 'python manage.py dumpdata > db.json'
    status = os.system(command)
    if status != 0:
        raise Exception('执行系统命令失败, command=%s, status=%s' % (command, status))

