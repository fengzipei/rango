from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    qq_number = models.CharField(max_length=50, null=True, blank=True)
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
    computer_type_categories = (
        ('pc', 'pc'),
        ('laptop', 'laptop'),
    )
    computer_type = models.CharField(max_length=50, choices=computer_type_categories,
                                     default=computer_type_categories[0])
    computer_model = models.CharField(max_length=50, blank=True, null=True)
    computer_age_categories = (
        ('< 1 year', '< 1 year'),
        ('1 ~ 2 years', '1 ~ 2 year'),
        ('> 2 years', '> 2 year'),
        ('I don\'t know', 'I don\'t know'),
    )
    computer_age = models.CharField(max_length=50, choices=computer_age_categories, default=computer_age_categories[0])
    computer_os_categories = (
        ('Windows 10', 'Windows 10'),
        ('Windows 8', 'Windows 8'),
        ('Windows 7', 'Windows 7'),
        ('Windows xp', 'Windows xp'),
        ('Linux', 'Linux'),
        ('Mac OS X', 'Mac OS X'),
        ('I\'m not sure.', 'I\'m not sure.'),
    )
    computer_os = models.CharField(max_length=50, choices=computer_os_categories, default=computer_os_categories[0])
    os_bits_categories = (
        ('64', '64'),
        ('32', '32'),
        ('I\'m not sure.', 'I\'m not sure.'),
    )
    os_bits = models.CharField(max_length=50, choices=os_bits_categories, default=os_bits_categories[0])
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
    advice_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000)
    create_time = models.DateTimeField('date created', default=timezone.now)
    suggester_id = models.ForeignKey(User, on_delete=models.CASCADE)
    advice_status = (
        ('waiting for review', 'waiting for review'),
        ('reviewed', 'reviewed'),
    )
    status = models.CharField(max_length=50, choices=advice_status, default=advice_status[0])
    comment = models.CharField(max_length=500, blank=True, null=True)
    reviewer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advice_reviewer_id', blank=True,
                                    null=True)
    review_time = models.DateTimeField('date reviewed', blank=True, null=True)

    def __str__(self):
        return str(self.id) + " " + self.content[:10]


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='newbie_id')
    create_time = models.DateTimeField('data created', default=timezone.now)
    reason = models.CharField(max_length=500)
    reviewer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application_reviewer_id', blank=True,
                                    null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    review_time = models.DateTimeField('date reviewed', blank=True, null=True)
    application_status = (
        ('waiting for review', 'waiting for review'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    )
    status = models.CharField(max_length=50, choices=application_status, default=application_status[0])

    def __str__(self):
        return str(self.application_id) + " " + str(self.applicant_id.id) + " " + str(self.applicant_id.username)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publish_time = models.DateTimeField('data published', default=timezone.now)
    publisher_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher_id')
    content = models.CharField(max_length=1500)

    def __str__(self):
        return str(self.id) + " " + self.title
