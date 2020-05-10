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


class Inout(models.Model):
    creterion_sell = models.IntegerField(default=0,verbose_name="売る基準")
    creterion_buy = models.IntegerField(default=0,verbose_name="買う基準")
    interval = models.IntegerField(default=0,verbose_name="投資間隔")
    volume = models.IntegerField(default=0,verbose_name="一回で買う量")

class Calc(models.Model):
    max_stock=models.IntegerField(default=0)
    max_usd=models.IntegerField(default=0)
    gains=models.IntegerField(default=0)