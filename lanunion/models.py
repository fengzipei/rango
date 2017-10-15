from django.db import models


# Create your models here.


class Staff(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    categories = (
        ('student', 'student'),
        ('super admin', 'super admin'),
        ('normal admin', 'normal admin'),
        ('repairer', 'repairer'),
        ('teacher', 'teacher')
    )
    category = models.CharField(max_length=50, choices=categories)
    score = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    join_time = models.DateTimeField('date joined')
    exit_time = models.DateTimeField('date leave', null=True, blank=True)

    def __str__(self):
        return self.id


class RepairOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='applicant_id')
    problem_text = models.CharField(max_length=500)
    repairer_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='repairer_id', blank=True, null=True)
    start_time = models.DateTimeField('date created')
    end_time = models.DateTimeField('date finished', blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.order_id)


class Advices(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000)
    create_time = models.DateTimeField('date created')
    suggester_id = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='newbie_id')
    application_time = models.DateTimeField('data created')
    reason = models.CharField(max_length=500)
    auditor_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='auditor_id', blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    audit_time = models.DateTimeField('date audited', blank=True, null=True)

    def __str__(self):
        return str(self.applicant_id)
