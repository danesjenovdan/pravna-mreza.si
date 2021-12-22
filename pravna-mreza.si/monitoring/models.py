from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class MonitoringPage(Page):
    date = models.DateField()
    preview_text = RichTextField(blank=False, null=False, default='')
    intro_text = RichTextField(blank=True, null=True, verbose_name='Opis')
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('preview_text'),
        FieldPanel('intro_text'),
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        if self.get_parent().specific.monitor_archive_link:
            monitoring_archive = self.get_parent().specific.monitor_archive_link.url
        else:
            monitoring_archive = '/'
        context['monitoring_archive'] = monitoring_archive
        return context


class MonitoringArchivePage(Page):
    headline_first = models.TextField(verbose_name='Naslovnica prvi del', blank=True)
    headline_second = models.TextField(verbose_name='Naslovnica drugi del', blank=True)
    headline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika na naslovnici')
    intro_text = RichTextField(blank=True, null=True, verbose_name='Opis')
    get_in_touch = models.URLField(verbose_name='Povezava v opisu', blank=True, null=True)
    get_in_touch_text = models.TextField(verbose_name='Ime povezave', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline_first'),
        FieldPanel('headline_second'),
        ImageChooserPanel('headline_image'),
        FieldPanel('intro_text'),
        FieldPanel('get_in_touch'),
        FieldPanel('get_in_touch_text'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        # Get all monitoring pages
        all_monitoring = MonitoringPage.objects.all().live().order_by('-first_published_at')
        # Paginate all monitoring pages
        paginator = Paginator(all_monitoring, 10)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            monitoring_pages = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            monitoring_pages = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            monitoring_pages = paginator.page(paginator.num_pages)
        context['monitoring_pages'] = monitoring_pages
        return context
