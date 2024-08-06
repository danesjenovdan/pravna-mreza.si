from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class Author(models.Model):
    name = models.TextField()
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika')

    content_panels = [
        FieldPanel('name'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name


class BlogPage(Page):
    date = models.DateField(verbose_name='Datum')
    preview_text = RichTextField(verbose_name='Opis na seznamu', blank=False, null=False, default='')
    preview_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika')
    intro_text = RichTextField(blank=True, null=True, verbose_name='Opis pod naslovom')
    related_blog_posts = StreamField(
        [('blog_post', blocks.PageChooserBlock(label="Povezava do blog zapisa")),],
        blank=True,
        null=True,
        # min_num=0,
        # max_num=3,
        verbose_name="Povezani blog zapisi"
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], verbose_name='Besedilo')
    meta_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='OG slika'
    )

    @property
    def authors(self):
        authors = [
            n.author for n in self.blog_author_relationship.all()
        ]
        return authors

    @property
    def authors_list_string(self):
        return ', '.join([str(elem) for elem in self.authors])


    content_panels = Page.content_panels + [
        FieldPanel('date'),
        InlinePanel('blog_author_relationship', label='Avtorji'),
        FieldPanel('preview_text'),
        FieldPanel('preview_image'),
        FieldPanel('intro_text'),
        FieldPanel('body'),
        FieldPanel('related_blog_posts'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("meta_image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        try:
            homepage = Page.objects.get(slug='home')
            blogpost_archive = homepage.specific.blog_section_archive_link.url
        except:
            blogpost_archive = '/'
        context['blogpost_archive'] = blogpost_archive
        return context

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"


class BlogAuthorRelationship(models.Model):
    # the model that connects blog posts and authors
    blog = ParentalKey(
        'BlogPage',
        related_name='blog_author_relationship',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'Author',
        related_name="+",
        on_delete=models.CASCADE,
        verbose_name='Avtor_ica'
    )

    panels = [
        FieldPanel('author')
    ]


class BlogArchivePage(Page):
    headline_first = models.TextField(verbose_name='Naslovnica prvi del', blank=True)
    headline_second = models.TextField(verbose_name='Naslovnica drugi del', blank=True)
    headline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Slika na naslovnici')

    content_panels = Page.content_panels + [
        FieldPanel('headline_first'),
        FieldPanel('headline_second'),
        FieldPanel('headline_image'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        # Get all blogposts
        all_blogposts = BlogPage.objects.all().live().order_by('-first_published_at')
        # Paginate all novice by 2 per page
        paginator = Paginator(all_blogposts, 10)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            blogposts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            blogposts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            blogposts = paginator.page(paginator.num_pages)
        context['blogposts'] = blogposts
        return context

    class Meta:
        verbose_name = "Seznam blog zapisov"
        verbose_name_plural = "Seznam blog zapisov"
