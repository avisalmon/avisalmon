from django.contrib import admin
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Lecture, LectureAdmin)
