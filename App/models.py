from django.db import models

# Create your models here.

class Book4(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    publication_date2 = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.title,self.authors)
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    publication_date2 = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.title,self.authors)
class Book1(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    publication_date2 = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.title,self.authors)
class Book3(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    publication_date2 = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.title,self.authors)