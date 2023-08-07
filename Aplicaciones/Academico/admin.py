from django.contrib import admin
from .models import Curso, Event, Venue, MyClubUser

# Register your models here.
admin.site.register(Curso)
admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)