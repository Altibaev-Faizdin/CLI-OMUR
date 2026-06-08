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

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["sort_order", "id"]


class PatientTip(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="patient_tips/")
    button_text = models.CharField(max_length=255, blank=True)
    button_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Совет для пациентов'
        verbose_name_plural = 'Советы для пациентов'

class VideoMaterial(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="video_materials/")
    video_url = models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Видео материал'
        verbose_name_plural = 'Видео материалы'


class RecommendedSpecialist(BaseModel):
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="specialists/")
    profile_url = models.URLField(blank=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Рекомендуемый специалист'
        verbose_name_plural = 'Рекомендуемые специалисты'


class PreparationArticle(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья для подготовки'
        verbose_name_plural = 'Статьи для подготовки'


class PreparationArticleImage(models.Model):
    article = models.ForeignKey(
        PreparationArticle,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="preparation_articles/")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Изображение для статьи подготовки'
        verbose_name_plural = 'Изображения для статей подготовки'


class FAQ(BaseModel):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'
