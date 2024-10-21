# quizzerapp/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.organization import add_organization, get_organizations, organization_detail
from .views.questions import QuestionViewSet
from .views.questiontype import QuestionTypeViewSet
from .views.questionbank import QuestionBankViewSet

router = DefaultRouter()

router.register(r'questions', QuestionViewSet,basename='questions')
router.register(r'question-types', QuestionTypeViewSet)
router.register(r'question-banks', QuestionBankViewSet, basename='question-bank')


urlpatterns = [
    path('organizations/', add_organization, name='add_organization'),  # POST to add organization
    path('organizations/all/', get_organizations, name='get_organizations'),  # GET to list all organizations
    path('organizations/<int:pk>/', organization_detail, name='organization_detail'),  # GET, PUT, DELETE for a specific organization
   

    path('', include(router.urls)),
   
]





