#-*- coding=utf-8 -*-

from django.db import models

# Create your models here.

#博客标题
class BlogInfo(models.Model):
    blogTitle = models.CharField(max_length=30)
    blogSubtitle = models.CharField(max_length=30)

 #   def __str__(self):
  #      return self.blogTitle

    def __unicode__(self):
        return self.blogTitle

#文章标签
class ArticleTags(models.Model):
    tags = models.CharField(max_length=10)

    def __unicode__(self):
        return self.tags

#文章分类
class ArticleCategories(models.Model):
    categoryName = models.CharField(max_length=15)

    def __unicode__(self):
        return self.categoryName

#文章
class Article(models.Model):
    #url = models.URLField(blank=True)
    title = models.CharField(max_length=50)
    
    author = models.CharField(max_length=30)
    
    content = models.TextField()
    #多对多的标签
    articleTags = models.ManyToManyField(ArticleTags)   #django, python..
    #一对多的外键：分类
    articleCategories = models.ForeignKey(ArticleCategories)

    viewsCount = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __unicode__(self):
        return self.title


class ArticleComment(models.Model):
    commentContent = models.CharField(max_length=500)
    commentTime = models.DateTimeField()
    commentUsername = models.CharField(max_length=15)

    commentArticle = models.ForeignKey(Article)

    def __unicode__(self):
        return self.commentArticle + self.commentContent