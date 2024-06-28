from django.shortcuts import render
from django.views import View
#Models
from resume.models import Education,Experience
class ResumeView(View):
    def get(self,request):
        experiences = Experience.objects.all().filter(status=True).order_by('-date')
        educations = Education.objects.all().filter(status=True).order_by('-date')
        context={
            'educations':educations,
            'experiences':experiences,
        }
        return render(request,'resume/resume.html',context)