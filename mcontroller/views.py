from django.shortcuts import render, redirect
from mcontroller.info import Info
from mcontroller.forms import SubmitMasturbationForm


def home(request):
    info = Info()

    context = {
        'info': info,
    }

    return render(request, 'home.html', context)


def submit_masturbation(request):
    if request.method == 'POST':
        form = SubmitMasturbationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubmitMasturbationForm()
    return render(request, 'submit.html', {'form': form})