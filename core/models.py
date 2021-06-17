from django.db import models


# Create your models here.

class BaseModel(models.Model):
    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("cdate",)
        abstract = True


class Imtahan(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    tarix = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"


class Neticeler(BaseModel):
    file = models.FileField(null=True, upload_to='upload', blank=True)
    imtahan_id = models.ManyToManyField(Imtahan, blank=True)
    descriptions = models.TextField(null=True, blank=True)


class ExamCorrect(BaseModel):
    file = models.FileField(null=True, upload_to='upload', blank=True)
    imtahan_id = models.ManyToManyField(Imtahan, blank=True)
    descriptions = models.TextField(null=True, blank=True)
