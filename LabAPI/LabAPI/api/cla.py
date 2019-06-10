from rest_framework import serializers

from api.models import *

# 用户的序列化
class LabUserstudents(serializers.ModelSerializer):
    class Meta:
        model = LabUserstudent
        fields = '__all__'

class LabUserstudents2(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabUserstudent
        exclude = ['belong']

class LabUserstudents3(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabUserstudent
        fields = '__all__'

class LabUserstudents4(serializers.ModelSerializer):
    class Meta:
        model = LabUserstudent
        fields = ("id","student_name")

class LabUserteachers(serializers.ModelSerializer):
    class Meta:
        model = LabUserstudent
        fields = '__all__'

class LabUserteachers(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabUserteacher
        fields = '__all__'

# 分组的序列化
class LabTeams(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabTeam
        fields = '__all__'

# 成果的序列化
class LabGains(serializers.ModelSerializer):
    class Meta:
        model = LabGain
        fields = '__all__'

# 签到的序列化
class LabRegisters(serializers.ModelSerializer):
    class Meta:
        model = LabRegister
        fields = '__all__'

# 个人规划的序列化
class LabPlans(serializers.ModelSerializer):
    class Meta:
        model = LabPlan
        fields = '__all__'

class LabTPlans(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabTPlan
        fields = ["plan_ID"]

# 比赛的序列化
class LabCompetes(serializers.ModelSerializer):
    class Meta:
        model = LabCompete
        fields = '__all__'

class LabCompeteTeams(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabCompeteTeam
        fields = '__all__'
class LabCompeteTeams2(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LabCompeteTeam
        fields = ["team_compete"]

# 练习模块的序列化
# 单选题的序列化
class LabPraProb1s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProb1
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

class LabPraProb2s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProb2
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

class LabPraProb3s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProb3
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

# 多选题的序列化
class LabPraProbD1s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbD1
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

class LabPraProbD2s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbD2
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

class LabPraProbD3s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbD3
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

# 判断题的序列化
class LabPraProbP1s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbP1
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

class LabPraProbP2s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbP2
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

class LabPraProbP3s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbP3
        fields = ("prob_body","prob_option_a","prob_option_b","prob_option_c","prob_option_d",)

# 填空题的序列化
class LabPraProbK1s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbK1
        fields = ["prob_body"]

class LabPraProbK2s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbK2
        fields = ["prob_body"]

class LabPraProbK3s(serializers.ModelSerializer):
    class Meta:
        model =LabPraProbK3
        fields = ["prob_body"]

class LabPraPapers(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = LabPraPaper
        fields = '__all__'

# 实验室新闻序列化
class LabInNewss(serializers.ModelSerializer):
    class Meta:
        model = LabInNews
        fields = '__all__'


# 贴子序列化
class LabPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabPost
        fields = '__all__'