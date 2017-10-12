from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    COMMENT_STATUS = (
        ('o', '打开'),
        ('c', '关闭'),

    )

    TYPE = (
        ('a', '文章'),
        ('p', '页面'),
    )

    title = models.CharField('标题', max_length=200)
    body = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)
    pub_time = models.DateTimeField('发布时间', blank=True, null=True, help_text='不指定发布时间则视为草稿，可以指定未来时间，到时将自动发布。')
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    comment_status = models.CharField('评论状态', max_length=1, choices=COMMENT_STATUS, default='o')
    type = models.CharField('类型', max_length=1, choices=TYPE, default='a')
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)

    category = models.ForeignKey('Category',verbose_name='分类',on_delete=models.CASCADE,blank=True,null=True)
    tags = models.ManyToManyField('Tag',verbose_name='标签集合',blank=True,null=True)

    class Meta:
        ordering = ['-pub_time']
        verbose_name = '文章'
        verbose_name_plural ='文章'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={
            'article_id':self.id,
            'year':self.create_time.year,
            'month':self.create_time.month,
            'day':self.create_time.day
        })

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])


    def get_category_tree(self):

        names = []
        def parse(category):
            names.append((category.name,category.get_absolute_url()))
            if category.parent_category:
                parse(category.parent_category)
        parse(self.category)

        return names


class Category(models.Model):
    name = models.CharField('分类名', max_length=30)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)
    parent_category = models.ForeignKey('self', verbose_name='父级分类', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural ='分类'

    def get_absolute_url(self):

        return reverse('blog:category_detail',kwargs={'category_name':self.name})


class Tag(models.Model):
    name = models.CharField('标签名', max_length=30)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural ='标签'


class Links(models.Model):
    name = models.CharField('链接名称', max_length=30)
    sequence = models.IntegerField('排序', unique=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
