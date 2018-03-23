from django.db import models

class Article(models.Model)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture=models.ImageField(upload_to="user")
    likes= models.Integer()
     published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
