from django.contrib import admin

from article.models import Article, ArticleType


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'postTime', 'articleType')


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('typeName', 'id')


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
