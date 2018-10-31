from django.shortcuts import render,  HttpResponse
from .models import Item
from django.contrib.auth.models import User, Group, Permission, ContentType
# Create your views here.

def get_issues_list(request):
    results=Item.objects.all()
    return render(request, "issues_list.html", {'items': results})#,'ordering': ordering})
def grant_permissions(request):
    user = request.user
    content_type = ContentType.objects.get_for_model(Item)
    permission = Permission.objects.get(
    codename='add comments',
    content_type=content_type,
)
    user.user_permissions.add(permission)