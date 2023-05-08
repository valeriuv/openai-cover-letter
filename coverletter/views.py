import openai
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from .forms import InputForm, ApplicationForm
from .forms import RegisterForm
from .app import generate_cover_letter, parse_pdf


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        print("request.POST: ", request.POST)
        print("request.FILES: ", request.FILES)
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company = form.cleaned_data['company']
            position = form.cleaned_data['position']
            description = form.cleaned_data['job_description']
            cv = request.FILES['cv']
            fs = FileSystemStorage() 
            fs.save(cv.name, cv)    # save the file to the MEDIA_ROOT

            if cv:
                text = parse_pdf(cv)
                cover_letter_text = generate_cover_letter(first_name, last_name, company, position, description, text)
            else:
                cover_letter_text = generate_cover_letter(first_name, last_name, company, description, position)
            context = {'cover_letter_text': cover_letter_text, 'form': form}
            form = InputForm()
        else:
            print("Form errors: ", form.errors)
    else:
        form = InputForm()
        context = {'form': form}
    
    return render(request, 'coverletter/index.html', context)



def application_list(request):
    return render(request, 'coverletter/application-list.html')


def application_create(request):

    if request.method == 'POST':
        print("request.POST: ", request.POST)
        print("request.FILES: ", request.FILES)
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.username
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            job_title = form.cleaned_data['job_title']
            job_description = form.cleaned_data['job_description']
            cv = request.FILES['cv']
            fs = FileSystemStorage() 
            fs.save(cv.name, cv)    # save the file to the MEDIA_ROOT

            if cv:
                text = parse_pdf(cv)
                cover_letter_text = generate_cover_letter(user.first_name, user.last_name, company, job_title, job_description, text)
            else:
                cover_letter_text = generate_cover_letter(user.first_name, user.last_name, company, job_title, job_description)
            context = {'cover_letter_text': cover_letter_text, 'form': form}
            form.save()
            form = ApplicationForm()
        else:
            print("Form errors: ", form.errors)
    else:
        form = ApplicationForm()
        context = {'form': form}

    return render(request, 'coverletter/application-form.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() #saving the new user to the database
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('index')
        else:
            print("Form is not valid")
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})