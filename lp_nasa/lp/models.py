from django.db import models

from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField(
        max_length=100
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="image"
    )
    pub_date = models.DateField(
        auto_now_add=True
    )
    sort = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('sort',)
