"""enrollment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.authtoken import views as token_view
from django.conf import settings
from django.conf.urls.static import static
# from graphene_django.views import GraphQLView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Viewset routes
router = routers.DefaultRouter()
router.register('subjects', views.SubjectViewSet)
router.register('majors', views.MajorViewSet)
router.register('ays', views.AyViewSet)
router.register('courses', views.CourseViewSet)
router.register('subjectsenrolled', views.SubjectEnrollViewSet)
router.register('instructors', views.InstructorViewSet)
router.register('enrolls', views.EnrollStudViewSet)
router.register('students', views.StudentViewSet)
router.register('yearlevels', views.YearLevelViewSet)
router.register('ids', views.IdAndFullnameViewSet)
router.register('curriculums', views.CurriculumViewSet)
router.register('curriculumss', views.CurriculumsViewSet)
router.register('aosfs', views.AOSFViewSet)
router.register('instructorloads', views.InstructorLoadSubjectViewSet)
router.register('instructorloads-read', views.InstructorLoadSubjectWithObjectViewSet)
router.register('rooms', views.RoomViewSet)
router.register('times', views.TimeSchedViewSet)
router.register('days', views.DaySchedViewSet)
router.register('studentusers', views.StudentUserViewSet)
router.register('createuser', views.CreateUserView)

# Url Patterns
urlpatterns = [
    # path('graphql', GraphQLView.as_view(graphiql=True)),
    path('', include(router.urls)),
    path('IntructorLoadedSubjectByClassList/<sem>/<ay>/<course>/<major>/<section>/<year_level>',views.IntructorLoadedSubjectByClassList.as_view(),name='IntructorLoadedSubjectByClassList'),
    path('IntructorLoadedSubjectList/<sem>/<ay>/<instructor>',views.IntructorLoadedSubjectList.as_view(),name='IntructorLoadedSubjectList'),
    path('searchenrolllist/<id>/<course>/<major>/<sem>/<year>/<ay>',views.SearchEnroll.as_view(),name='searchenrolllist'),
    path('addsubjectbycuriculumAPI/<int:pk>/',views.add_subject_by_curiculum_api,name='addsubjectbycuriculumAPI'),
    path('Apiaddsubjectbycuriculum/<course>/<major>/<sem>/<year>',views.SubjectbyCurriculum.as_view(),name='Apiaddsubjectbycuriculum'),
    path('getSubjectsByCurriculumAPI/<int:course>/<sem>',views.get_subjects_by_curriculum_api,name='getSubjectsByCurriculumAPI'),
    path('getSubjectsByCurriculumAPI/',views.get_subjects_by_curriculum_api_all,name='getSubjectsByCurriculumAPIAll'),
    path('Api/students/enroll/<int:pk>/status',views.update_status_api,name='enroll-status-api'),
    path('Api/students/enroll/<int:pk>/return',views.return_for_correction_api,name='enroll-return-api'),
    path('Api/students/enroll/<int:pk>/forward',views.forward_for_approval_api,name='enroll-forward-api'),
    path('Api/displayAllEnrollAPI',views.display_all_enroll_api,name='displayAllEnrollAPI'),
    path('Api/<int:pk>/enroll/', views.enroll_stud_api,name='enroll-api'),
    path('Api/<int:pk>/enroll/subjects/add/', views.add_subject_load_api,name='subjectLoad-api'),
    path('Api/enroll/subjects/update/', views.update_subject_load_api,name='subjectLoad-update-api'),
    # path('Api/uploadSubjectsAPI/',views.upload_subjects_api,name='uploadSubjectsAPI'),
    path('Api/<int:pk>/enroll/subjects/delete/',views.delete_subject_loaded,name='delete-enroll-subject'),
    path('Api/<int:pk>/enroll/subjects/drop/',views.drop_subject_loaded,name='drop-enroll-subject'),
    path('Api/<int:pk>/enroll/subjects/enroll/',views.enroll_drop_subject_loaded,name='enroll-drop-enroll-subject'),
    path('Api/enrollStudent/all/',views.StudentEnrollList.as_view(),name='student-enroll-api'),
    path('Api/enrollStudent/<ay>/<course>/<sem>/',views.ByCourseStudentEnrollList.as_view()),
    path('Api/subjectloaded/<sub>/<major>/<ay>/<course>/<sem>',views.SubjectLoadedList.as_view(),name="subjects_loadedapi"),
    path('Api/enrollbystudsub/<student>/<ay>/<sem>',views.SubjectByStudentList.as_view(),name="enrollbystudsub"),
    path('Api/allEnrollbySemAyCourse/<ay>/<sem>/<course>/<year>/<major>',views.AllStudentEnrollBySYAndSEM.as_view(),name="allEmrollbySemAy"),
    path('getIdAndFullname/<student_id>',views.GetStudentIdAnfFullnameList.as_view(),name="getStudentId"),
    path('subjects', views.SubjectsList.as_view(), name = ''),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/user/', views.get_user_from_token, name='token_user'),
    path('getstudentbyid/<studentid>', views.get_student_by_id, name='get_student_by_id'),
    path('enrollStudentbystudent/<id>/',views.SearchEnrollByStudent.as_view(),name='enrollStudentbystudent'),
    path('api-token-auth/', views.CustomAuthToken.as_view())
 
]
