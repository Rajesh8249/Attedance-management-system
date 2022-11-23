from rest_framework.response import Response
from school.models import *
from school.serializers import UserSerializer,subjectserializer,standardserializer,studentserializer,Attedancesserializer
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from.permissions import IsAdminUser_ForAdmin
from rest_framework.permissions import  AllowAny



# class ActionBasedPermission(AllowAny):
#     """
#     Grant or deny access to a view, based on a mapping in view.action_permissions
#     """
#     def has_permission(self, request, view):
#         for klass, actions in getattr(view, 'action_permissions', {}).items():
#             if view.action in actions:
#                 return klass().has_permission(request, view)
#         return False

class UserViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    

    serializer_class = UserSerializer
    queryset = User.objects.all()

class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False

class subjectsViewset(viewsets.ViewSet):
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAdminUser_ForAdmin: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['list','retrieve']
    }
    def list(self,request,pk=None):
        queryset = subjects.objects.all()
        serializer = subjectserializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = subjects.objects.all()
        serializer = subjectserializer(get_object_or_404(queryset, pk=pk))
        return Response(serializer.data)


    def create(self,request):
        serializer = subjectserializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk=None):
        subject = get_object_or_404(subjects.objects.all(), pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False



class standardViewset(viewsets.ViewSet):
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAdminUser_ForAdmin: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['list','retrieve']
    }



    def list(self,request):
        queryset = standard.objects.all()
        serializer = standardserializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = standard.objects.all()
        serializer = standardserializer(get_object_or_404(queryset, pk=pk))
        return Response(serializer.data)


    def create(self,request):
        serializer = standardserializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None):
    #     standard = get_object_or_404(standard.objects.all(), pk=pk)
    #     serializer = standardserializer(data=request.data) 
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        

    def partial_update(self, request,pk, *args, **kwargs):
        instance = standard.objects.get(pk=pk)
        serializer =standardserializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self,request,pk=None):
        standard = get_object_or_404(subjects.objects.all(), pk=pk)
        standard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False

class  StudentsViewset(viewsets.ViewSet):
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAdminUser_ForAdmin: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['list','retrieve']
    }


    def list(self,request):
        queryset = Students.objects.all()
        serializer = studentserializer(queryset, many=True)
        return Response(serializer.data)

        
    def retrieve(self, request, pk=None):
        queryset = Students.objects.all()
        serializer =studentserializer(get_object_or_404(queryset, pk=pk))
        return Response(serializer.data)
    

    def create(self,request):
        serializer = studentserializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request,pk, *args, **kwargs):
        instance = Students.objects.get(pk=pk)
        serializer =studentserializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self,request,pk=None):
        Students = get_object_or_404(subjects.objects.all(), pk=pk)
        Students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework.permissions import IsAdminUser
# class IsAdminUser_ForAdmin(BasePermission):
#     def has_permission(self, request,view):
#         # import pdb;pdb.set_trace()
#         return bool(
#             request.user and request.user.is_staff and request.user.is_superuser
        # )
from django.core.mail import EmailMessage
class  AttedanceViewset(viewsets.ViewSet):
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAdminUser_ForAdmin: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['list','retrieve']
    }

    def list(self,request):
        print(request.user)
        queryset = Attedance.objects.all()
        serializer = Attedancesserializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request,pk, *args, **kwargs):
        instance = Attedance.objects.get(pk=pk)
        serializer =Attedancesserializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if request.data['status'] == "present":
            return Response(serializer.data)
        else:
            # here i will send SMS if student is absent
            # import pdb;pdb.set_trace()
            email = EmailMessage(
                subject='Student Absent Message',
                body=f"Hi your scholar is absent in this subject",
                to=[instance.student_name.parent.email]
            )
            email.send()


            return Response(serializer.data)
         

        
    def retrieve(self, request, pk=None):
        queryset = Attedance.objects.all()
        serializer =Attedancesserializer(get_object_or_404(queryset, pk=pk))
        return Response(serializer.data)
