from django.shortcuts import render,  HttpResponse, redirect, reverse, get_object_or_404
from .models import Item, Votefor, Comment
from .forms import ItemForm, VoteforForm, CommentForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def get_issues_list(request):
    """ Render the ticket list """
    item=Item.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(item, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(request, "issues_list.html", {'items': items})

def create_an_item(request):
    """ Present a blank form to be filled in """
    if request.method == "POST":
        #create new form
        form = ItemForm(request.POST, request.FILES)
        #django checks if form is valid and saves if so
        if form.is_valid():
            if request.user.is_authenticated():
                form = form.save(commit=False)
                form.user=request.user
                form.save()
                return redirect(get_issues_list)
    #if not a post request return an empty form
    else:
        form = ItemForm()
    return render(request, "itemform.html", {'form': form})
    
#get item where primary key = id
def edit_an_item(request, id):
    """ Return an existing form for edit """
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_issues_list)
    else:
        #item is the instance that we want to construct the object from
        form = ItemForm(instance=item)
    return render(request, "editform.html", {'form': form})
    
def get_issue_detail(request,id):
    """ Return the ticket issue detail view"""
    item = get_object_or_404(Item, pk=id)
    user = request.user
    upvotes = Votefor.objects.filter(item=item, user=user).count()
    comments = Comment.objects.all()
    return render(request, "issue_detail.html", {'item' : item, 'upvotes' : upvotes, 'comments' : comments})
    
def cast_an_upvote(request, id):
    """ Free vote up a bug"""
    item = get_object_or_404(Item, id=id)
    user = request.user
    if Votefor.objects.filter(item=item, user_id=request.user.id).exists():
        messages.success(request, "Sorry you have already voted!")
        return redirect(get_issues_list)  
    else:
        item.upvotes += 1
        item.save()
        Votefor.objects.get_or_create(user=user, item=item)
        messages.success(request, "Your Bug has been upvoted!")
        return redirect(get_issues_list)    
            
def add_comment_to_issue(request, id):
     """Add a comment to a ticket item"""
     item= get_object_or_404(Item, pk=id)
     form = CommentForm(request.POST)
     if request.method == "POST":
         if item.category =="Bug":
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.item = item
                form.save()
                return redirect(get_issue_detail, id)
         else:
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.item = item
                form.save()
                return redirect(get_feature_detail, id)
     else:
        form = CommentForm()
     return render(request, "issue_commentform.html", {'form': form})
     
# def get_feature_detail(request,id):
#     """ Get the feature detail """
#     item = get_object_or_404(Item, pk=id)
#     user = request.user
#     upvotes = Votefor.objects.filter(item=item, user=user).count()
#     comments = Comment.objects.all()
#     return render(request, "feature_detail.html", {'item' : item, 'upvotes' : upvotes, 'comments' : comments})




        