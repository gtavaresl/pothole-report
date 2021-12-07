from django.shortcuts import render

def report_list(request):
    return render(request, 'report/report_list.html', {})
