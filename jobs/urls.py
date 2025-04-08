from django.urls import re_path, path
from jobs import views


from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0



urlpatterns = [
    # 首页自动跳转到 职位列表
    path("", views.joblist, name="name"),
    #职位列表
    re_path(r'^joblist/', views.joblist, name='joblist'),
    #职位详情
    re_path(r'^jobdetail/(?P<job_id>\d+)/', views.jobdetail, name='jobdetail'),
    #提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    path('sentry-debug/', trigger_error),
]