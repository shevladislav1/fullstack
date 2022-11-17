from django.db import models

class TestModels(models.Model):
    title = models.CharField('Заголовок', max_length=150, null=False, unique=True, blank=True)

    def __str__(self) -> str:
        return self.title