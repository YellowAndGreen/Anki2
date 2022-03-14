import newspaper
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import *


def article_detailview(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request,
                  'reader/read_article.html',
                  {'title': article.title,
                   'content': article.content
                   })


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 10)  # 20 articles in each page
    page = request.GET.get('page')  # 当前页数

    try:
        current_page_articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        current_page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        current_page_articles = paginator.page(paginator.num_pages)
    return render(request,
                  'reader/article_list.html',
                  {'articles': current_page_articles,
                   'page': page,
                   })


def update_article(request):
    url = 'https://www.cnn.com/'
    if 'url' in request.POST and request.POST['url'][0:4] == 'http':
        url = request.POST['url']
    cnn = newspaper.build(url, languange='en', memoize_articles=False)
    print(f"开始，共有{len(cnn.articles)}篇文章")
    count_num = 0
    # 增加一篇文章，删除一篇id最前的文章
    id_article = Article.objects.all()[0].id
    for article in cnn.articles:
        try:
            article.download()
            article.parse()
        except Exception as e:
            print(e)
            continue
        if article.text == "" or article.title == "" or len(article.text) < 2000:
            print(f'太短！只有{len(article.text)}字符')
            continue
        else:

            count_num += 1
            print(f'{count_num}/100，有{len(article.text)}个字符')
            art_model = Article(title=article.title, content=article.text)
            if article.top_image != '':
                art_model.top_image_url = article.top_image
            art_model.save()
            get_object_or_404(Article, id=id_article).delete()
            id_article += 1

            if count_num == 100:
                print('大功告成')
                break
    print(f"更新{count_num}篇文章")
    messages.success(request, f"更新{count_num}篇文章")
    return JsonResponse({'status': 'ok'})


def read_book(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # 20 articles in each page
    page = request.GET.get('page')  # 当前页数

    try:
        current_page_books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        current_page_books = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        current_page_books = paginator.page(paginator.num_pages)
    return render(request,
                  'reader/book_list.html',
                  {'books': current_page_books,
                   'page': page,
                   }
                  )


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # 字节码转换
    book.content = book.content.decode()
    return render(request,
                  'reader/book_detail.html',
                  {'book': book,
                   })


def book_progress(request):
    progress = request.POST.get('progress')
    book_id = request.POST.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    if progress and book_id:
        book.progress = progress
        book.save()
        return JsonResponse({'status': '保存成功'})
    return JsonResponse({'progress': book.progress})
