from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=1000)
    creditos=models.PositiveSmallIntegerField()
    class Meta:
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre,self.creditos)

class Venue(models.Model):
    name = models.CharField( 'Venue Name', max_length=120 )
    address = models.CharField( max_length=300 )
    zip_code =  models.CharField( 'Zip Code', max_length=120 )
    phone =  models.CharField( 'Contact Phone', max_length=120 )
    web = models.URLField('Web Site Adress')
    email_address = models.EmailField('Email Address')
    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name =  models.CharField( 'First Name', max_length=120 )
    last_name =  models.CharField( 'Last Name', max_length=120 )
    email = models.EmailField('Email User')
    def __str__(self):
        return self.first_name + '' + self.last_name
    

class Event(models.Model):
    name = models.CharField( 'Event Name', max_length=120 )
    venue = models.ForeignKey(Venue, blank = True, null=True,on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    manager = models.CharField( max_length=60 )
    description = models.TextField( blank= True)    
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    def __str__(self):
        return self.name