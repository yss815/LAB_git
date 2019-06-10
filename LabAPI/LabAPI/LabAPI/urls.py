"""LabAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
     # 调取所有的学生成员信息
    path('api/stuuser/', views.stuuserData),
    # 调取单个学生信息
    path('api/stuuser/<int:user_id>/', views.stuuserID),
    # 查询对应年级的所有学生
    path('api/grade/<int:grade_id>/',views.stuuserGrade),
    # 查询组的成员信息
    path('api/team/<int:team_id>/',views.teamID),
    # 查询所有老师信息
    path('api/teauser/',views.teauserData),
    # 查询所有成果信息
    path('api/gain/',views.gainData),
    # 查询单个学生信息及其成果
    path('api/gain/<int:gain_id>/',views.gainID),
    # 查询所有学生的签到信息
    path('api/register/',views.registerData),
    # 查询单个学生的签到信息
    path('api/register/<int:user_id>/',views.registerID),
    # 查询所有学生的计划安排
    path('api/plan/',views.planData),
    # 查询单个学生的计划安排
    path('api/plan/<int:user_id>/',views.planID),
    # 查询所有比赛信息
    path('api/compete/',views.competeData),
    # 根据ID查询单个学生比赛信息
    path('api/competestu/<int:user_id>/',views.competeID),
    # 根据比赛ID查询参赛学生
    path('api/competetype/<int:type_id>/',views.competeType),
    # 根据难度调取对应试题（包含各种试题）
    path('api/pracid/<int:level_id>/',views.prapaperID),
    # 根据题量调取对应试题（包含各种试题）
    path('api/pracnum/<int:num>/',views.prapaperNum),
    # 根据题型和题量调取试题
    path('api/practype/<int:type_id>/<int:num>/',views.prapaperType),
    # 根据数量调取实验室新闻
    path('api/news/<int:num>/',views.labnews),
    # 根据数量贴子信息
    path('api/postnum/<int:num>/',views.postsDataNum),
    # 根据ID查询单个贴子信息
    path('api/postid/<int:post_id>/',views.postsDataID),
    # 测试接口返回的页面
    path('',views.index),
]
