from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'article'
    # 自定义admin中显示的APP名称，记得还要去__init__.py中添加一行
    verbose_name = '文档管理'

