from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 分组表
class LabTeam(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField( default='',blank=True,max_length=50)
    team_captain = models.CharField(default='',blank=True, max_length=50)
    
# 老师用户
class LabUserteacher(models.Model):
    teacher_name = models.CharField(default='',blank=True,max_length=20)
    teacher_photo = models.ImageField(blank=True,null=True)
    teacher_introduction = models.TextField(blank=True,null=True)
    teacher_access = models.IntegerField(default='1')
    teacher_postion = models.CharField(default='',blank=True,max_length=20)
    belong = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE,blank=True,null=True,related_name='LabUserteacher')

# 学生用户
class LabUserstudent(models.Model):
    student_name = models.CharField(default='',blank=True,max_length=20,unique=True)
    student_photo = models.ImageField(blank=True,null=True)
    student_introduction = models.TextField(blank=True,null=True)
    student_major = models.CharField(default='',blank=True,max_length=20)
    student_teamid = models.ForeignKey(LabTeam, on_delete=models.CASCADE)
    student_access = models.IntegerField(default='2')
    belong = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='LabUserstudent')
    
    
# 普通用户
class LabUsercommen(models.Model):
    commen_account = models.IntegerField(default='')
    commen_name = models.CharField(default='',blank=True,max_length=20)
    commen_major = models.CharField(default='',blank=True,max_length=20)
    commen_number = models.IntegerField()
    belong = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='LabUsercommen')

# 成果表
class LabGain(models.Model):
    belong = models.ForeignKey( LabUserstudent,to_field='id', on_delete=models.CASCADE)
    gain_title = models.CharField( max_length=50)
    gain_decb = models.TextField(blank=True,null=True)
    gain_photo = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    gain_see = models.IntegerField(blank=True,null=True)
    gain_getdate = models.DateField( auto_now=False, auto_now_add=False,null=True)

    class Meta:
        ordering = ['-gain_getdate']

# 签到表
class LabRegister(models.Model):
    user_id = models.ForeignKey( LabUserstudent,to_field='id', on_delete=models.CASCADE)
    content = models.CharField( max_length=100)
    img = models.ImageField(blank=True,null=True)
    date_time = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['-date_time']

# 指定计划
class LabPlan(models.Model):
    user_plan = models.CharField(default='',blank=True,max_length=20)
    user_plandate = models.DateField(auto_now=False, auto_now_add=False)
    user_remind = models.BooleanField(default='')

class LabTPlan(models.Model):
    user_ID = models.ForeignKey(LabUserstudent,on_delete='CASCADE')
    plan_ID = models.ForeignKey(LabPlan,on_delete='CASCADE')

# 比赛表
class LabCompete(models.Model):
    compete_name = models.CharField( max_length=50)
    compete_desc = models.CharField( max_length=50)
    compete_type = models.CharField( max_length=20)
    compete_date = models.DateField( auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['-compete_date']

# 队伍表
class LabCompeteTeam(models.Model):
    team_compete = models.ForeignKey( LabCompete, on_delete=models.CASCADE)
    team_playerID = models.ForeignKey( LabUserstudent, on_delete=models.CASCADE)
    

# 练习试题库
# 单选题难度为1
class LabPraProb1(models.Model):
    prob_difficult = models.IntegerField(default='1')
    prob_body = models.TextField(max_length=2048,null=True)
    prob_option_a = models.CharField(max_length=1024,null=True)
    prob_option_b = models.CharField(max_length=1024,null=True)
    prob_option_c = models.CharField(max_length=1024,null=True)
    prob_option_d = models.CharField(max_length=1024,null=True)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='2')
    prob_type = models.CharField( default='单选', max_length=50)

# 单选题难度为2
class LabPraProb2(models.Model):
    prob_difficult = models.IntegerField(default='2')
    prob_body = models.TextField(max_length=2048)
    prob_option_a = models.CharField(max_length=1024)
    prob_option_b = models.CharField(max_length=1024)
    prob_option_c = models.CharField(max_length=1024)
    prob_option_d = models.CharField(max_length=1024)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='4')
    prob_type = models.CharField( default='单选', max_length=50)

# 单选题难度为3
class LabPraProb3(models.Model):
    prob_difficult = models.IntegerField(default='3')
    prob_body = models.TextField(max_length=2048)
    prob_option_a = models.CharField(max_length=1024)
    prob_option_b = models.CharField(max_length=1024)
    prob_option_c = models.CharField(max_length=1024)
    prob_option_d = models.CharField(max_length=1024)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='5')
    prob_type = models.CharField( default='单选', max_length=50)

# 多选题难度为1
class LabPraProbD1(models.Model):
    prob_difficult = models.IntegerField(default='1')
    prob_body = models.TextField(max_length=2048,null=True)
    prob_option_a = models.CharField(max_length=1024,null=True)
    prob_option_b = models.CharField(max_length=1024,null=True)
    prob_option_c = models.CharField(max_length=1024,null=True)
    prob_option_d = models.CharField(max_length=1024,null=True)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='2')
    prob_type = models.CharField( default='多选', max_length=50)

# 多选题难度为2
class LabPraProbD2(models.Model):
    prob_difficult = models.IntegerField(default='2')
    prob_body = models.TextField(max_length=2048,default='多选题的难度为2')
    prob_option_a = models.CharField(default='A',max_length=1024)
    prob_option_b = models.CharField(default='B',max_length=1024)
    prob_option_c = models.CharField(default='C',max_length=1024)
    prob_option_d = models.CharField(default='D',max_length=1024)
    prob_right = models.CharField( default='ABC',max_length=50,null=True)
    prob_score = models.IntegerField(default='4')
    prob_type = models.CharField( default='多选', max_length=50)

# 多选题难度为3
class LabPraProbD3(models.Model):
    prob_difficult = models.IntegerField(default='3')
    prob_body = models.TextField(max_length=2048,default='多选题的难度为3')
    prob_option_a = models.CharField(max_length=1024,default='A')
    prob_option_b = models.CharField(max_length=1024,default='B')
    prob_option_c = models.CharField(max_length=1024,default='C')
    prob_option_d = models.CharField(max_length=1024,default='D')
    prob_right = models.CharField(default='AD', max_length=50,null=True)
    prob_score = models.IntegerField(default='6')
    prob_type = models.CharField( default='多选', max_length=50)


# 判断题难度为1
class LabPraProbP1(models.Model):
    prob_difficult = models.IntegerField(default='1')
    prob_body = models.TextField(max_length=2048,null=True,default='判断题难度为1')
    prob_option_a = models.CharField(max_length=1024,null=True,default='A')
    prob_option_b = models.CharField(max_length=1024,null=True,default='B')
    prob_option_c = models.CharField(max_length=1024,null=True,default='C')
    prob_option_d = models.CharField(max_length=1024,null=True,default='D')
    prob_right = models.CharField( default='A',max_length=50,null=True)
    prob_score = models.IntegerField(default='1')
    prob_type = models.CharField( default='判断', max_length=50)

# 判断题难度为2
class LabPraProbP2(models.Model):
    prob_difficult = models.IntegerField(default='2')
    prob_body = models.TextField(max_length=2048,default='判断题难度为2')
    prob_option_a = models.CharField(max_length=1024,default='A')
    prob_option_b = models.CharField(max_length=1024,default='B')
    prob_option_c = models.CharField(max_length=1024,default='C')
    prob_option_d = models.CharField(max_length=1024,default='D')
    prob_right = models.CharField( default='B',max_length=50,null=True)
    prob_score = models.IntegerField(default='2')
    prob_type = models.CharField( default='判断', max_length=50)

# 判断题难度为3
class LabPraProbP3(models.Model):
    prob_difficult = models.IntegerField(default='3')
    prob_body = models.TextField(max_length=2048,default='判断题难度为3')
    prob_option_a = models.CharField(max_length=1024,default='A')
    prob_option_b = models.CharField(max_length=1024,default='B')
    prob_option_c = models.CharField(max_length=1024,default='C')
    prob_option_d = models.CharField(max_length=1024,default='D')
    prob_right = models.CharField( default='C',max_length=50,null=True)
    prob_score = models.IntegerField(default='4')
    prob_type = models.CharField( default='判断', max_length=50)

# 填空题难度为1
class LabPraProbK1(models.Model):
    prob_difficult = models.IntegerField(default='1')
    prob_body = models.TextField(max_length=2048,null=True,default='填空题难度为1')
    prob_right = models.CharField( max_length=50,null=True,default='在此输入答案')
    prob_score = models.IntegerField(default='1')
    prob_type = models.CharField( default='填空', max_length=50)

# 填空题难度为2
class LabPraProbK2(models.Model):
    prob_difficult = models.IntegerField(default='2')
    prob_body = models.TextField(max_length=2048,default='填空题难度为2')
    prob_right = models.CharField( max_length=50,null=True,default='在此输入答案')
    prob_score = models.IntegerField(default='2')
    prob_type = models.CharField( default='填空', max_length=50)

# 填空题难度为3
class LabPraProbK3(models.Model):
    prob_difficult = models.IntegerField(default='3')
    prob_body = models.TextField(max_length=2048,default='填空题难度为3')
    prob_right = models.CharField( max_length=50,null=True,default='在此输入答案')
    prob_score = models.IntegerField(default='4')
    prob_type = models.CharField( default='填空', max_length=50)

# 实验室新闻表
class LabInNews(models.Model):
    news_title = models.CharField( max_length=50)
    news_content = models.TextField()
    news_date = models.DateField( auto_now=False, auto_now_add=False)
    news_see = models.IntegerField(null=True)
    news_comment = models.TextField(max_length=1024)
    news_captainid = models.ForeignKey(LabUserstudent, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-news_date"]


# 目前接口用不到的数据库

# 从试题库调取试题保存的试题表
# 难度为1
class LabPraProbt1(models.Model):
    prob_difficult = models.IntegerField(default='1')
    prob_body = models.TextField(max_length=2048,null=True)
    prob_option_a = models.CharField(max_length=1024,null=True)
    prob_option_b = models.CharField(max_length=1024,null=True)
    prob_option_c = models.CharField(max_length=1024,null=True)
    prob_option_d = models.CharField(max_length=1024,null=True)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='2')

# 难度为2
class LabPraProbt2(models.Model):
    prob_difficult = models.IntegerField(default='2')
    prob_body = models.TextField(max_length=2048)
    prob_option_a = models.CharField(max_length=1024)
    prob_option_b = models.CharField(max_length=1024)
    prob_option_c = models.CharField(max_length=1024)
    prob_option_d = models.CharField(max_length=1024)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='4')

# 难度为3
class LabPraProbt3(models.Model):
    prob_difficult = models.IntegerField(default='3')
    prob_body = models.TextField(max_length=2048)
    prob_option_a = models.CharField(max_length=1024)
    prob_option_b = models.CharField(max_length=1024)
    prob_option_c = models.CharField(max_length=1024)
    prob_option_d = models.CharField(max_length=1024)
    prob_right = models.CharField( max_length=50,null=True)
    prob_score = models.IntegerField(default='5')


# 根据难度生成的试卷表
class LabPraPaper(models.Model):
    paper_difficult = models.IntegerField(default='1')
    paper_d1 = models.ManyToManyField( LabPraProbt1)
    paper_d2 = models.ManyToManyField( LabPraProbt2)
    paper_d3 = models.ManyToManyField( LabPraProbt3)

# 练习成绩
class LabPracResult(models.Model):
    prac_user = models.ForeignKey( LabUserstudent, on_delete=models.CASCADE)
    prac_score = models.IntegerField()
    prac_ratio = models.FloatField(max_length=64,default='%0')
    prac_paper = models.ForeignKey( LabPraPaper, on_delete=models.CASCADE) 

# 邮件发送 
class LabEmail(models.Model):
    email_send = models.ForeignKey(LabUserstudent,on_delete='CASCADE')
    # email_accept = models.ForeignKey(LabUserstudent,on_delete='CASCADE')
    email_content = models.TextField(default='')
    email_state = models.BooleanField(default=False)

# 收藏表
class LabCollect(models.Model):
    collect_url = models.URLField(max_length=200,blank=True,null=True)
    collect_data = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)

class LabsCollect(models.Model):
    user_ID = models.ForeignKey(LabUserstudent,on_delete='CASCADE')

# 动态表
class LabInformation(models.Model):
    userID = models.ForeignKey(LabUserstudent, on_delete=models.CASCADE)
    information_content = models.TextField(default='')
    information_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True,null=True)


# 贴子类型
class LabPostType(models.Model):
    type_name = models.CharField(max_length=17)

    def __str__(self):
        return self.type_name

# 贴子表
class LabPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=30, default='在此输入贴子标题')
    content = models.TextField(default='在此输入贴子内容')
    post_type = models.ForeignKey(
        LabPostType, on_delete=models.DO_NOTHING, null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    edited_data = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_data']    



    

    


















