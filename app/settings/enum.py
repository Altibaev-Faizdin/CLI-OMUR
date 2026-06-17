from django.db import models
from django.utils.translation import gettext_lazy as _


class ServiceType(models.TextChoices):
    THERAPY = "therapy", _("Терапия")
    DIAGNOSTICS = "diagnostics", _("Диагностика")
    VACCINATION = "vaccination", _("Вакцинация")
    NEUROLOGY = "neurology", _("Неврология")


class SpecialistType(models.TextChoices):
    THERAPY = "therapy", _("Терапия")
    DIAGNOSTICS = "diagnostics", _("Диагностика")
    VACCINATION = "vaccination", _("Вакцинация")
    NEUROLOGY = "neurology", _("Неврология")