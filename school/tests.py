

# Create your tests here.


from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


class RegisterTestCase(APITestCase):
    def test_Register(self):
        data = {
            "email":"testcase@example.com",
            "username":"testcase",
            "password":"testcase"
            
        }
       
        response= self.client.post(reverse('user-list'),data)
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class  subjectsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="testcase",password="password@123",email="testcase@example.com")
        token = self.client.post(path=reverse('token_obtain_pair'),data={"username":self.user.username,
                                                                        "email":self.user.email,
                                                                        "password":"password@123"})

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")

        self.subject = subjects.objects.create(subject_id ="1",subject_name="math")
        self.sub_data = {
            "subject_id": "1",
            "subject_name": "math"
        }

          
    def test_subject_craeate(self):


        # import pdb;pdb.set_trace()
        response = self.client.post(reverse('subjectsViewset-list'),self.sub_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_subject_list(self):
        response = self.client.get(reverse('subjectsViewset-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_subject_delete(self):
        response = self.client.delete(reverse('subjectsViewset-detail',kwargs={'pk':1}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_subject_ind(self):
      
        response = self.client.get(reverse('subjectsViewset-detail', kwargs={'pk':self.sub_data['subject_id']}))
        # import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class standardTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="testcase",password="password@123",email="testcase@example.com")
        token = self.client.post(path=reverse('token_obtain_pair'),data={"username":self.user.username,
                                                                        "email":self.user.email,
                                                                        "password":"password@123"})

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")

        self.subject = subjects.objects.create(subject_id ="1",subject_name="math")
        self.standard = standard.objects.create(standard_name="1st")
        self.standard.subjects.set([1])
        self.standard.save()
        self.data = {
            "standard_name": "1st",
            "subject_name": "math"
        }

    def test_standard_create(self):
        data = {
            "standard_name": "1st",
            "subject_name": "math"
        }

        response = self.client.post(reverse('standardViewset-list'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_standard_list(self):

        response = self.client.get(reverse('standardViewset-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_standard_delete(self):
        response = self.client.delete(reverse('standardViewset-detail',kwargs={'pk':1}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    
    def test_standard_ind(self):

      
        response = self.client.get(reverse('standardViewset-detail', kwargs={'pk':self.standard.id}))
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    
    def test_standard_update(self):
        # import pdb; pdb.set_trace()
      
        response = self.client.patch(reverse('standardViewset-detail', kwargs={'pk':self.standard.id}))
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class  StudentsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="testcase",password="password@123",email="testcase@example.com")

        token = self.client.post(path=reverse('token_obtain_pair'),data={"username":self.user.username,
                                                                        "email":self.user.email,
                                                                        "password":"password@123"})

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")

        self.subject = subjects.objects.create(subject_id ="1",subject_name="math")
        self.standard = standard.objects.create(standard_name="1st")
 
        self.parent = User.objects.create_user(username="testcaseparent",password="password@123",email="testcaseparent@example.com")
        self.parent.role="parent"
        self.parent.save()

    
    def test_Students_create(self):
        data={
            "parent":self.parent.id,
            "student_name":"test12",
            "student_rollno":"1",
            "address":"abcdef", 
            "gender":"male",
            "standard_id":self.standard.id
             }

        response = self.client.post(reverse('studentViewset-list'),data)
        # import pdb;pdb.set_trace()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    
    def test_Students_list(self):

        response = self.client.get(reverse('studentViewset-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_Students_delete(self):
        response = self.client.delete(reverse('studentViewset-detail',kwargs={'pk':1}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

     
    def test_Students_ind(self):
        # import pdb; pdb.set_trace()

        data={
            "parent":self.parent,
            "student_name":"testdd12",
            "student_rollno":"12",
            "address":"abcdef", 
            "gender":"male",
            "standard_id":self.standard
             }
        student = Students.objects.create(**data)
        # print("ZZZZZZ",student)
        response = self.client.get(reverse('studentViewset-detail', kwargs={'pk':student.id}))
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_student_update(self):

        data={
            "parent":self.parent,
            "student_name":"testdd12",
            "student_rollno":"12",
            "address":"abcdef", 
            "gender":"male",
            "standard_id":self.standard
             }
        student = Students.objects.create(**data)

      
        response = self.client.patch(reverse('studentViewset-detail', kwargs={'pk':1}))
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)    


class  AttedanceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="testcase",password="password@123",email="testcase@example.com")

        token = self.client.post(path=reverse('token_obtain_pair'),data={"username":self.user.username,
                                                                        "email":self.user.email,
                                                                        "password":"password@123"})

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")

        self.subject = subjects.objects.create(subject_id ="1",subject_name="math")
        self.standard = standard.objects.create(standard_name="1st")
        self.parent = User.objects.create_user(username="testcaseparent",password="password@123",email="testcaseparent@example.com")
   

        data={
            "parent":self.parent,
            "student_name":"testdd12",
            "student_rollno":"12",
            "address":"abcdef", 
            "gender":"male",
            "standard_id":self.standard
             }
        self.student = Students.objects.create(**data)

        self.attedance = Attedance.objects.create( student_name=self.student,subject_id=self.subject,attendance_date="2022-1-10",status="absent" )
        self.attedance.save()

    def test_attedance_create(self):
        data = {
            "student_name":self.student.id,
            "attendance_date":"2022-1-10",
            "status":"absent",
            "subject_id":self.subject.subject_id,
        }

        response = self.client.patch(reverse('AttedanceViewset-detail',kwargs={"pk":self.attedance.id}),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    
    
    def test_attedance_list(self):

        response = self.client.get(reverse('AttedanceViewset-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    
    def test_attedance_ind(self):
        data = {
            "student_name":self.student.id,
            "attendance_date":"2022-1-10",
            "status":"absent",
            "subject_id":self.subject.subject_id,
            }
              
        response = self.client.get(reverse('AttedanceViewset-detail', kwargs={'pk':self.attedance.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)