from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from .models import User


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'success': 'Form submitted successfully', 'form': form})
    else:
        form = UserForm()
        return render(request, 'index.html', {'form': form})


