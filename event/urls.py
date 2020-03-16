from django.urls import path
from . import views

urlpatterns = [
      path('',views.Event,name='Event'),
      path('event_details',views.event_details,name='event_details'),
      path('Admissions',views.Admissions,name='Admissions'),
      path('Courses',views.courses,name='Courses')

]
