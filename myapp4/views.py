
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import User


import logging


logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # do something with data
            logger.info(f'Got: {name} {email} {age}')
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST)
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # do something
            logger.info(f'Got: {form.cleaned_data=}')
    else:
        # form = ManyFieldsForm()
        form = ManyFieldsFormWidget()

    return render(request, 'myapp4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Got {name}, {email}, {age}')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранен'
    else:
        form = UserForm()
        message = 'Заполните поле'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})

