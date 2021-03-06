from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

'''
1. 主键不用自己定义，Django会自动加上
'''

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
        verbose_name = '文档分类'
        verbose_name_plural = '文档分类'


# 文档模型
class Article(models.Model):
    # 字符字段
    title = models.CharField(max_length=50, blank=True, verbose_name='标题')
    # 文本字段
    # detail = models.TextField(blank=True, verbose_name='内容')
    # 只要使用RichTextField就能自动在后台呈现可视化编辑器，叼炸天！
    # detail = RichTextField(verbose_name='内容')
    detail = RichTextUploadingField(verbose_name='内容')
    # Datetime字段，默认是当前时间
    postTime = models.DateTimeField(verbose_name='发布时间')
    # 这里是外键
    articleType = models.ForeignKey(ArticleType, verbose_name='文档类型')

    # 定义显示名称
    class Meta:
        verbose_name = '文档管理'
        verbose_name_plural = '文档管理'
