from django import forms
from .models import User
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = User.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = User.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunately we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-username',
                   'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Firstname', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    phone_number = forms.CharField(
        label='Phone', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Phone', 'id': 'form-phonenumber'}))

    address_line_1 = forms.CharField(
        label='Address1', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Address1', 'id': 'form-address_line_1'}))

    address_line_2 = forms.CharField(
        label='Address2', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Address2', 'id': 'form-address_line_2'}))

    town_city = forms.CharField(
        label='City', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'City', 'id': 'form-town_city'}))

    country = forms.CharField(
        label='Country', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Country', 'id': 'form-country'}))

    postcode = forms.CharField(
        label='ZipCode', min_length=0, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'ZipCode', 'id': 'form-postcode'}))

    class Meta:
        model = User
        fields = ('email', 'user_name', 'first_name', 'phone_number', 'address_line_1', 'address_line_2', 'town_city', 'country', 'postcode')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['phone_number'].required = False
        self.fields['address_line_1'].required = False
        self.fields['address_line_2'].required = False
        self.fields['town_city'].required = False
        self.fields['country'].required = False


class ViewProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'user_name', 'email', 'first_name', 'phone_number', 'address_line_1', 'address_line_2', 'town_city',
            'country')
