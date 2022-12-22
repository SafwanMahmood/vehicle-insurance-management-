from django import forms
from  .models import Person,Customer


class PersonDetailForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

        widgets = {
            'BirthDate': forms.DateInput(attrs={'type':'date'}),
            }

class CustomerDetailForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
