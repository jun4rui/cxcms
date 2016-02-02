from django.contrib import admin

from article.models import Article, ArticleType

# Register your models here.

# 模型的管理端定义
class ArticleAdmin(admin.ModelAdmin):
    # 定义在列表页面显示哪些字段
    list_display = ('title', 'detail', 'postTime', 'articleType')

# 模型的管理端定义
class ArticleTypeAdmin(admin.ModelAdmin):
    # 定义在列表页面显示哪些字段
    list_display = ('typeName', 'id')

# 在管理端口绑定那个模型，和模型的管理端定义
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
