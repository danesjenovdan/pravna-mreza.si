from django.utils.translation import gettext_lazy as _
from django.db import models
from novice.models import NovicaPage
from blog.models import BlogPage
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet


class ExternalLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(label=_('Ime'))
    url = blocks.URLBlock(label=_('Povezava'))
    has_border = blocks.BooleanBlock(label='Gumb ima obrobo?', required=False)

    class Meta:
        label = _('Zunanja povezava')
        icon = 'link'


class PageLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=False, label=_('Ime'), help_text=_('Če je prazno se uporabi naslov strani.'))
    page = blocks.PageChooserBlock(label=_('Stran'))
    has_border = blocks.BooleanBlock(label='Gumb ima obrobo?', required=False)

    class Meta:
        label = _('Povezava do strani')
        icon = 'link'


class EmailLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(label=_('Ime'))
    email = blocks.EmailBlock(label=_('Email povezava'))

    class Meta:
        label = _('Email povezava')
        icon = 'link'


@register_snippet
class Infopush(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Naslov (neobvezno)')
    text = RichTextField(verbose_name='Opis')
    page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do strani (neobvezno)')
    page_text = models.TextField(null=True, blank=True, verbose_name='Besedilo na gumbu s povezavo (neobvezno)')

    panels = [
        FieldPanel('title'),
        FieldPanel('text', classname="full"),
        FieldPanel('page_text'),
        PageChooserPanel('page'),
    ]

    def __str__(self):
        return self.title


@register_setting
class OgSettings(BaseSetting):
    og_title = models.CharField(max_length=255)
    og_description = models.CharField(max_length=255)
    og_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('og_title'),
        FieldPanel('og_description'),
        ImageChooserPanel('og_image'),
    ]


@register_setting()
class NavigationSettings(BaseSetting):
    navigation_links = StreamField(
        [
            ('page_link', PageLinkBlock()),
            ('external_link', ExternalLinkBlock()),
        ],
        verbose_name=_("Povezave v glavi"),
    )

    panels = [
        StreamFieldPanel("navigation_links"),
    ]

    class Meta:
        verbose_name = 'Navigacija'


@register_setting()
class FooterSettings(BaseSetting):
    footer_text = models.TextField(verbose_name='Besedilo v footerju', blank=True)
    facebook_link = models.URLField(verbose_name='Facebook URL', blank=True, null=True)
    twitter_link = models.URLField(verbose_name='Twitter URL', blank=True, null=True)
    instagram_link = models.URLField(verbose_name='Instagram URL', blank=True, null=True)
    footer_links_left = StreamField(
        [
            ("page_link", PageLinkBlock()),
            ("external_link", ExternalLinkBlock()),
            ("email_link", EmailLinkBlock()),
        ],
        verbose_name=_("Povezave v nogi na levi"),
    )
    footer_links_right = StreamField(
        [
            ("page_link", PageLinkBlock()),
            ("external_link", ExternalLinkBlock()),
            ("email_link", EmailLinkBlock()),
        ],
        verbose_name=_("Povezave v nogi na desni"),
    )

    panels = [
        FieldPanel('footer_text'),
        FieldPanel('facebook_link'),
        FieldPanel('twitter_link'),
        FieldPanel('instagram_link'),
        StreamFieldPanel("footer_links_left"),
        StreamFieldPanel("footer_links_right"),
    ]

    class Meta:
        verbose_name = 'Footer'


@register_setting()
class SocialMedia(BaseSetting):
    social_media_title_part_one = models.TextField(verbose_name='Naslov 1. del', blank=True)
    social_media_title_part_two = models.TextField(verbose_name='Naslov 2. del', blank=True)
    facebook_link = models.URLField(verbose_name='Facebook URL', blank=True, null=True)
    twitter_link = models.URLField(verbose_name='Twitter URL', blank=True, null=True)
    instagram_link = models.URLField(verbose_name='Instagram URL', blank=True, null=True)

    panels = [
        FieldPanel('social_media_title_part_one'),
        FieldPanel('social_media_title_part_two'),
        FieldPanel('facebook_link'),
        FieldPanel('twitter_link'),
        FieldPanel('instagram_link'),
    ]

    class Meta:
        verbose_name = 'Družbena omrežja'


@register_setting()
class Newsletter(BaseSetting):
    newsletter_title_part_one = models.TextField(verbose_name='Naslov 1. del', blank=True)
    newsletter_title_part_two = models.TextField(verbose_name='Naslov 2. del', blank=True)
    newsletter_terms = models.TextField(verbose_name='Novičnik pogoji', blank=True)
    newsletter_success = models.TextField(verbose_name='Sporočilo ob uspešni prijavi', blank=True)
    newsletter_failure = models.TextField(verbose_name='Sporočilo ob neuspešni prijavi', blank=True)

    panels = [
        FieldPanel('newsletter_title_part_one'),
        FieldPanel('newsletter_title_part_two'),
        FieldPanel('newsletter_terms'),
        FieldPanel('newsletter_success'),
        FieldPanel('newsletter_failure'),
    ]

    class Meta:
        verbose_name = 'Novičnik'


@register_setting()
class Support(BaseSetting):
    support_title_part_one = models.TextField(verbose_name='Naslov 1. del', blank=True)
    support_title_part_two = models.TextField(verbose_name='Naslov 2. del', blank=True)
    support_text = models.TextField(verbose_name='Opis', blank=True)
    support_button = models.TextField(verbose_name='Besedilo na gumbu', blank=True)
    support_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava')

    panels = [
        FieldPanel('support_title_part_one'),
        FieldPanel('support_title_part_two'),
        FieldPanel('support_text'),
        FieldPanel('support_button'),
        FieldPanel('support_link'),
    ]

    class Meta:
        verbose_name = 'Donacije'


@register_setting()
class Monitor(BaseSetting):
    monitor_title_part_one = models.TextField(verbose_name='Naslov 1. del', blank=True)
    monitor_title_part_two = models.TextField(verbose_name='Naslov 2. del', blank=True)
    monitor_text = models.TextField(verbose_name='Opis', blank=True)
    monitor_button = models.TextField(verbose_name='Besedilo na gumbu', blank=True)
    monitor_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava')

    panels = [
        FieldPanel('monitor_title_part_one'),
        FieldPanel('monitor_title_part_two'),
        FieldPanel('monitor_text'),
        FieldPanel('monitor_button'),
        FieldPanel('monitor_link'),
    ]

    class Meta:
        verbose_name = 'Prispevaj'


class Objava(models.Model):
    title = models.TextField()
    url = models.URLField()
    source = models.TextField()
    date = models.DateField()

    panels = [
        FieldPanel('title'),
        FieldPanel('url', classname="full"),
        FieldPanel('source'),
        FieldPanel('date'),
    ]

    def __str__(self):
        return self.title


class HomePage(Page):
    intro_text = RichTextField(blank=True, null=True)
    intro_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    news_section_title = models.TextField(verbose_name='Naslov sekcije z novicami', blank=True)
    news_section_archive_link_title = models.TextField(verbose_name='Ime povezave do seznama novic', blank=True)
    news_section_archive_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do seznama novic')
    blog_section_title = models.TextField(verbose_name='Naslov blog sekcije', blank=True)
    blog_section_archive_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do seznama blog zapisov')
    blog_section_archive_link_title = models.TextField(verbose_name='Ime povezave do seznama blog zapisov', blank=True)
    monitor_archive_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do seznama monitoring zapisov')

    content_panels = Page.content_panels + [
        FieldPanel('intro_text', classname="full"),
        ImageChooserPanel('intro_image'),
        FieldPanel('news_section_title'),
        FieldPanel('news_section_archive_link_title'),
        FieldPanel('news_section_archive_link'),
        FieldPanel('blog_section_title'),
        FieldPanel('blog_section_archive_link'),
        FieldPanel('blog_section_archive_link_title'),
        FieldPanel('monitor_archive_link'),
    ]

    parent_page_types = []

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        novice = NovicaPage.objects.all().live().order_by('-first_published_at')[:3]
        blogposts = BlogPage.objects.all().live().order_by('-first_published_at')[:1]
        context['novice'] = novice
        context['blogposts'] = blogposts
        # context['pojavljanja'] = pojavljanja
        return context

    class Meta:
        verbose_name = "Domača stran"
        verbose_name_plural = "Domače strani"


class GenericPage(Page):
    headline_first = models.TextField(verbose_name='Naslovnica prvi del', blank=True)
    headline_second = models.TextField(verbose_name='Naslovnica drugi del', blank=True)
    headline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika na naslovnici')
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ])
    social_media_box = models.BooleanField(default=False, verbose_name='Škatla družbena omrežja')
    newsletter_box = models.BooleanField(default=False, verbose_name='Škatla novičnik')
    support_box = models.BooleanField(default=False, verbose_name='Škatla podpri')
    monitor_box = models.BooleanField(default=False, verbose_name='Škatla prispevaj')

    content_panels = Page.content_panels + [
        FieldPanel('headline_first'),
        FieldPanel('headline_second'),
        ImageChooserPanel('headline_image'),
        StreamFieldPanel('body'),
        FieldPanel('monitor_box'),
        FieldPanel('newsletter_box'),
        FieldPanel('social_media_box'),
        FieldPanel('support_box'),
    ]

    class Meta:
        verbose_name = "Generična stran"
        verbose_name_plural = "Generične strani"


class DonationPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ])
    left_box_heading_part_one = models.TextField(blank=True, verbose_name='Leva škatla - naslov prvi del')
    left_box_heading_part_two = models.TextField(blank=True, verbose_name='Leva škatla - naslov drugi del')
    left_box_description = models.TextField(blank=True, verbose_name='Leva škatla - opis')    
    left_box_button_text = models.TextField(blank=True, verbose_name='Leva škatla - gumb besedilo')
    left_box_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Leva škatla - gumb povezava')
    right_box_heading_part_one = models.TextField(blank=True, verbose_name='Desna škatla - naslov prvi del')
    right_box_heading_part_two = models.TextField(blank=True, verbose_name='Desna škatla - naslov drugi del')
    right_box_description = models.TextField(blank=True, verbose_name='Desna škatla - opis')    
    right_box_button_text = models.TextField(blank=True, verbose_name='Desna škatla - gumb besedilo')
    right_box_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Desna škatla - gumb povezava')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('left_box_heading_part_one'),
        FieldPanel('left_box_heading_part_two'),
        FieldPanel('left_box_description'),
        FieldPanel('left_box_button_text'),
        FieldPanel('left_box_button_link'),
        FieldPanel('right_box_heading_part_one'),
        FieldPanel('right_box_heading_part_two'),
        FieldPanel('right_box_description'),
        FieldPanel('right_box_button_text'),
        FieldPanel('right_box_button_link'),
    ]

    class Meta:
        verbose_name = "Donacijska stran (z gumbi)"
        verbose_name_plural = "Donacijske strani (z gumbi)"


class DonationEmbedPage(Page):
    embed_url = models.URLField()

    content_panels = Page.content_panels + [
        FieldPanel('embed_url', classname="full"),
    ]

    class Meta:
        verbose_name = "Donacijska stran z embedom"
        verbose_name_plural = "Donacijske strani z embedom"


class NewsletterPage(Page):
    headline_first = models.TextField(verbose_name='Naslovnica prvi del', blank=True)
    headline_second = models.TextField(verbose_name='Naslovnica drugi del', blank=True)
    headline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika na naslovnici')
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Opis"),
    )

    content_panels = Page.content_panels + [
        FieldPanel('headline_first'),
        FieldPanel('headline_second'),
        ImageChooserPanel('headline_image'),
        FieldPanel("description"),
    ]

    class Meta:
        verbose_name = "Urejanje naročnine"
        verbose_name_plural = "Urejanja naročnin"


class MaintenancePage(Page):
    text = models.TextField(verbose_name='Besedilo', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]
