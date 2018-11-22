from django.shortcuts import render
from django.http import JsonResponse
from issues_list.models import Item
from datetime import datetime, timedelta
# Create your views here.

def charts(request):
     return render(request, "graphs.html")
    
def chart_bugs(request):
    """ Get Bug related data for activities chart """
    data = list(Item.objects.filter(category='Bug').values('category','status'))
    return JsonResponse(data, safe=False)
    
def chart_features(request):
    """ Get Feature related data for activities chart """
    data = list(Item.objects.filter(category='Feature').values('category','status'))
    return JsonResponse(data, safe=False)
    
def chart_issues(request):
    """ Get Feature and Bug related data for activities chart """
    data = list(Item.objects.values('category'))
    return JsonResponse(data, safe=False)

def get_time_spent(request):
    """ Get days spent data for all ongoing and completed bugs and features """
    data = list(Item.objects.values('status', 'category', 'created_date','completed_date', 'assigned_date', 'upvotes', 'fee'))
    return JsonResponse(data, safe=False)
    
