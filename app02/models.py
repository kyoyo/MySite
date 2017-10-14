from django.db import models

# Create your models here.

TITLE_CHOICES =(
    ('MR','Mr.'),
    ('MRS','Mrs.'),
    ('MS','Ms.'),
)

class Author(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3,choices= TITLE_CHOICES)
    birth_date = models.DateField(blank=True,null=True)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __str__(self):

        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'