import json
import redis
from readmdict import MDX
import re

from Anki import settings


def find_example(queryword):
    r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
    headwords, items = r.get('headwords'), r.get('items')
    if not headwords or not items:
        # 加载mdx文件
        filename = "flashcards/static/dict/牛津/牛津高阶8简体.mdx"
        # filename = "flashcards/static/dict/剑桥高阶.mdx"
        headwords = [*MDX(filename)]  # 单词名列表
        items = [*MDX(filename).items()]  # 释义html源码列表
        # 存入redis
        r.set('headwords', json.dumps([headword.decode() for headword in headwords]))
        r.set('items', json.dumps([[byte.decode() for byte in item] for item in items]))
    else:
        headwords = json.loads(headwords)
        items = json.loads(items)

    # 查词，返回单词和html文件

    # 只查单词，使用正则过滤
    queryword = re.findall(r"[a-zA-Z]+", queryword)[0]
    html_result = ''
    try:
        wordindex = headwords.index(queryword)
        word, html = items[wordindex]
        word, html_result = word, html
    except ValueError:
        # 首字母大写的问题
        try:
            wordindex = headwords.index(queryword.lower())
            word, html = items[wordindex]
            word, html_result = word, html
        except ValueError:
            return [], []
    # 过滤出例句和翻译
    raw_examples = re.findall(r"<font color=#008080>.*?</font></div>", html_result)
    examples, translations = [], []
    for raw_example in raw_examples:
        example_and_tran = re.sub(r"(<.*?>|</.*?>)", "", raw_example)
        # 分割英文和中文，以中文第一个字切割
        first_chinese = re.search(r"[\u4e00-\u9fa5]", example_and_tran).span()[0]
        example = example_and_tran[0:first_chinese]
        translation = example_and_tran[first_chinese:]
        examples.append(example)
        translations.append(translation)
        # print(example+translation)
    return examples, translations
