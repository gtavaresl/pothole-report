from django import forms

from .models import Report

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('resolved', 'street', 'number', 'district', 'description',)