from django.db import models
from django.core.validators import MinValueValidator
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.


class Instance(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, validators=[
                                MinValueValidator(limit_value=1)])

    class Meta:
        abstract = True


class Repo(Instance):
    owner = models.ForeignKey(
        'Owner', related_name='repos', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    private = models.BooleanField()
    html_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(null=True)
    info = models.JSONField(encoder=DjangoJSONEncoder)

    def get_absolute_url(self):
        return "/api/repos/%i/" % self.id


class Owner(Instance):
    login = models.CharField(max_length=200)
    html_url = models.URLField(max_length=500)
    OWNER_TYPE_CHOICES = [
        ('USR', 'User'),
        ('ORG', 'Organization'),
    ]
    type = models.CharField(
        max_length=3,
        choices=OWNER_TYPE_CHOICES,
        default='USR',
    )
    info = models.JSONField(encoder=DjangoJSONEncoder)

    def get_absolute_url(self):
        return "/api/owners/%i/" % self.id
