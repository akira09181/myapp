from django.db import models

# Create your models here.
class Article(models.Model):
    content=models.CharField(max_length=200)
    user_name = models.CharField(max_length=200,null =True)

    def __str__(self):
        return self.content

class Question(models.Model):
    quesion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
