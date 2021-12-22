from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class AchievementTag(models.Model):
    name = models.TextField(verbose_name='Oznaka dosežka', blank=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.TextField(verbose_name='Naslov', blank=True)
    tag = models.ForeignKey(AchievementTag, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    description = models.TextField(verbose_name='Opis', blank=True)
    link = models.URLField(verbose_name='Povezava do predloga zakona', null=True, blank=True)
    link_text = models.TextField(verbose_name='Besedilo na gumbu', blank=True)

    def __str__(self):
        return self.title


class AchievementArchivePage(Page):
    headline_first = models.TextField(verbose_name='Naslovnica prvi del', blank=True)
    headline_second = models.TextField(verbose_name='Naslovnica drugi del', blank=True)
    headline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika na naslovnici')

    content_panels = Page.content_panels + [
        FieldPanel('headline_first'),
        FieldPanel('headline_second'),
        ImageChooserPanel('headline_image'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        achievements_by_year = {}

        # get all years
        date_list = Achievement.objects.all().dates('date', 'year').order_by('-date')

        for year in date_list:
            achievements_by_year[year.year] = Achievement.objects.filter(date__year = year.year).order_by('-date')

        context['achievements_by_year'] = achievements_by_year
        return context
