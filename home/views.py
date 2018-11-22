from django.shortcuts import render, redirect, reverse
from issues_list.models import Item

# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')
    
def get_about(request):
    """Return the about.html file"""
    return render(request,  'about.html')
    
def get_activities_summary(request):
    """Return the activities summary page"""
    bug_pending = Item.objects.filter(status='Pending').filter(category='Bug').count()
    bug_ongoing = Item.objects.filter(status='Ongoing').filter(category='Bug').count()
    bug_completed = Item.objects.filter(status='Completed').filter(category='Bug').count()
    total_bug = bug_pending + bug_ongoing + bug_completed
    feature_pending = Item.objects.filter(status='Pending').filter(category='Feature').count()
    feature_ongoing = Item.objects.filter(status='Ongoing').filter(category='Feature').count()
    feature_completed = Item.objects.filter(status='Completed').filter(category='Feature').count()
    total_feature = feature_pending + feature_ongoing + feature_completed
    return render(request, 'activities.html', {'bug_pending': bug_pending, 'bug_ongoing':bug_ongoing, 'bug_completed':bug_completed, 'feature_pending':feature_pending, 'feature_ongoing' :feature_ongoing, 'feature_completed':feature_completed, 'total_bug':total_bug, 'total_feature': total_feature})

def get_documentation(request):
    return render(request,  'documentation.html')