from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question.question_text+" >> "+self.choise_text

class Dashboard(models.Model):
    wom = models.CharField(max_length=6,verbose_name="Main WIP",unique=True)
    customer = models.CharField(max_length=30,default="",verbose_name="Customer")
    contract_value = models.FloatField(default=0,verbose_name="Total Contract")
    paid_by_customer = models.FloatField(default=0,verbose_name="Paid by Customer")
    unpaid_by_customer = models.FloatField(default=0,verbose_name="Customer Debt")
    cost_paid = models.FloatField(default=0,verbose_name="Cost Paid")
    cost_to_finish = models.FloatField(default=0,verbose_name="Cost To Finish")
    deadline = models.DateField(default=None,null=True,verbose_name="Deadline")
    finish_estimation = models.DateField(default=None,null=True,verbose_name="Finish Estimation")
    invoice_sent = models.DateField(default=None,null=True,verbose_name="Invoice Date")
    invoice_sent_days = models.FloatField(default=0,verbose_name="days to collect") 
    pic = models.CharField(max_length=30,default="")
    note = models.CharField(max_length=250,default="")

    


# Create your models here.
