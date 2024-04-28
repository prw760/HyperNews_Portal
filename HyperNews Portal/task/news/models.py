from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class META:
        abstract = True


class News(BaseModel):
    created = models.DateTimeField(null=True, blank=True)
    text = models.TextField()
    title = models.CharField(max_length=128)
    link = models.IntegerField(default=0)

    class META:
        ordering = ['title', 'created']

    def __str__(self, *args, **kwargs):
        return f'{self.title}, {self.created}, {self.text}, {self.link}'
