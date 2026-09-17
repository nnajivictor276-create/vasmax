from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=100)
    code = models.TextField(help_text="Paste your Adsterra/ExoClick script here")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    slug = models.SlugField(unique=True, help_text="e.g: test, youtube1")
    destination_url = models.URLField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug