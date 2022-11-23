from django.urls import path,include
from rest_framework.routers import DefaultRouter
from school.views import UserViewset,subjectsViewset,standardViewset, StudentsViewset, AttedanceViewset
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView




router = DefaultRouter()
router.register('User',UserViewset,basename="user"),
router.register('subjects',subjectsViewset,basename="subjectsViewset"),
router.register('standard',standardViewset,basename="standardViewset"),
router.register('Students',StudentsViewset,basename="studentViewset"),
router.register('Attedance', AttedanceViewset,basename="AttedanceViewset")

urlpatterns = [
    path('',include(router.urls)),

        path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    

]