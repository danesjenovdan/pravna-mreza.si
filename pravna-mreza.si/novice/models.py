from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class NovicaTag(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class NovicaPage(Page):
    date = models.DateField()
    preview_text = RichTextField(blank=False, null=False, default='')
    tag = models.ForeignKey(NovicaTag, on_delete=models.SET_NULL, null=True, blank=True)
    preview_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    intro_text = RichTextField(blank=True, null=True, verbose_name='Opis')
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ])
    meta_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='OG slika'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('tag'),
        FieldPanel('preview_text', classname="full"),
        ImageChooserPanel('preview_image'),
        FieldPanel('intro_text'),
        StreamFieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + [
        ImageChooserPanel("meta_image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        if self.get_parent().specific.news_section_archive_link:
            novice_archive = self.get_parent().specific.news_section_archive_link.url
        else:
            novice_archive = '/'
        context['novice_archive'] = novice_archive
        return context


class NovicaArchivePage(Page):
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
        # Get all novice
        vse_novice = NovicaPage.objects.all().live().order_by('-first_published_at')
        # Paginate all novice by 2 per page
        paginator = Paginator(vse_novice, 10)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            novice = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            novice = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            novice = paginator.page(paginator.num_pages)
        context['novice'] = novice
        return context
