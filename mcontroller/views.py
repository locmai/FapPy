from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mcontroller.info import Info
from mcontroller.forms import MasturbationForm
from django.contrib.auth.models import User
from mcontroller.constants import METRICS_CHECK
from mcontroller.data_handler import DataHandler
import csv


def home(request):
    if request.user.is_authenticated:
        info = Info(request.user)
        context = {
            'info': info,
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')


def submit_masturbation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MasturbationForm(request.POST)
            if form.is_valid():
                m = form.save(commit=False)
                m.m_user = request.user
                m.save()
                return redirect('home')
        else:
            form = MasturbationForm()
        return render(request, 'submit.html', {'form': form})
    else:
        raise PermissionDenied


def export_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)

            data = DataHandler.csv_data_handler_self(request.user)
            for elem in data:
                writer.writerow(elem)
            return response

        users = User.objects.all()
        context = {
            'users': users,
            'checkbox_metrics': METRICS_CHECK
        }
        return render(request, 'data.html', context=context)
    else:
        raise PermissionDenied


def about(request):
    return render(request, 'about.html')
