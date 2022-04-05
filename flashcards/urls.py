from django.urls import path

from flashcards.views import *

app_name = 'flashcards'
urlpatterns = [
    path('', index, name='dashboard'),
    # path('<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('<int:card_id>', card_detailview, name='card_detail'),
    path('next/', nextcardview, name='next'),
    path("recite/<int:card_id>/<int:rank>", cardreciteview, name="recite"),
    path("recitedata/", recitedatadisplay, name="display"),
    path('search/', search, name='search'),
    path('undo/<int:card_id>', undo, name='undo'),
    path('undo_list/<int:list_id>/<int:progress>/', undo_list, name='undo_list'),
    path('websearch/', websearch, name='websearch'),
    path('dict/', dict_search, name='dict'),
    path('create_wordlist_by_diff/', create_wordlist_by_diff, name='create_wordlist_by_diff'),
    path('create_wordlist_by_tag/', create_wordlist_by_tag, name='create_wordlist_by_tag'),
    path('delete_wordlist/<int:wordlist_id>/', delete_wordlist, name='delete_wordlist'),
    path('recite_wordlist/<int:wordlist_id>/<int:progress>/<int:rank>/', recite_wordlist, name='recite_wordlist'),
    path('word_add_tags/<int:word_id>/<slug:tag>/<int:section>/', word_add_tags, name='word_add_tags'),
    path('word_delete_tags/<int:word_id>/<int:tag_id>/<int:section>/', word_delete_tags, name='word_delete_tags'),
    path('word_edit/<int:word_id>/<int:section>/', word_edit, name='word_edit'),
    path('word_add/', word_add, name='word_add'),
    path('word_delete/<int:word_id>/', word_delete, name='word_delete'),
    path('settings/', settings_view, name='settings_view'),
    path('dict_query/', dict_query, name='dict_query'),
    path('get_example/', get_example, name='get_example'),
    path('export_card_as_txt/', export_card_as_txt, name='export_card_as_txt'),
    path('export_db/', export_db, name='export_db'),
    path('card_recitedata_view/<int:card_id>/', card_recitedata_view, name='card_recitedata_view'),
    path('dict_query_get/<slug:query_word>/', dict_query_get, name='dict_query_get'),
]
