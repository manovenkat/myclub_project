from django.db import models
# this is a comment

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Postal Code', max_length=20)
    phone = models.CharField('contact phone', max_length=20)
    web = models.URLField('web address')
    email_address = models.EmailField('Email address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField('Manager Name', max_length=60)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    description = models.TextField('Event Description', blank=True)

    def __str__(self):
        return self.name

# class Event(models.Model):
#     name = models.CharField('Event Name', max_length=120)
#     event_date = models.DateTimeField('Event Date')
#     venue = models.CharField(max_length=120)
#     manager = models.CharField('Manager Name', max_length=60)
#     description = models.TextField('Event Description', blank=True)
#
#     def __str__(self):
#         return self.name

