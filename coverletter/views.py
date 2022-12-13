import openai
from django.shortcuts import render
from . app import generate_cover_letter
from . forms import InputForm

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company = form.cleaned_data['company']
            position = form.cleaned_data['position']
            cover_letter_text = generate_cover_letter(first_name, last_name, company, position)
            context = {'cover_letter_text': cover_letter_text, 'form': form}
            form = InputForm()
    else:
        form = InputForm()
        context = {'form': form}
    
    return render(request, 'coverletter/index.html', context)