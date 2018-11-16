from django.shortcuts import render
from django.http import JsonResponse
from issues_list.models import Item
# Create your views here.

def charts(request):
     return render(request, "graphs.html")
    
def chart_bugs(request):
    data = list(Item.objects.filter(category='Bug').values('category','status'))
    return JsonResponse(data, safe=False)
def chart_features(request):
    data = list(Item.objects.filter(category='Feature').values('category','status'))
    return JsonResponse(data, safe=False)
    
    