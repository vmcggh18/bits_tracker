from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# import classes
from .models import Post, PostComment
from .forms import BlogPostForm, BlogCommentForm

# Create your views here.
def get_posts(request):
    """
    A view that returns a list of Posts published previously
    and renders them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})
    
def post_detail(request, pk):
    """
    Return a single post object based on the post ID and
    ender it to the 'postdetail.html' template. Or return 
    a 404 error if the post is not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def create_a_post(request):
    """  
    Create a view that allows us to add a post
    """
    if request.method == "POST":
        #create new form
        form = BlogPostForm(request.POST, request.FILES)
        #django checks if form is valid and saves if so
        if form.is_valid():
            if request.user.is_authenticated():
                form = form.save(commit=False)
                form.user=request.user
                form.save()
                return redirect(get_posts)
    #if not a post request return an empty form
    else:
        form = BlogPostForm()
    return render(request, "blogpostform.html", {'form': form})
 
def edit_a_post(request, pk):
    """ Return an existing form for edit """
    item = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_posts)
    else:
        #item is the instance that we want to construct the object from
        form = BlogPostForm(instance=item)
    return render(request, "blogpostform.html", {'form': form})
    
def add_comment_to_post(request, pk):
     """Add a comment to a ticket item"""
     post= get_object_or_404(Post, pk=pk)
     form = BlogCommentForm(request.POST)
     if request.method == "POST":
         if form.is_valid():
             if request.user.is_authenticated():
                 form = form.save(commit=False)
                 form.author = request.user
                 form.post = post
                 form.save()
                 return redirect(post_detail, pk)
     else:
        form = BlogCommentForm()
     return render(request, "blogcommentform.html", {'form': form})