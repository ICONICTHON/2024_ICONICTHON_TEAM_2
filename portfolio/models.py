from django.db import models

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('club', '동아리'),
        ('volunteer', '봉사'),
        ('competition', '공모전/대회'),
        ('lecture', '학교강의'),
    ]
    kind = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=30)
    starttime = models.DateTimeField()
    finishtime = models.DateTimeField()
    name = models.CharField(max_length=30)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title  # It might be more useful to return the title or a more unique field
