from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    categories = (
        ('student', 'student'),
        ('super admin', 'super admin'),
        ('normal admin', 'normal admin'),
        ('repairer', 'repairer'),
        ('teacher', 'teacher')
    )
    category = models.CharField(max_length=50, choices=categories)
    score = models.IntegerField(default=0)
    address = models.CharField(max_length=100, null=True, blank=True)
    join_time = models.DateTimeField('date joined', default=timezone.now)
    exit_time = models.DateTimeField('date leave', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class RepairOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicant_id')
    problem_text = models.CharField(max_length=500)
    repairer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repairer_id', blank=True, null=True)
    create_time = models.DateTimeField('date created', default=timezone.now)
    finish_time = models.DateTimeField('date finished', blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    order_status = (
        ('waiting for repairing', 'waiting for repairing'),
        ('processing', 'processing'),
        ('finished', 'finished'),
    )
    status = models.CharField(max_length=50, choices=order_status, default=order_status[0])

    def __str__(self):
        return str(self.order_id) + " " + str(self.applicant_id.id) + " " + str(self.applicant_id.username)


class Advice(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000)
    create_time = models.DateTimeField('date created', default=timezone.now)
    suggester_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.content[:10]


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='newbie_id')
    create_time = models.DateTimeField('data created', default=timezone.now)
    reason = models.CharField(max_length=500)
    auditor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auditor_id', blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    audit_time = models.DateTimeField('date audited', blank=True, null=True)

    def __str__(self):
        return str(self.application_id) + " " + str(self.applicant_id.id) + " " + str(self.applicant_id.name)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publish_time = models.DateTimeField('data published', default=timezone.now)
    pubisher_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher_id')
    content = models.CharField(max_length=1500)

    def __str__(self):
        return str(self.id) + " " + self.title
