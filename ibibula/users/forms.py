from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from main.models import Categories, Subcategories


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "telegram",
        )

    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    phone_number = forms.CharField()
    telegram = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "telegram",
            "image",
        )

    username = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    telegram = forms.CharField()
    image = forms.ImageField(required=False)



class ProductForm(forms.Form):
    productname = forms.CharField()
    price = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    category = forms.ChoiceField(choices=[(category.id, category.name) for category in Categories.objects.all()])
    subcategory = forms.ChoiceField(choices=[(subcategory.id, subcategory.name) for subcategory in Subcategories.objects.all()])

    def clean_category(self):
        category_id = self.cleaned_data['category']
        return Categories.objects.get(id=category_id)

    def clean_subcategory(self):
        subcategory_id = self.cleaned_data['subcategory']
        return Subcategories.objects.get(id=subcategory_id)

