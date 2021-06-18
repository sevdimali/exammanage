from django.contrib import admin

# Register your models here.
from core.models import Imtahan, Neticeler, ExamCorrect


class ImtahanAdmin(admin.ModelAdmin):
    list_display = ('name', 'tarix',)


class NeticelerAdmin(admin.ModelAdmin):
    list_display = ('descriptions',)


class ExamCorrectAdmin(admin.ModelAdmin):
    list_display = ('descriptions',)


admin.site.register(Imtahan, ImtahanAdmin)
admin.site.register(Neticeler, NeticelerAdmin)
admin.site.register(ExamCorrect, ExamCorrectAdmin)
