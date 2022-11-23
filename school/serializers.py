from rest_framework import serializers
from school.models import  *
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(
            password = validated_data['password'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        return validated_data

    def validate(self, data):
        user = User.objects.filter(email=data['email']).exists()
        if user:
            raise serializers.ValidationError("This Email alredy exists")

        return data

    def update(self, instance, validated_data):
        if 'username' in validated_data:
            instance.user.password = make_password(
                validated_data.get('username').get('password', instance.user.password)
            )
            instance.user.save()

    class Meta:
         model = User
         fields =  ('username', 'email','password')




class  subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = '__all__'


class standardserializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(queryset=subjects.objects.all(), many=True)
    class Meta:
        model = standard
        fields = ['subjects','standard_name']

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class Attedancesserializer(serializers.ModelSerializer):
    class Meta:
        model = Attedance
        fields = '__all__'
