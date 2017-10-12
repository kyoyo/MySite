from django import template
from app01.models import Article,Category
from django.template.defaultfilters import stringfilter
import markdown2
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.conf import settings
from app01.models import Article
import datetime


register = template.Library()

@register.inclusion_tag('app01/tags/article_info.html')
def load_article_detail(article,isindex,user):
    return {
        'article':article,
        'isindex':isindex,
        'user':user
    }

@register.inclusion_tag('app01/tags/sidebar.html')
def load_sidebar(user):
    recent_articles = Article.objects.filter(status='p')[:settings.ARTICLE_SUB_LENGTH]
    sidebar_categorys = Category.objects.all()
    most_read_articles = Article.objects.filter(status='p').order_by('-views')[:settings.ARTICLE_SUB_LENGTH]

    return {
        'recent_articles': recent_articles,
        'sidebar_categorys':sidebar_categorys,
        'most_read_articles':most_read_articles,
        'user':user
    }

@register.filter(is_safe=True)
@stringfilter
def truncatechars_content(content):
    from django.template.defaultfilters import truncatechars_html

    return truncatechars_html(content,50)


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):

    return mark_safe(markdown2.markdown(force_text(content),extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables",
                                                                    "spoiler"]))
@register.inclusion_tag('app01/tags/breadcrumb.html')
def load_breadcrumb(article):
    names = article.get_category_tree()
    names.append((settings.SITE_NAME,'http://127.0.0.1:8000'))
    names = names[::-1]

    return {
        'names':names,
        'article':article
    }

@register.assignment_tag
def query(qs,**kwargs):
    """ template tag which allows queryset filtering. Usage:
      {% query books author=author as mybooks %}
      {% for book in mybooks %}
        ...
      {% endfor %}
    """
    return qs.filter(**kwargs)
"""
article = Article.objects.get(pk=4)
comments = Comment.objects.filter(article=article)
for c in comments.filter(parent_comment=None):
    datas = parse_commenttree(comments, c)
    print(datas)
"""
@register.filter
def getravatar():
    pass

@register.inclusion_tag('app01/tags/article_meta_info.html')
def load_article_metas(article,user):
    return {
        'article':article,
        'user':user
    }

@register.simple_tag
def datetimeformat(data):
    return data.strftime(settings.DATE_TIME_FORMAT)