from django.contrib import admin
from .models import Lecture, Session

class LectureAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Session)
