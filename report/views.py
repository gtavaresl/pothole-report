from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Report

def report_list(request): 
    reports = Report.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'report/report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(pk=pk) 
    return render(request, 'report/report_detail.html', {'report': report})
