from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=80)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
