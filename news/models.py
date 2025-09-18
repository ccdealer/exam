from django.db import models

class Article(models.Model):
    source_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Источник ID"
    )
    source_name = models.CharField(
        max_length=255,
        verbose_name="Название источника",
        null=True,
        blank=True
    )
    author = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Автор"
    )
    title = models.CharField(
        max_length=500,
        verbose_name="Заголовок",
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    url = models.URLField(
        unique=True,
        verbose_name="Ссылка на статью"
    )
    url_to_image = models.URLField(
        null=True,
        blank=True,
        verbose_name="Ссылка на картинку статьи"
    )
    published_at = models.DateTimeField(
        verbose_name="Дата публикации",
        null=True,
        blank=True
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="Содержание"
    )

    class Meta:
        ordering = ["published_at"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title