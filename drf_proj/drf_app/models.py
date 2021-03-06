from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title