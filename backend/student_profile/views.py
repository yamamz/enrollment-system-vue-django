from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm, EnrollForm, SubjectLoadForm,CurriculumForm,UploadExcelForm,SubjectForm,IDsNameForm,StudentFormUpdate
from .mixins import AjaxFormMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models  import StudentUser, DaySched, TimeSched, Room, InstructorLoadSubject, AOSF, Instructor, EnrollbyStudent, Student,Major, Academic_year, Year_level,Course, SubjectsLoaded,Subject,Curriculum,IDandFullname
from django.conf import settings
from .serializers import UserSerializer, StudentUserSerializer, MyTokenObtainPairSerializer, InstructorLoadSubjectWithObjectSerializer, RoomSerializer, DaySchedSerializer, TimeSchedSerializer, InstructorLoadSubjectSerializer, AOSFSerializer, StudentsEnrollSerializer, CurriculumSerializer,CurriculumsSerializer, IDandFullnameSerializer, EnrollStudSerlizer, SubjectSerializer,InstructorSerializer, StudentEnrollSerializer, SubjectsLoadedSerializer, CourseSerializer, Academic_yearSerializer, MajorSerializer,Year_levelSerializer,StudentSerializer,SubjectEnrollSerializer
from rest_framework import generics
# import numpy as np
# import pandas as pd
from django.utils import timezone
from datetime import datetime
from django.db.models import Q
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
import json
import os
from os.path import expanduser
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
# from xhtml2pdf import pisa
# import pandas as pd
# from pandas import ExcelWriter
# from pandas import ExcelFile
# import numpy as np
# from openpyxl import load_workbook
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
User = get_user_model()

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def enroll_stud_api(request,pk):
	if request.method=='POST':
		form=EnrollForm(request.POST)
		if form.is_valid():
			student=get_object_or_404(Student,pk=pk)
			enroll_key=student.student_id+str(form.cleaned_data['academic_year'])+str(form.cleaned_data['course'])+str(form.cleaned_data['semister'])
			student_enrollKey=EnrollbyStudent.objects.filter(enrollment_key=enroll_key)
			if not student_enrollKey.exists():
				enroll=form.save(commit=False)
				enroll.student=student
				enroll.enrollment_key=enroll_key
				enroll.save()
				enrollRes={'pk': enroll.pk,'message':'enrolled successfully','is_save':True}
				return Response(enrollRes)
			else:
				enrollRes={'message':'already enrolled on this semister','is_save':False}
				return Response(enrollRes)
		return Response({'message':'invalid forms'})
	return Response({'message':'get request'})

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication,))
@permission_classes((IsAuthenticated,))
def update_status_api(request,pk):
	enroll=get_object_or_404(EnrollbyStudent,pk=pk)
	subjects=SubjectsLoaded.objects.filter(enrolled_by_student=enroll)
	if request.method=='POST':
		if subjects.exists():
			enroll.status='approved'
			enroll.date_created=datetime.now(timezone.utc)
			enroll.save()
			serialize_subjects=[]
			for subject_loaded in subjects:
				subject_loaded.status="enrolled"
				subject_loaded.save()
				subject_enroll={'pk':str(subject_loaded.pk),'subject_pk':str(subject_loaded.subject.pk),'code':subject_loaded.subject.code,
					'description':subject_loaded.subject.description,'unit':subject_loaded.subject.unit,'status':subject_loaded.status}
				serialize_subjects.append(subject_enroll)
			return Response({'message':'ok','enroll_status':'approved','subjects':serialize_subjects})
		return Response({'message':'you don\'t have subjects added'})
	return Response({'message':'get request'})

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication,))
@permission_classes((IsAuthenticated,))
def return_for_correction_api(request,pk):
	enroll=get_object_or_404(EnrollbyStudent,pk=pk)
	subjects=SubjectsLoaded.objects.filter(enrolled_by_student=enroll)
	if request.method=='POST':
		if subjects.exists():
			enroll.status='returned for correction'
			enroll.save()
			serialize_subjects=[]
			for subject_loaded in subjects:
				subject_loaded.status="returned for correction"
				subject_loaded.save()
				subject_enroll={'pk':str(subject_loaded.pk),'subject_pk':str(subject_loaded.subject.pk),'code':subject_loaded.subject.code,
					'description':subject_loaded.subject.description,'unit':subject_loaded.subject.unit,'status':subject_loaded.status}
				serialize_subjects.append(subject_enroll)
			return Response({'message':'ok','enroll_status':enroll.status,'subjects':serialize_subjects})
		return Response({'message':'you don\'t have subjects added'})
	return Response({'message':'get request'})

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication,))
@permission_classes((IsAuthenticated,))
def display_all_enroll_api(request):
	enrollees=EnrollbyStudent.objects.all()
	enroll_dic_list=[]
	for enrollee in enrollees:
		enroll_dic_list.append({'student_id':str(enrollee.student.student_id),
			'fullname': enrollee.student.first_name + " " + enrollee.student.middle_name +" "+enrollee.student.last_name,
			'course':enrollee.course.code, 'ay':enrollee.academic_year.ay,'semister':enrollee.semister,'status':enrollee.status})
	context={'enrollees':enroll_dic_list}
	return Response(context)

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication,))
@permission_classes((IsAuthenticated,))
def forward_for_approval_api(request,pk):
	enroll=get_object_or_404(EnrollbyStudent,pk=pk)
	subjects=SubjectsLoaded.objects.filter(enrolled_by_student=enroll)
	if request.method=='POST':
		if subjects.exists():
			enroll.status='forwarded'
			enroll.save()
			serialize_subjects=[]
			for subject_loaded in subjects:
				subject_loaded.status="forwarded"
				subject_loaded.save()
				subject_enroll={'pk':str(subject_loaded.pk),'subject_pk':str(subject_loaded.subject.pk),'code':subject_loaded.subject.code,
					'description':subject_loaded.subject.description,'unit':subject_loaded.subject.unit,'status':subject_loaded.status}
				serialize_subjects.append(subject_enroll)
			return Response({'is_forwarded': True,'message':'forward successfully','enroll_status':'forwarded','subjects':serialize_subjects})
		return Response({'message':'you don\'t have subjects added','is_forwarded': False})
	return Response({'message':'get request'})

class CreateUserView(CreateModelMixin, GenericViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class ByCourseStudentEnrollList(generics.ListAPIView):
	serializer_class = StudentsEnrollSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		ay_pk=self.kwargs['ay']
		course_pk=self.kwargs['course']
		sem=self.kwargs['sem']
		course=get_object_or_404(Course,pk=course_pk)
		ay=get_object_or_404(Academic_year,pk=ay_pk)
		return EnrollbyStudent.objects.select_related("student").select_related("year_level").select_related("academic_year").select_related("major").select_related("course").filter(semister=sem,course=course,academic_year=ay,status="approved")

class SubjectsList(generics.ListAPIView):
	serializer_class = SubjectSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return Subject.objects.all()

class StudentEnrollList(generics.ListAPIView):
	serializer_class = StudentEnrollSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return EnrollbyStudent.objects.select_related("student").select_related("year_level").select_related("academic_year").select_related("major").select_related("course").all()

class AllStudentEnrollBySYAndSEM(generics.ListAPIView):
	serializer_class = StudentEnrollSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		sem=self.kwargs['sem']
		ayId = self.kwargs['ay']
		coursePk = self.kwargs['course']
		yearPk = self.kwargs['year']
		majorPk = self.kwargs['major']
		ay = get_object_or_404(Academic_year,pk=ayId)
		course = get_object_or_404(Course,pk=coursePk)
		year = get_object_or_404(Year_level,pk=yearPk)
		results = []
		if majorPk != '-1':
			major = get_object_or_404(Major, pk = majorPk)
			results = EnrollbyStudent.objects.select_related("student").select_related("year_level").select_related("academic_year").select_related("major").select_related("course").filter(major = major,academic_year=ay, semister = sem, course = course, year_level= year, status ='approved').all()
			if len(results) != 0:
				return EnrollbyStudent.objects.select_related("student").select_related("year_level").select_related("academic_year").select_related("major").select_related("course").filter(major = major,academic_year=ay, semister = sem, course = course, year_level= year, status ='approved').all()
			return EnrollbyStudent.objects.select_related("student").select_related("year_level").select_related("academic_year").select_related("major").select_related("course").filter(academic_year=ay, semister = sem, course = course, year_level= year, status ='approved').all()	
		return EnrollbyStudent.objects.select_related("student").select_related("year_level").select_related("academic_year").select_related("major").select_related("course").filter(academic_year=ay, semister = sem, course = course, year_level= year, status ='approved').all()
		
class SubjectbyCurriculum(generics.ListAPIView):
	serializer_class = SubjectSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		major_pk=self.kwargs['major']
		course_pk=self.kwargs['course']
		sem=self.kwargs['sem']
		yearpk=self.kwargs['year']
		if major_pk != "0":
			year=get_object_or_404(Year_level,pk=yearpk)
			major=get_object_or_404(Major,pk=major_pk)
			course=get_object_or_404(Course,pk=course_pk)
			return  Curriculum.objects.filter(course=course,year_level=year,semister=sem,major=major).first().subjects.all()
		year=get_object_or_404(Year_level,pk=yearpk)
		course=get_object_or_404(Course,pk=course_pk)
		return Curriculum.objects.filter(course=course,year_level=year,semister=sem).first().subjects.all()

class SearchEnroll(generics.ListAPIView):
	serializer_class = EnrollStudSerlizer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		major_pk=self.kwargs['major']
		course_pk=self.kwargs['course']
		sem=self.kwargs['sem']
		year=self.kwargs['year']
		ay = self.kwargs['ay']
		student=get_object_or_404(Student,pk=self.kwargs['id'])
		if major_pk != "0":	
			major=get_object_or_404(Major,pk=major_pk)
			course=get_object_or_404(Course,pk=course_pk)
			year=get_object_or_404(Year_level,pk=year)
			academic_year = get_object_or_404(Academic_year,pk = ay)
			return EnrollbyStudent.objects.filter(academic_year = academic_year, student=student,semister=sem,course=course,year_level=year,major=major)
		course=get_object_or_404(Course,pk=course_pk)
		year=get_object_or_404(Year_level,pk=year)
		academic_year = get_object_or_404(Academic_year,pk = ay)
		return EnrollbyStudent.objects.filter(academic_year = academic_year,student=student,semister=sem,course=course,year_level=year)

class SearchEnrollByStudent(generics.ListAPIView):
	serializer_class = StudentEnrollSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		student=get_object_or_404(Student,pk=self.kwargs['id'])
		return EnrollbyStudent.objects.filter(student=student)

class SubjectLoadedList(generics.ListAPIView):
	serializer_class = SubjectEnrollSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		sub_pk=self.kwargs['sub']
		major_pk=self.kwargs['major']
		course_pk=self.kwargs['course']
		sem=self.kwargs['sem']
		ay=self.kwargs['ay']
		if major_pk != "0":
			sub=get_object_or_404(Subject,pk=sub_pk)
			major=get_object_or_404(Major,pk=major_pk)
			course=get_object_or_404(Course,pk=course_pk)
			academic_y=get_object_or_404(Academic_year,pk=ay)
			return SubjectsLoaded.objects.select_related("enrolled_by_student").filter(enrolled_by_student__course=course,enrolled_by_student__academic_year=academic_y,enrolled_by_student__semister=sem,subject=sub,enrolled_by_student__major=major,status="enrolled")
		sub=get_object_or_404(Subject,pk=sub_pk)
		course=get_object_or_404(Course,pk=course_pk)
		academic_y=get_object_or_404(Academic_year,pk=ay)
		return SubjectsLoaded.objects.select_related("enrolled_by_student").filter(enrolled_by_student__course=course,enrolled_by_student__academic_year=academic_y,enrolled_by_student__semister=sem,subject=sub,status="enrolled")

class SubjectByStudentList(generics.ListAPIView):
	serializer_class = SubjectEnrollSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		stud=self.kwargs['student']
		sem=self.kwargs['sem']
		ay=self.kwargs['ay']
		student=get_object_or_404(Student,pk=stud)
		academic_y=get_object_or_404(Academic_year,pk=ay)
		return SubjectsLoaded.objects.select_related("enrolled_by_student").filter(enrolled_by_student__student=student,enrolled_by_student__academic_year=academic_y,enrolled_by_student__semister=sem,status="enrolled")

class IntructorLoadedSubjectList(generics.ListAPIView):
	serializer_class = InstructorLoadSubjectWithObjectSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		instruc=self.kwargs['instructor']
		sem=self.kwargs['sem']
		ay=self.kwargs['ay']
		instructor=get_object_or_404(Instructor,pk=instruc)
		academic_y=get_object_or_404(Academic_year,pk=ay)
		return InstructorLoadSubject.objects.filter(instructor=instructor,academic_year=academic_y,semister=sem)

class IntructorLoadedSubjectByClassList(generics.ListAPIView):
	serializer_class = InstructorLoadSubjectWithObjectSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		course_pk=self.kwargs['course']
		sem=self.kwargs['sem']
		ay=self.kwargs['ay']
		section = self.kwargs['section']
		major_pk = self.kwargs['major']
		year_level_pk = self.kwargs['year_level']
		year_level = get_object_or_404(Year_level,pk=year_level_pk)
		course=get_object_or_404(Course,pk=course_pk)
		academic_y=get_object_or_404(Academic_year,pk=ay)
		if major_pk == '-1':
			return InstructorLoadSubject.objects.filter(course=course,academic_year=academic_y,semister=sem, section=section, year_level = year_level)
		major = get_object_or_404(Major,pk=major_pk)
		return InstructorLoadSubject.objects.filter(course=course,academic_year=academic_y,semister=sem, section=section, year_level = year_level, major=major)

class GetStudentIdAnfFullnameList(generics.ListAPIView):
	serializer_class = IDandFullnameSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		student_id=self.kwargs['student_id']
		return IDandFullname.objects.filter(student_id=student_id)

class EnrollStudViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	serializer_class = EnrollStudSerlizer
	queryset = EnrollbyStudent.objects.all()

class IdAndFullnameViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = IDandFullname.objects.all()
	serializer_class = IDandFullnameSerializer

class CurriculumViewSet(viewsets.ModelViewSet):
	queryset = Curriculum.objects.all()
	serializer_class = CurriculumSerializer
	permission_classes = (IsAuthenticated,)

class CurriculumsViewSet(viewsets.ModelViewSet):
	queryset = Curriculum.objects.all()
	serializer_class = CurriculumsSerializer
	permission_classes = (IsAuthenticated,)

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	permission_classes = (IsAuthenticated,)

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.select_related("course").select_related("major").all()
	serializer_class = StudentSerializer
	permission_classes = (IsAuthenticated,)

class MajorViewSet(viewsets.ModelViewSet):
	queryset = Major.objects.all()
	serializer_class = MajorSerializer
	permission_classes = (IsAuthenticated,)

class AyViewSet(viewsets.ModelViewSet):
	queryset = Academic_year.objects.all()
	serializer_class = Academic_yearSerializer
	permission_classes = (IsAuthenticated,)

class InstructorViewSet(viewsets.ModelViewSet):
	queryset = Instructor.objects.all()
	serializer_class = InstructorSerializer
	permission_classes = (IsAuthenticated,)

class SubjectEnrollViewSet(viewsets.ModelViewSet):
	queryset = SubjectsLoaded.objects.all()
	serializer_class = SubjectsLoadedSerializer
	permission_classes = (IsAuthenticated,)

class StudentUserViewSet(viewsets.ModelViewSet):
	queryset = StudentUser.objects.all()
	serializer_class = StudentUserSerializer
	permission_classes = (IsAuthenticated,)

class YearLevelViewSet(viewsets.ModelViewSet):
	queryset = Year_level.objects.all()
	serializer_class = Year_levelSerializer
	permission_classes = (IsAuthenticated,)

class AOSFViewSet(viewsets.ModelViewSet):
	queryset = AOSF.objects.all()
	serializer_class = AOSFSerializer
	permission_classes = (IsAuthenticated,)

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = (IsAuthenticated,)

class RoomViewSet(viewsets.ModelViewSet):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer
	permission_classes = (IsAuthenticated,)

class DaySchedViewSet(viewsets.ModelViewSet):
	queryset = DaySched.objects.all()
	serializer_class = DaySchedSerializer
	permission_classes = (IsAuthenticated,)

class TimeSchedViewSet(viewsets.ModelViewSet):
	queryset = TimeSched.objects.all()
	serializer_class = TimeSchedSerializer
	permission_classes = (IsAuthenticated,)

class InstructorLoadSubjectViewSet(viewsets.ModelViewSet):
	queryset = InstructorLoadSubject.objects.all()
	serializer_class = InstructorLoadSubjectSerializer
	permission_classes = (IsAuthenticated,)

class InstructorLoadSubjectWithObjectViewSet(viewsets.ModelViewSet):
	queryset = InstructorLoadSubject.objects.all()
	serializer_class = InstructorLoadSubjectWithObjectSerializer
	permission_classes = (IsAuthenticated,)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication,))
@permission_classes((IsAuthenticated,))
def add_subject_load_api(request,pk):
	enrollbyStud=get_object_or_404(EnrollbyStudent,pk=pk)
	enroll_subject=SubjectsLoaded.objects.filter(enrolled_by_student=enrollbyStud)
	if request.method == 'POST':
		form=SubjectLoadForm(request.POST)
		if form.is_valid():
			addSubject=form.save(commit=False)
			duplicate_subject=enroll_subject.filter(subject=addSubject.subject)
			if not duplicate_subject.exists():
				addSubject.enrolled_by_student=enrollbyStud
				addSubject.status="draft"
				addSubject.save()
				context={
						'pk':str(addSubject.pk),
						'subject_pk':str(addSubject.subject.pk),
						'code':str(addSubject.subject.code),
						'description':str(addSubject.subject.description),
						'unit':str(addSubject.subject.unit),
						'status':str(addSubject.status),
						'is_save':True}
				return Response(context)
			return Response({'message':'subject already enroll','is_save':False})
		return Response({'message':'fail','is_save':False})
	return Response({'message':'get request'})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def update_subject_load_api(request):
	if request.method == 'POST':
		subject_pk=request.POST
		subject=get_object_or_404(SubjectsLoaded,pk=subject_pk['is_updated'])
		form = SubjectLoadForm(request.POST, instance=subject)
		if form.is_valid():
			addSubject=form.save(commit=False)
			addSubject.save()
			context={
						'pk':str(addSubject.pk),
						'subject_pk':str(addSubject.subject.pk),
						'code':str(addSubject.subject.code),
						'description':str(addSubject.subject.description),
						'unit':str(addSubject.subject.unit),
						'status':str(addSubject.status),
					'is_updated':True,}
			return Response(context)
		return Response({'is_updated':False})
	return Response({'message':'get request'})

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def get_user_from_token(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		access_token = AccessToken(data['token'])
		user = User.objects.get(id=access_token['user_id'])
		return Response({'id': user.pk, 'username': user.username, 'is_admin': user.is_superuser})
	return Response({'message':'get request'})

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_student_by_id(request, studentid):
	students = Student.objects.filter(student_id = studentid)
	if len(students) > 0:
		return Response({'is_exists' : True, 'id': students.first().id})
	return Response({'is_exists' : False}) 



@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def delete_subject_loaded(request,pk):
	subject=get_object_or_404(SubjectsLoaded,pk=pk)
	if request.method == 'POST':
		subject.delete()
		return Response({'is_delete':True})
	return Response({'is_delete':False})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def drop_subject_loaded(request,pk):
	subject=get_object_or_404(SubjectsLoaded,pk=pk)
	if request.method == 'POST':
		subject.status="drop"
		subject.save()
		serializer=SubjectsLoadedSerializer(subject)
		return Response(serializer.data)
	return Response({'is_drop':False})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def enroll_drop_subject_loaded(request,pk):
	subject=get_object_or_404(SubjectsLoaded,pk=pk)
	if request.method == 'POST':
		subject.status="enrolled"
		subject.save()
		serializer=SubjectsLoadedSerializer(subject)
		return Response(serializer.data)
	return Response({'is_enroll':False})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def get_subjects_by_curriculum_api(request,*args,**kwargs):
	queryset = Curriculum.objects.all()
	sem = kwargs['sem']
	course_pk=kwargs['course']
	course=Course.objects.get(pk=course_pk)
	curriculums=queryset.filter(course=course,semister=sem)
	subjects=[]
	for curriculum in curriculums:
		for subject in curriculum.subjects.all():
			serializer=SubjectSerializer(subject)
			subjects.append(serializer.data)
	context={'subjects':subjects}
	return Response(context)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def get_subjects_by_curriculum_api_all(request,*args,**kwargs):
	curriculums=Curriculum.objects.prefetch_related('subjects').all()
	subjects=[]
	for curriculum in curriculums:
		for subject in curriculum.subjects.all():
			serializer=SubjectSerializer(subject)
			subjects.append(serializer.data)
	context={'subjects':subjects}
	return Response(context)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def api_add_subject_by_curiculum(request,*args,**kwargs):
	major_pk=kwargs['majorpk']
	try:
		course=Course.objects.get(pk=request.POST.get('coursepk'))
		year=Year_level.objects.get(pk=request.POST.get('yearpk'))
		sem=request.POST.get('semister')
		major=Major.objects.get(pk=major_pk)
		subjects_by_curriculum= Curriculum.objects.filter(course=course,year_level=year,semister=sem,major=major)
	except Major.DoesNotExist:
		major = None
	if major == None:
		subjects_by_curriculum= Curriculum.objects.filter(course=course,year_level=year,semister=sem)
	if subjects_by_curriculum.exists():
		subjects={'status':True,'subjects':subjects_by_curriculum[0].subjects.all(),'message':'subjects added'}
		return Response(subjects)
	return Response({'status':False,'message':'curriculum does not exist'})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def add_subject_by_curiculum_api(request,pk):
	enrollbyStud=get_object_or_404(EnrollbyStudent,pk=pk)
	if request.method == "POST":
		major_pk=request.POST.get('majorpk')
		if major_pk == "":
			major_pk=0
		try:
			course=Course.objects.get(pk=request.POST.get('coursepk'))
			year=Year_level.objects.get(pk=request.POST.get('yearpk'))
			sem=request.POST.get('semister')
			major=Major.objects.get(pk=major_pk)
			subjects_by_curriculum= Curriculum.objects.filter(course=course,year_level=year,semister=sem,major=major)
		except Major.DoesNotExist:
			major = None
		if major == None:
			subjects_by_curriculum= Curriculum.objects.filter(course=course,year_level=year,semister=sem)
		if subjects_by_curriculum.exists():
			serialize_subjects=[]
			for subject in subjects_by_curriculum[0].subjects.all():
				duplicate_subject=SubjectsLoaded.objects.filter(enrolled_by_student=enrollbyStud,subject=subject)
				if not duplicate_subject.exists():
					subject_loaded=SubjectsLoaded.objects.create(enrolled_by_student=enrollbyStud,subject=subject,status="draft")
					subject_enroll={'pk':str(subject_loaded.pk),'subject_pk':str(subject_loaded.subject.pk),'code':subject_loaded.subject.code,
					'description':subject_loaded.subject.description,'unit':subject_loaded.subject.unit,'status':subject_loaded.status}
					serialize_subjects.append(subject_enroll)
			subjects={'status':True,'subjects':serialize_subjects,'message':'subjects added'}
			return Response(subjects)
		return Response({'status':False,'message':'curriculum does not exist'})
	return Response({'message':'get'})

# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
# def upload_subjects_api(request):
# 	if request.method == 'POST':
# 		form=UploadExcelForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			df = pd.read_excel('C:/Bitnami/djangostack-2.1.1-1/apps/django/django_projects/enrollment'+form.file.url, sheet_name=0)  
# 			for cell in df.values:
# 				Subject.objects.create(code=cell[0],description=cell[1],unit=cell[2])
# 				context={'is_save':True}
# 			return Response(context)
# 		return Response({'is_save':False})
# 	return Response({'message':'get'})




