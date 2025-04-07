from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404

from jobs.models import Job, JobTypes,Cities,Resume
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
# Create your views here.

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    #template = loader.get_template('joblist.html')
    context = {'job_list': job_list}
    for job in job_list:
        job.job_type = JobTypes[job.job_type][1]
        job.job_location = Cities[job.job_location][1]
    #return HttpResponse(template.render(context))
    # 带有上下文的模板渲染
    return render(request, 'joblist.html', context)

def jobdetail(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        template = loader.get_template('job.html')
        context = {'job': job}
        job.job_type = JobTypes[job.job_type][1]
        job.job_location = Cities[job.job_location][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    #return HttpResponse(template.render(context))
    # 带有上下文的模板渲染
    return render(request, 'job.html', context)

class ResumeCreateView(LoginRequiredMixin, CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree", "picture", "attachment",
        "candidate_introduction", "work_experience", "project_experience"]

    ### 从 URL 请求参数获取参数
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    ### 保存数据
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ResumeDetailView(DetailView):
    """   简历详情页    """
    model = Resume
    template_name = 'resume_detail.html'