from django.db import models


# Create your models here.


class News(models.Model):
    news_pic = models.ImageField(null=True, default='')
    news_title = models.CharField(max_length=200)
    news_content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.news_title


class Teachers(models.Model):
    teacher_pic = models.ImageField(null=True, default='')
    teacher_name = models.CharField(null=True, max_length=200)
    teacher_title = models.CharField(max_length=200)
    date_join = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_join']

    def __str__(self):
        return self.teacher_name


class Parents_review(models.Model):
    parent_pic = models.ImageField(null=True, default='')
    parent_name = models.CharField(null=True, max_length=200)
    remark = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.parent_name


class Blog(models.Model):
    blog_pic = models.ImageField(null=True, default='')
    writer = models.CharField(max_length=200)
    blog_title = models.CharField(max_length=200)
    paragraph = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.blog_title
