from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .forms import PersonDetailForm,CustomerDetailForm
from .models import Person,Customer
from django.views.generic import TemplateView
from .risk_model import RiskOutput,RiskModel



class Home(TemplateView):
    context = {}
    template_name = "risk_app/home.html"

    def get(self,request):
        form = CustomerDetailForm()
        self.context['form'] = form
        self.context['detail'] = Customer.objects.all()
        return render(request,self.template_name,self.context)

    def post(self,request):
        form = CustomerDetailForm(request.POST)
        if form.is_valid():
            form.save()

        self.context['form'] = form
        self.context['detail'] = Customer.objects.all()
        return render(request, self.template_name, self.context)

class Result(TemplateView):
    context = {}
    template_name = "risk_app/result.html"

    def get(self,request):
        form = CustomerDetailForm()
        self.context['form'] = form
        self.context['detail'] = Customer.objects.all()
        return render(request,self.template_name,self.context)

    def post(self,request):
        form = CustomerDetailForm(request.POST)
        if form.is_valid():
            form.save()

        cust_attrs = form.cleaned_data
        name = cust_attrs.get('Name')
        Age = cust_attrs.get('Age')
        Previously_Insured = cust_attrs.get('Previously_Insured')
        Vehicle_Age = cust_attrs.get('Vehicle_Age')
        Vehicle_Damage = cust_attrs.get('Vehicle_Damage')
        Annual_Premium = cust_attrs.get('Annual_Premium')

        Previously_Insured = 1 if str(Previously_Insured).lower == "yes" else 0
        Vehicle_Damage = 1 if str(Vehicle_Damage).lower == "yes" else 0

        cust_data = [Age,Previously_Insured,Vehicle_Age,Vehicle_Damage,	Annual_Premium]

        print("Cust Data: ",cust_data)
            
        risk_model = RiskModel()
        risk = risk_model.predict_res(cust_data=cust_data)
        print("Risk: ",risk)
        
        output_risk = RiskOutput(name=name,risk=risk)

        self.context['form'] = form
        self.context['detail'] = output_risk
        return render(request, self.template_name, self.context)