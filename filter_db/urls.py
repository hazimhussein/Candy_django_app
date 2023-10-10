## APP(filter_db)

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    path('about',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('project/<str:pk>', views.ProjectDetailView.as_view(),name = 'project_detail'),
]