from django.contrib import admin
from . import models
# Register your models here.

# for slug fields. auto fillup slug fields in admin panale

class TutionClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(models.TutionClassModel, TutionClassAdmin)
admin.site.register(models.TutionModel)
admin.site.register(models.ReviewModel)