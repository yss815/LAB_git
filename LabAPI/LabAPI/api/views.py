from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render

from api.cla import *
import random
# 查询所有学生信息
@api_view(['GET'])
def stuuserData(request):
    labstudent = LabUserstudent.objects.all() 
    labstudentData = LabUserstudents(labstudent,many=True)

    return Response({'labstudent':labstudentData.data})

# 查询所有老师信息
@api_view(['GET'])
def teauserData(request):
    labteacher = LabUserteacher.objects.all()
    labteacherData = LabUserteachers(labteacher,many=True)

    return Response({'labteacher':labteacherData.data})


# 根据ID查询单个学生信息
@api_view(['GET'])
def stuuserID(request,user_id):
    labstudent = LabUserstudent.objects.filter(id=user_id)
    labstudentData = LabUserstudents3(labstudent,many=True)

    return Response({'labstudent':labstudentData.data})

# 查询对应年纪的所有学生
@api_view(['GET'])
def stuuserGrade(request,grade_id):
    labstudent = LabUserstudent.objects.filter(student_access=grade_id)
    labstudentData = LabUserstudents(labstudent,many=True)

    return Response({'labstudent':labstudentData.data})

# 根据teamID查询组员信息
@api_view(['GET'])
def teamID(request,team_id):
    labteam = LabTeam.objects.filter(team_id=team_id)
    labteamData = LabTeams(labteam,many=True)

    labstudent = LabUserstudent.objects.filter(student_teamid=team_id)
    labstudentData = LabUserstudents2(labstudent,many=True)

    return Response({'labteam':labteamData.data,'labstudent':labstudentData.data})

# 查询所有成果信息
@api_view(['GET'])
def gainData(request):
    labgain = LabGain.objects.all()
    labgainData = LabGains(labgain,many=True)

    return Response({'labgain':labgainData.data})

# 列出单个学生信息及其成果
@api_view(['GET'])
def gainID(request,gain_id):
    labstudent = LabUserstudent.objects.filter(id=gain_id)
    labstudentData = LabUserstudents4(labstudent,many=True)

    labgain = LabGain.objects.filter(belong_id=gain_id)
    labgainData = LabGains(labgain,many=True)

    return Response({'labstudent':labstudentData.data,'labgain':labgainData.data})

# 列出所有学生的签到信息
@api_view(['GET'])
def registerData(request):
    labregister = LabRegister.objects.order_by("-date_time")
    labregisterData = LabRegisters(labregister,many=True)

    return Response({'labregister':labregisterData.data})

# 列出单个学生的签到信息
@api_view(['GET'])
def registerID(request,user_id):
    student = LabUserstudent.objects.filter(id=user_id)
    studentData = LabUserstudents4(student,many=True)

    labregister = LabRegister.objects.filter(user_id=user_id)
    labregisterData = LabRegisters(labregister,many=True)

    return Response({'student':studentData.data,'labregister':labregisterData.data})

# 列出所有学生的计划信息
@api_view(['GET'])
def planData(request):
    labplan = LabPlan.objects.all()
    labplanData = LabPlans(labplan,many=True)

    return Response({'labplan':labplanData.data})


# 查询单个学生的计划安排
@api_view(['GET'])
def planID(request,user_id):
    student = LabUserstudent.objects.filter(id=user_id)
    studentData = LabUserstudents4(student,many=True)

    labtplan = LabTPlan.objects.filter(user_ID=user_id)
    labtplanData = LabTPlans(labtplan,many=True)

    return Response({'student':studentData.data,'labtplan':labtplanData.data})

# 查询所有比赛信息
@api_view(['GET'])
def competeData(request):
    labcompete = LabCompete.objects.all()
    labcompeteData = LabCompetes(labcompete,many=True)

    return Response({'labcompete':labcompeteData.data})

# 根据ID查询单个学生比赛信息
@api_view(['GET'])
def competeID(request,user_id):
    student = LabUserstudent.objects.filter(id=user_id)
    studentData = LabUserstudents4(student,many=True)

    labcompeteteam = LabCompeteTeam.objects.filter(team_playerID=user_id)
    labcompeteteamData = LabCompeteTeams(labcompeteteam,many=True)

    return Response({'student':studentData.data,'labcompeteteam':labcompeteteamData.data})

# 根据比赛ID查询参赛学生
@api_view(['GET'])
def competeType(request,type_id):
    labcompete = LabCompete.objects.filter(id=type_id)
    labcompeteData = LabCompetes(labcompete,many=True)
    
    labcompeteteam = LabCompeteTeam.objects.filter(team_compete=type_id)
    labcompeteteamData = LabCompeteTeams2(labcompeteteam,many=True)

    return Response({'labcompete':labcompeteData.data,'labcompeteteam':labcompeteteamData.data})

# 根据难度调取对应试题(包含单选，多选，判断题，填空题)
@api_view(['GET'])
def prapaperID(request,level_id):
    # s1,s2,s3代表每个难度应调出的题数
    if(level_id==1):
        s1,s2,s3=30,10,0   
    elif(level_id==2):
        s1,s2,s3=20,10,4
    else:
        s1,s2,s3=10,10,8


    # 难度为1
    # 单选题
    question1 = LabPraProb1.objects.filter(id__in = [random.random()*51 for _ in range(s1)])
    question1Data = LabPraProb1s(question1,many=True)
    # 多选题
    questiond1 = LabPraProbD1.objects.filter(id__in = [random.random()*40 for _ in range(s1)])
    questiond1Data = LabPraProbD1s(questiond1,many=True)
    # 判断题
    questionp1 = LabPraProbP1.objects.filter(id__in = [random.random()*50 for _ in range(s1)])
    questionp1Data = LabPraProbP1s(questionp1,many=True)
    # 填空题
    questionk1 = LabPraProbK1.objects.filter(id__in = [random.random()*50 for _ in range(s1)])
    questionk1Data = LabPraProbK1s(questionk1,many=True)

    # 难度为2
    # 单选题
    question2 = LabPraProb2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    question2Data = LabPraProb2s(question2,many=True)
    # 多选题
    questiond2 = LabPraProbD2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    questiond2Data = LabPraProbD2s(questiond2,many=True)
    # 判断题
    questionp2 = LabPraProbP2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    questionp2Data = LabPraProbP2s(questionp2,many=True)
    # 填空题
    questionk2 = LabPraProbK2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    questionk2Data = LabPraProbK2s(questionk2,many=True)

    # 难度为3
    # 单选题
    question3 = LabPraProb3.objects.filter(id__in = [random.random()*20 for _ in range(s3)])
    question3Data = LabPraProb3s(question3,many=True)
    # 多选题
    questiond3 = LabPraProbD3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
    questiond3Data = LabPraProbD3s(questiond3,many=True)
    # 判断题
    questionp3 = LabPraProbP3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
    questionp3Data = LabPraProbP3s(questionp3,many=True)
    # 填空题
    questionk3 = LabPraProbK3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
    questionk3Data = LabPraProbK3s(questionk3,many=True)

    return Response({'question1':question1Data.data,'question2':question2Data.data,'question3':question3Data.data,'questiond1':questiond1Data.data,'questiond2':questiond2Data.data,'questiond3':questiond3Data.data,'questionp1':questionp1Data.data,'questionp2':questionp2Data.data,'questionp3':questionp3Data.data,'questionk1':questionk1Data.data,'questionk2':questionk2Data.data,'questionk3':questionk3Data.data})

# 根据题量调取试题(该题量非总题量而是每个题型的题量)
@api_view(['GET'])
def prapaperNum(request,num):
    s1 = int(num/2)
    s2 = int(num/3)
    s3 = int(num-s1-s2)
    # print(s1,s2,s3)
    # 难度为1
    # 单选题
    question1 = LabPraProb1.objects.filter(id__in = [random.random()*51 for _ in range(s1)])
    question1Data = LabPraProb1s(question1,many=True)
    # 多选题
    questiond1 = LabPraProbD1.objects.filter(id__in = [random.random()*40 for _ in range(s1)])
    questiond1Data = LabPraProbD1s(questiond1,many=True)
    # 判断题
    questionp1 = LabPraProbP1.objects.filter(id__in = [random.random()*50 for _ in range(s1)])
    questionp1Data = LabPraProbP1s(questionp1,many=True)
    # 填空题
    questionk1 = LabPraProbK1.objects.filter(id__in = [random.random()*50 for _ in range(s1)])
    questionk1Data = LabPraProbK1s(questionk1,many=True)

    # 难度为2
    # 单选题
    question2 = LabPraProb2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    question2Data = LabPraProb2s(question2,many=True)
    # 多选题
    questiond2 = LabPraProbD2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    questiond2Data = LabPraProbD2s(questiond2,many=True)
    # 判断题
    questionp2 = LabPraProbP2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    questionp2Data = LabPraProbP2s(questionp2,many=True)
    # 填空题
    questionk2 = LabPraProbK2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
    questionk2Data = LabPraProbK2s(questionk2,many=True)

    # 难度为3
    # 单选题
    question3 = LabPraProb3.objects.filter(id__in = [random.random()*20 for _ in range(s3)])
    question3Data = LabPraProb3s(question3,many=True)
    # 多选题
    questiond3 = LabPraProbD3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
    questiond3Data = LabPraProbD3s(questiond3,many=True)
    # 判断题
    questionp3 = LabPraProbP3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
    questionp3Data = LabPraProbP3s(questionp3,many=True)
    # 填空题
    questionk3 = LabPraProbK3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
    questionk3Data = LabPraProbK3s(questionk3,many=True)


    return Response({'question1':question1Data.data,'question2':question2Data.data,'question3':question3Data.data,'questiond1':questiond1Data.data,'questiond2':questiond2Data.data,'questiond3':questiond3Data.data,'questionp1':questionp1Data.data,'questionp2':questionp2Data.data,'questionp3':questionp3Data.data,'questionk1':questionk1Data.data,'questionk2':questionk2Data.data,'questionk3':questionk3Data.data})

# 根据(一种)题型加题量调取试题
@api_view(['GET'])
def prapaperType(request,type_id,num):
    s1 = int(num/2)
    s2 = int(num/3)
    s3 = int(num-s1-s2)
    # print(s1,s2,s3)

    if(type_id==1):
        # 单选题
        question1 = LabPraProb1.objects.filter(id__in = [random.random()*51 for _ in range(s1)])
        question1Data = LabPraProb1s(question1,many=True)

        question2 = LabPraProb2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
        question2Data = LabPraProb2s(question2,many=True)

        question3 = LabPraProb3.objects.filter(id__in = [random.random()*20 for _ in range(s3)])
        question3Data = LabPraProb3s(question3,many=True)
    elif(type_id==2):
        # 多选题
        question1 = LabPraProbD1.objects.filter(id__in = [random.random()*40 for _ in range(s1)])
        question1Data = LabPraProbD1s(question1,many=True)

        question2 = LabPraProbD2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
        question2Data = LabPraProbD2s(question2,many=True)

        question3 = LabPraProbD3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
        question3Data = LabPraProbD3s(question3,many=True)
    elif(type_id==3):
        # 判断题
        question1 = LabPraProbP1.objects.filter(id__in = [random.random()*50 for _ in range(s1)])
        question1Data = LabPraProbP1s(question1,many=True)

        question2 = LabPraProbP2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
        question2Data = LabPraProbP2s(question2,many=True)

        question3 = LabPraProbP3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
        question3Data = LabPraProbP3s(question3,many=True)
    else:
        # 填空题
        question1 = LabPraProbK1.objects.filter(id__in = [random.random()*50 for _ in range(s1)])
        question1Data = LabPraProbK1s(question1,many=True)

        question2 = LabPraProbK2.objects.filter(id__in = [random.random()*40 for _ in range(s2)])
        question2Data = LabPraProbK2s(question2,many=True)

        question3 = LabPraProbK3.objects.filter(id__in = [random.random()*40 for _ in range(s3)])
        question3Data = LabPraProbK3s(question3,many=True)

    return Response({'question1':question1Data.data,'question2':question2Data.data,'question3':question3Data.data})

# 根据数量调取实验室新闻
@api_view(['GET'])
def labnews(request,num):
    news = LabInNews.objects.all()[:num]
    newsData = LabInNewss(news,many=True)

    return Response({'news':newsData.data})


# 根据数量查询贴子信息
@api_view(['GET'])
def postsDataNum(request,num):
    post = LabPost.objects.all()[:num]
    postData = LabPostSerializer(post, many=True)

    return Response({'post': postData.data})

# 根据ID查询单个贴子信息
@api_view(['GET'])
def postsDataID(request, post_id):
    post = LabPost.objects.filter(id=post_id)
    postData = LabPostSerializer(post, many=True)

    return Response({'post': postData.data})

def index(request):

    return render(request,'api/index.html')