from django.utils.translation import gettext_lazy as _
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# class ProjectTag(models.Model):
#     name = models.TextField()

#     def __str__(self):
#         return self.name


class ProjectsBlock(blocks.StructBlock):
    project = blocks.PageChooserBlock(page_type="projects.ProjectPage")

    class Meta:
        label = _("Projekt")


class ProjectPage(Page):
    # date = models.DateField()
    preview_text = RichTextField(blank=False, null=False, default="")
    # tag = models.ForeignKey(ProjectTag, on_delete=models.SET_NULL, null=True, blank=True)
    preview_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    intro_text = RichTextField(blank=True, null=True, verbose_name="Opis")
    body = StreamField(
        [
            ("paragraph", blocks.RichTextBlock()),
        ]
    )
    meta_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="OG slika",
    )

    content_panels = Page.content_panels + [
        # FieldPanel('date'),
        # FieldPanel('tag'),
        FieldPanel("preview_text", classname="full"),
        FieldPanel("preview_image"),
        FieldPanel("intro_text"),
        FieldPanel("body"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("meta_image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        try:
            projects_archive = ProjectsArchivePage.objects.first().url
        except:
            projects_archive = "/"
        context["projects_archive"] = projects_archive
        return context

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekti"


class ProjectsArchivePage(Page):
    headline_first = models.TextField(verbose_name="Naslovnica prvi del", blank=True)
    headline_second = models.TextField(verbose_name="Naslovnica drugi del", blank=True)
    headline_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika na naslovnici",
    )
    projects = StreamField(
        [
            ("project", ProjectsBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("headline_first"),
        FieldPanel("headline_second"),
        FieldPanel("headline_image"),
        FieldPanel("projects"),
    ]

    # def get_context(self, request):
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super().get_context(request)
    #     # all_projects = ProjectPage.objects.all().live().order_by("-first_published_at")
    #     all_projects = self.projects
    #     paginator = Paginator(all_projects, 10)
    #     page = request.GET.get("page")
    #     try:
    #         projects = paginator.page(page)
    #     except PageNotAnInteger:
    #         projects = paginator.page(1)
    #     except EmptyPage:
    #         projects = paginator.page(paginator.num_pages)
    #     context["projects"] = projects
    #     return context

    class Meta:
        verbose_name = "Seznam projektov"
        verbose_name_plural = "Seznami projektov"
