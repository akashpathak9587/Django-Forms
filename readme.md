# Handling file inputs and Creating Modelform in Django

This guide will walk you through setting up static and media file handling in your Django project, as well as creating and using ModelForms.

## Settings Configuration

Add the following settings to your `settings.py` file to configure static and media file handling:

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files (Uploads)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Creating a ModelForm

### 1. Create `forms.py` in Your App

Inside your Django app, create a file named `forms.py`.

### 2. Import Required Modules

Inside `forms.py`, import the necessary modules to create a ModelForm.

```python
from django import forms
from django.forms import ModelForm
from .models import User
```

### 3. Create ModelForm Classes

Define the ModelForm classes inside `forms.py`.

```python
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'country', 'password', 'profile_pic', 'resume', 'mobile_No', 'favorite_color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'country': forms.Select(choices=country, attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'mobile_No': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'favorite_color': forms.Select(choices=colors, attrs={'class': 'form-control'}),
        }
```

### 4. Using ModelForms in Views

In your views, import the forms and pass them to your template for rendering.

```python
from django.shortcuts import render
from .forms import UserForm

def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL or render a success template
    else:
        form = UserForm()

    return render(request, 'template_name.html', {'form': form})
```

### 5. Render the Form in a Template

In your template (e.g., `template_name.html`), render the form as follows:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>User Form</title>
  </head>
  <body>
    <h1>Create User</h1>
    <form method="post">
      {% csrf_token %} {{ form.as_p }}
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
```

## Conclusion

By following these steps, you have configured static and media file handling in your Django project, created a ModelForm, and rendered it in a template. Adjust the configurations and form fields as needed for your project requirements.
