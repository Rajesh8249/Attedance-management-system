# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *
from datetime import date
 
 
# @receiver(post_save, sender=Students)
# def create_profile(sender, instance, created, **kwargs):
#         import pdb;pdb.set_trace()
  
@receiver(post_save, sender=Students)
def save_profile(sender, instance, **kwargs):

    if instance.standard_id.subjects.all().count():
        for i in instance.standard_id.subjects.all():
            Attedance.objects.create(student_name=instance,
                            subject_id=i,
                            attendance_date = date.today()
            )
  