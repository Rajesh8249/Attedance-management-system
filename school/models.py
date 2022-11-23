from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
from django.contrib.auth.models import PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self, email,username,password=None):
        if username is None:
            raise TypeError('users should a username')
        if email is None:
            raise TypeError('users should have a email')
        # print("AAAAAAAA",password)
        user = self.model(username=username,email=self.normalize_email(email),
                        password=password)
        user.set_password(password)
        user.is_verified = True
        # print("AAAAAAAA",user.__dict__)
        user.save()
        return user

    def create_superuser(self,username,email,password=None):
        # if password is None:
        user = self.create_user(email,username,password)
        user.is_superuser = True
        user.is_staff = True
        
        user.is_verified = True
        user.save()
        # print("ZZZZZZZ",user)
        return user




class User(AbstractBaseUser,PermissionsMixin):
    ROLES = (
        ('','No Role is Selected'),
        ('parent','Parents'),
        ('student','Students')
    )
    username = models.CharField('username', max_length=255)
    role = models.CharField(choices=ROLES,max_length=30,blank=True,null=True)  
    email = models.EmailField('email address', unique=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default= False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class subjects(models.Model):
    
    subject_id = models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)

    def __str__(self):
        return self.subject_name

class standard(models.Model):
    standard_name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(subjects, related_name='subjects')
   
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.standard_name



class Students(models.Model):
    parent = models.OneToOneField(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    student_name = models.CharField(max_length=200)
    student_rollno = models.IntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=255)
    standard_id=models.ForeignKey(standard,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name




class Attedance(models.Model):
    attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)
    student_name = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    subject_id=models.ForeignKey(subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField()
    # attedance_list = models.OneToManyField(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=8, choices=attendance_choices, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(str(self.student_name.student_name) +"-"+ str(self.attendance_date))

    class Meta:
        unique_together = ('student_name', 'subject_id','attendance_date')







