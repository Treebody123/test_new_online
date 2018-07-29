from django.db import models




class NOCQE(models.Model):
    qm_num = models.CharField(max_length=16,default=None)
    rep_date = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now_add=True)
    ticket_num = models.CharField(max_length=16)
    description = models.TextField(blank=False)
    recurring_status = models.CharField(max_length=5)
    customer_interruption = models.CharField(max_length=5)
    level = models.CharField(max_length=5)
    assignee = models.ForeignKey("qsauth.User",on_delete=models.SET_NULL,null=True)
    acknowledge_status = models.CharField(max_length=5)
    email_send = models.BooleanField(default=False)
    finding_final_status = models.CharField(max_length=5)

class NOC_Measurement(models.Model):
    content = models.TextField()
    author = models.ForeignKey('qsauth.User', on_delete=models.CASCADE)
    qe = models.ForeignKey("NOCQE", on_delete=models.CASCADE, related_name='noc_measurement')

class NOC_Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey('qsauth.User', on_delete=models.CASCADE)
    qe = models.ForeignKey("NOCQE", on_delete=models.CASCADE, related_name='noc_comment')