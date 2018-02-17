from django.http import HttpResponse
from django.shortcuts import render, redirect
from mcontroller.info import Info
from mcontroller.forms import SubmitMasturbationForm
from django.contrib.auth.models import User
from mcontroller.constants import METRICS_CHECK
from mcontroller.data_handler import DataHandler
import csv

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


def export_data(request):
    # Currently will get all the user information, need to update query and permission after update model
    if request.method == 'POST':
        #checked_metrics = request.POST.getlist('checked_metrics')
        #header_row = [metrics for metrics in checked_metrics]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        writer = csv.writer(response)
        #writer.writerow(header_row)
        #data = DataHandler.csv_data_handler(header_row)
        data = DataHandler.csv_data_handler()
        for elem in data:
            writer.writerow(elem)
        return response

    users = User.objects.all()
    context = {
        'users': users,
        'checkbox_metrics': METRICS_CHECK
    }
    return render(request, 'data.html', context=context)


def about(request):
    return render(request,'about.html')