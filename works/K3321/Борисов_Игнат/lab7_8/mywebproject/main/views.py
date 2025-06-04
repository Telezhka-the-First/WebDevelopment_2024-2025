from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def feedback(request):
    error = ""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        return redirect('home')###
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка: форма неверна"

    form = Feedback()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/feedback.html', data)