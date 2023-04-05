from django.shortcuts import render, HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View

class index(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'resumeapp/index.html', {'form':form, 'candidates':candidates})
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    
class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'resumeapp/candidate.html', {'candidate':candidate})