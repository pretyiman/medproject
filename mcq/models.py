from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    name    = models.CharField(max_length=250,unique=True)
    def __str__(self):
        return "%s" % (self.name)

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name  = models.CharField(max_length=250)


    def __str__(self):
        return "%s" % (self.name)

class Question(models.Model):
    subject    = models.ForeignKey(Subject, on_delete=models.PROTECT)
    topic       = models.ForeignKey(Topic, on_delete=models.PROTECT)
    desciption  = models.TextField(max_length=700, null=False)


    def __str__(self):
        return "%s %s %s" % (self.desciption[:100],self.topic,self.subject)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option  = models.CharField(max_length=100)
    is_true  = models.BooleanField(default=False)
    explaination = models.TextField(max_length=500, null=True ,blank=True)

    def __str__(self):
        return "%s" % (self.option)

class Quiz(models.Model):
    title = models.CharField(max_length=60, blank=False)
    description = models.TextField(blank=True, help_text=("a description of the quiz"))
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.PROTECT)
    quesions = models.ManyToManyField(Question)

    def __str__(self):
        return "%s" % (self.title)

class PublicMcq(models.Model):
     subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
     topic    = models.ForeignKey(Topic, on_delete=models.PROTECT)
     post_date=models.DateTimeField(auto_now_add=True)
     question = models.TextField(max_length=700,null=False)
     option_a  = models.CharField(max_length=100,null=False)
     a_is_true = models.BooleanField(default=False)
     option_b = models.CharField(max_length=100, null=False)
     b_is_true = models.BooleanField(default=False)
     option_c  = models.CharField(max_length=100,null=False)
     c_is_true = models.BooleanField(default=False)
     option_d = models.CharField(max_length=100, null=False)
     d_is_true = models.BooleanField(default=False)
     
     def __str__(self):
            return "%s" % (self.question)

     

class PublicAnswers(models.Model):
    question = models.ForeignKey(PublicMcq, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    is_true = models.BooleanField(default=False)
    explaination = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.option)