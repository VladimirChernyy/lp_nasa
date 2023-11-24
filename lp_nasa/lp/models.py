from django.db import models


class SliderImage(models.Model):
    title = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to='images/%Y/%m'
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
