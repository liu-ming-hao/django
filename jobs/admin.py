from django.contrib import admin

from jobs.models import Job,Resume
from django.contrib import messages
from interview.models import Candidate
from datetime import datetime

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    #参考models.py中的定义填充字段
    list_display = ('job_type','job_name','job_location','creator','created_date','updated_date')

    exclude = ('creator',)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job,JobAdmin)

# 简历管理页定义事件；候选人进入面试流程
def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        # 把 obj 对象中的所有属性拷贝到 candidate 对象中:
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + "," + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, '候选人: %s 已成功进入面试流程' % (candidate_names) )

enter_interview_process.short_description = "进入面试流程"

class ResumeAdmin(admin.ModelAdmin):
    actions = [enter_interview_process,]

    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major','created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            "applicant", ("username", "city", "phone"),
            ("email", "apply_position", "born_address", "gender", ), ("picture", "attachment",),
            ("bachelor_school", "master_school"), ("major", "degree"), ('created_date', 'modified_date'),
            "candidate_introduction", "work_experience","project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Resume,ResumeAdmin)