from django.db import models


# Create your models here.


# 文档类型模型
class ArticleType(models.Model):
    # 字符字段
    typeName = models.CharField(max_length=50, verbose_name='类型名称')

    # PY2:如果要让外键在admin中不是用xxx object显示，而是你希望的字段显示，那就需要手工添加__str__
    def __unicode__(self):
        return self.typeName

    # PY3:如果要让外键在admin中不是用xxx object显示，而是你希望的字段显示，那就需要手工添加__str__
    def __str__(self):
        return self.typeName

    # 定义显示的名字
    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'


# 文档模型
class Article(models.Model):
    # 字符字段
    title = models.CharField(max_length=50, blank=True, verbose_name='标题')
    # 文本字段
    detail = models.TextField(blank=True, verbose_name='内容')
    # Datetime字段，默认是当前时间
    postTime = models.DateTimeField(verbose_name='发布时间')
    # 这里是外键
    articleType = models.ForeignKey(ArticleType, verbose_name='文档类型')

    # 定义显示名称
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'
