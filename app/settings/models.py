from django.db import models


class TherapyPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_image = models.ImageField(
        upload_to="therapy/banner/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class PopularService(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    order = models.CharField(max_length=10, default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class TherapyService(models.Model):
    title = models.CharField(max_length=255)
    order = models.CharField(max_length=10, default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
