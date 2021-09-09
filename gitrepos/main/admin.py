from django.contrib import admin
from .models import Repo, Owner

# Register your models here.


admin.site.register(Repo)
admin.site.register(Owner)
