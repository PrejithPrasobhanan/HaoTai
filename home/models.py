from django.db import models

# Create your models here.
class Categories(models.Model):
    images = models.ImageField(upload_to='Categories')
    title = models.CharField(max_length=100)
    descreption = models.TextField()
    vaccency = models.IntegerField()

    def __str__(self):
        return self.title



class Jobsection(models.Model):
    images = models.ImageField(upload_to='Jobsection')
    title = models.CharField(max_length=200)
    descreption = models.TextField()
    vaccency = models.IntegerField()
    experience = models.TextField()
    document = models.TextField()
    skill = models.TextField()
    language = models.TextField()
    salary = models.TextField()
    age = models.TextField()
    Categories = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title
