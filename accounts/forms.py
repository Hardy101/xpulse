from django import forms
from .models import CustomUser

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'x_handle']
    
    email = forms.CharField(
    label='Email', 
    widget=forms.TextInput(attrs={
        'id': 'email',
        'class': 'poppins-bold w-full bg-tranparent p-2 outline-none text-md border-[1.4px] rounded-md border-blue-1 text-xs',
        'placeholder': 'Email',  # Add the placeholder attribute
        'required': True         # Add the required attribute
    })
)
    
    x_handle = forms.CharField(
    label='xname', 
    widget=forms.TextInput(attrs={
        'id': 'xname',
        'class': 'poppins-bold w-full bg-tranparent p-2 outline-none text-md border-[1.4px] border-gray-faded rounded-md focus:border-black text-xs',
        'placeholder': 'X handle',  # Add the placeholder attribute
        'required': True         # Add the required attribute
    })
)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email
    
    def clean_x_handle(self):
        x_handle = self.cleaned_data.get('x_handle')
        if CustomUser.objects.filter(x_handle=x_handle).exists():
            raise forms.ValidationError("This X account handle is already in use.")
        return x_handle