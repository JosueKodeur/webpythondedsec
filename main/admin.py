from django.contrib import admin
from .models import *
from django.db import models
from tinymce.widgets import TinyMCE


# Register your models here.


class TutorielAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["titre_tutoriel", "publication_tutoriel"]}),
        ("URL", {"fields": ["tutoriel_slug"]}),
        ("", {"fields": ["tutoriel_series"]}),
        ("Content", {'fields': ["content_tutoriel"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(TutorielSeries)
admin.site.register(TutorielCategorie)

admin.site.register(Tutoriel, TutorielAdmin)
