from django.db import models


class operation(models.Model):
    firstname = models.CharField(max_length=50,)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=50,choices=(('tech', 'Tech'),
        ('mplab', 'Mplab'),
        ('acadmey', 'Acadmey')),default='DEFAULT VALUE')

    operations = models.CharField(max_length=50,choices=(('hall', 'Hall'),
        ('utensils', 'Utensils')),default='DEFAULT VALUE')

    def __str__(self):
        return self.firstname

class leave(models.Model):
    firstname = models.CharField(max_length=50,)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=50,choices=(('tech', 'Tech'),
        ('mplab', 'Mplab'),
        ('acadmey', 'Acadmey')),default='DEFAULT VALUE')

    leavetype = models.CharField(max_length=50,choices=(('fullday', 'Fullday'),
        ('halfday', 'Halfday')),default='DEFAULT VALUE')

    supervisoremail = models.EmailField()
    teamleademail = models.EmailField()
    numberofdays = models.DateTimeField()

    def __str__(self):
        return self.firstname


class snacks(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=50,choices=(('tech', 'Tech'),
        ('mplab', 'Mplab'),
        ('acadmey', 'Acadmey')),default='DEFAULT VALUE')
    drinks = models.CharField(max_length=50,choices=(('tea', 'Tea'),
        ('coffee', 'Coffee')),default='DEFAULT VALUE')
    sugar = models.CharField(max_length=50,choices=(('sugar', 'Sugar'),
        ('nosugar', 'Nosugar')),default='DEFAULT VALUE')


    def __str__(self):
        return self.firstname


class booking(models.Model):
    firstname = models.CharField(max_length=50,)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=50,choices=(('tech', 'Tech'),
        ('mplab', 'Mplab'),
        ('acadmey', 'Acadmey')),default='DEFAULT VALUE')
    mettingroom = models.CharField(max_length=50,choices=(('t0', 'T0'),
        ('a0', 'A1'),('a1','A1')),default='DEFAULT VALUE')

    def __str__(self):
        return self.firstname