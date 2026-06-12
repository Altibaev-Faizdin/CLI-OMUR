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


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL-имя")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="Категория",
    )
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="services/", blank=True, null=True, verbose_name="Изображение"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["order"]

    def __str__(self):
        return self.name



class Specialist(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    specialization = models.CharField(max_length=255, verbose_name="Специализация")
    experience = models.CharField(max_length=255, verbose_name="Стаж")
    photo = models.ImageField(upload_to="specialists/", verbose_name="Фото")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ["order"]

    def __str__(self):
        return self.full_name





class ClinicLeader(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="about/leader/", blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Руководитель клиники"
        verbose_name_plural = "Руководитель клиники"

    def __str__(self):
        return self.full_name




class AboutClinic(models.Model):
    history = models.TextField(verbose_name="История")
    mission = models.TextField(verbose_name="Миссия")
    values = models.TextField(verbose_name="Ценности")

    class Meta:
        verbose_name = "О клинике"
        verbose_name_plural = "О клинике"

    def __str__(self):
        return "О клинике"



class WhyUs(models.Model):
    icon = models.ImageField(upload_to="about/why_us/", blank=True, null=True, verbose_name="Иконка")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.CharField(max_length=500, verbose_name="Описание")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Почему выбирают нас"
        verbose_name_plural = "Почему выбирают нас"
        ordering = ["order"]

    def __str__(self):
        return self.title