from typing import List

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Tag(models.Model):
    text = models.CharField(unique=True, max_length=64)
    level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.text = self.text.lower()
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.TextField()
    slug = models.SlugField()

    tags = models.ManyToManyField(Tag)

    source = models.URLField(null=True, blank=True)

    created_by = models.ForeignKey(User,
                                   related_name='created_by',
                                   on_delete=models.PROTECT,
                                   editable=True,
                                   null=False,
                                   blank=False)

    verified_by = models.ForeignKey(User,
                                    related_name="verified_by",
                                    on_delete=models.SET_NULL,
                                    editable=True,
                                    null=True,
                                    blank=True)

    def tag_text(self):
        tag_objects = self.tags.all()
        tag_names = [x.text for x in tag_objects]

        if len(tag_names) > 0:
            return ','.join(tag_names)

        return ''

    def get_text_words(self) -> List[str]:
        return self.text.split()

    def get_title(self):
        return ' '.join(self.get_text_words()[:8])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.get_title())

        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_title()


class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 editable=True)
    text = models.TextField()

    is_correct = models.BooleanField()
    is_active = models.BooleanField(default=True)

    def get_text_words(self) -> List[str]:
        return self.text.split()

    def get_title(self):
        return ' '.join(self.get_text_words()[:8])

    def __str__(self):
        return self.get_title()
