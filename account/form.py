from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from account.models import Address, User


class RegisterForm(forms.Form):
    email = forms.EmailField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'email'}) , required=True)
    is_Accept_terms = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}) , required=True)

class OtpForm(forms.Form):
    code = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':' otp :'}) , validators=[validators.MaxLengthValidator(4)])
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox , required = True)
    def clean_code(self):
        code = self.cleaned_data.get("code")
        if len(code)<4:
            raise ValidationError("this code is invalid")
        return code

class Edite_Profile_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['Full_name', 'username' , 'phone' , 'postal_code']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':''}),
            'Full_name' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':''}),
            'phone' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':''}),
            'postal_code' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':''}),
        }

class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
        model = Address
        exclude = '__all__'