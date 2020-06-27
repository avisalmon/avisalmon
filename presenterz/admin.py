from django.contrib import admin
from .models import Lecture, Session, Participation

class LectureAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


class ParticipationAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Session)
admin.site.register(Participation, ParticipationAdmin)
