from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})
