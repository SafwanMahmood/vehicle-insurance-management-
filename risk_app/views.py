from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .forms import PersonDetailForm
from .models import Person
from django.views.generic import TemplateView


class Home(TemplateView):
    context = {}
    template_name = "risk_app/home.html"

    def get(self,request):
        form = PersonDetailForm()
        self.context['form'] = form
        self.context['detail'] = Person.objects.all()
        return render(request,self.template_name,self.context)

    def post(self,request):
        form = PersonDetailForm(request.POST)

        if form.is_valid():
            form.save()

        self.context['form'] = form
        self.context['detail'] = Person.objects.all()
        return render(request, self.template_name, self.context)

class Result(TemplateView):
    context = {}
    template_name = "risk_app/result.html"

    def get(self,request):
        form = PersonDetailForm()
        self.context['form'] = form
        print("Data: get1 ", form.data)
        self.context['detail'] = Person.objects.all()
        return render(request,self.template_name,self.context)

    def post(self,request):
        form = PersonDetailForm(request.POST)
        if form.is_valid():
            form.save()

        cust_attrs = form.cleaned_data
        print("NAME: ",cust_attrs.get('Name'))

        self.context['form'] = form
        self.context['detail'] = Person.objects.all()
        return render(request, self.template_name, self.context)