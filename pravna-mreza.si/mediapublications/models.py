from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.models import Page
from home.models import Objava
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class MediaPublicationsPage(Page):
    headline_first = models.TextField(verbose_name='Naslovnica prvi del', blank=True)
    headline_second = models.TextField(verbose_name='Naslovnica drugi del', blank=True)
    headline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika na naslovnici')

    content_panels = Page.content_panels + [
        FieldPanel('headline_first'),
        FieldPanel('headline_second'),
        FieldPanel('headline_image'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        all_publications = Objava.objects.all().order_by('-date')
        paginator = Paginator(all_publications, 10)
        page = request.GET.get("page")
        try:
            publications = paginator.page(page)
        except PageNotAnInteger:
            publications = paginator.page(1)
        except EmptyPage:
            publications = paginator.page(paginator.num_pages)
        context['publications'] = publications
        return context

    class Meta:
        verbose_name = "Objave medijev"
        verbose_name_plural = "Objave medijev"
