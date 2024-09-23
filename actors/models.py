from django.db import models

# Create your models here.
NATIONALITY_CHOICES = (

    ('USA', 'Estados Unidos'), # valor a esquerda, salvo no banco, valor à direito mostrado no app
    ('BRASIL', 'Brasil'),
)
    
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
