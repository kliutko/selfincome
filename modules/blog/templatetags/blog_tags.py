from django import template
from django.db.models import Count
from taggit.models import Tag

from ..models import Comment, Article
from datetime import datetime, date, time, timedelta
from django import template
from django.db.models import Count, Q
from django.utils import timezone


register = template.Library()

@register.simple_tag
def popular_tags():
    tags = Tag.objects.annotate(num_times=Count('article')).order_by('-num_times')
    tag_list = list(tags.values('name', 'num_times', 'slug'))
    return tag_list

@register.inclusion_tag('includes/latest_comments.html')
def show_latest_comments(count=5):
    comments = Comment.objects.select_related('author').filter(status='published').order_by('-time_create')[:count]
    return {'comments': comments}






@register.simple_tag
def popular_articles():
    # получаем текущую дату и время в формате datetime
    now = timezone.now()
    # вычисляем дату начала дня (00:00) 7 дней назад
    start_date = now - timedelta(days=7)
    # вычисляем дату начала текущего дня (00:00)
    today_start = timezone.make_aware(datetime.combine(date.today(), time.min))
    # получаем все статьи и количество их просмотров за последние 7 дней
    articles = Article.objects.annotate(
        total_view_count=Count('views', filter=Q(views__viewed_on__gte=start_date)),
        today_view_count=Count('views', filter=Q(views__viewed_on__gte=today_start))
    ).prefetch_related('views')
    # сортируем статьи по количеству просмотров в порядке убывания, сначала по просмотрам за сегодня, затем за все время
    popular_articles = articles.order_by('-total_view_count', '-today_view_count')[:4]
    return popular_articles