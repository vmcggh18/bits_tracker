from django.shortcuts import render,  HttpResponse, redirect, reverse, get_object_or_404, HttpResponseRedirect
from .models import Item, Votefor, Comment
from .forms import ItemForm, VoteforForm, CommentForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
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
    
    #return the ticket detail view
def get_issue_detail(request,id):
    if Item.objects.filter(id=id, user_id=request.user.id).exists():

        # return render(request, 'issue_detail.html', {
        #     'error_message': "Sorry, but you have already voted."
        # })
        return HttpResponse( "Sorry, but you have already voted.")
    else:
        item = get_object_or_404(Item, pk=id)
        user = request.user
        #votefor = Votefor.objects.filter(item=item).count() 
        upvotes = Votefor.objects.filter(item=item, user=user).count()
        return render(request, "issue_detail.html", {'item' : item, 'upvotes' : upvotes})
    
    #upvote an issue item
def cast_an_upvote(request, id):
    """Vote up a feature or bug"""
    item = get_object_or_404(Item, id=id)
    if Votefor.objects.filter(id=id, user_id=request.user.id).exists():
         return HttpResponse("Sorry, but you have already voted!")
        # return render(request, 'issue_detail.html', {'item': item, 'error_message': "Sorry, but you have already voted."})
    else:
        item = get_object_or_404(Item, id=id)
    
    #votefor = Votefor(item=item, user=request.user)
        if item.category == 'Feature':
            item.upvotes += 1
            item.save()
            votefor= Votefor(user=request.user, item=item)
            #votefor.save()
      # Confirm upvote
            #messages.success(request, "Upvote has been added to Payments!")
            return HttpResponse("Upvote has been added to Payments")
            #return redirect('fee_form',id)
            #free vote a bug
        else:
            item.upvotes += 1
            item.save()
            votefor= Votefor(user=request.user, item=item)
           #votefor.save()
            # Confirm bug has been upvoted
            #return HttpResponse("Your Bug has been upvoted!")
            messages.success(request, "Your Bug has been upvoted!")
            return redirect('issue_detail', id)
            
def add_comment_to_issue(request, id):
     comment_item = get_object_or_404(Item, pk=id)
     form = CommentForm(request.POST)
     author = request.user
     if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = author
            form.item = comment_item
            form.save()
            return redirect(get_issue_detail, id)
     else:
        form = CommentForm()
     return render(request, "issue_commentform.html", {'form': form})
        
    
        




        