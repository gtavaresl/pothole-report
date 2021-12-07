from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import Report
from .forms import ReportForm

def report_list(request): 
    reports = Report.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 
    return render(request, 'report/report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk) 
    return render(request, 'report/report_detail.html', {'report': report})

def report_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.publish(request.user)
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm()
    return render(request, 'report/report_edit.html', {'form': form})

def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.publish(request.user)
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm(instance=report)
    return render(request, 'report/report_edit.html', {'form': form})
