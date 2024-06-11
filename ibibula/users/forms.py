from django import forms
from django.utils.text import slugify
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from main.models import Categories, Services, Subcategories


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
    name = forms.CharField()
    price = forms.DecimalField(decimal_places=2)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    category = forms.ChoiceField()
    subcategory = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(category.id, category.name) for category in Categories.objects.all()]
        self.fields['subcategory'].choices = [(subcategory.id, subcategory.name) for subcategory in Subcategories.objects.all()]

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Price must be a valid decimal number.")
        return price

    def clean_category(self):
        category_id = self.cleaned_data['category']
        return Categories.objects.get(id=category_id)

    def clean_subcategory(self):
        subcategory_id = self.cleaned_data['subcategory']
        return Subcategories.objects.get(id=subcategory_id)

    def generate_unique_slug(self, name):
        slug = slugify(name)
        unique_slug = slug
        num = 1
        while Services.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

    def save(self):
        product = Services(
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
            description=self.cleaned_data['description'],
            image=self.cleaned_data['image'],
            category=self.cleaned_data['category'],
            subcategory=self.cleaned_data['subcategory'],
            slug=self.generate_unique_slug(self.cleaned_data['name']),
        )
        product.save()
        return product







