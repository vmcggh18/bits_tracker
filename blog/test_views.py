from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Post, PostComment
from .forms import BlogPostForm, BlogCommentForm
from django.core.urlresolvers import reverse

class TestBlogViews(TestCase):

    def test_get_posts(self):
        #use built in helper to fake an url request
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogposts.html")
        
    def test_get_post_detail(self):
        post = Post(title="Create a Test")
        post.save()
        page = self.client.get("/blog/{0}/".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "postdetail.html")   
        
    def test_create_a_post(self):
        page = self.client.get("/blog/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
        
    def test_edit_post_detail(self):
        post = Post(title="Create a Test")
        post.save()
        page = self.client.get("/blog/{0}/edit/".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
        
    def test_add_comment_to_post(self):
        post = Post(title="Create a Test")
        post.save()
        page = self.client.get("/blog/post_comment/{0}/".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogcommentform.html")
        
    def test_get_edit_page_for_post_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        
    def test_post_form_is_valid(self):
        form = BlogPostForm({'Title': 'Create Tests'})
        page = self.client.get("/blog/")
        self.assertFalse(form.is_valid())
        self.assertTemplateUsed(page, "blogposts.html")   
    def test_blog_add_form_is_loaded(self):
        url = reverse('new_post')
        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        
    def test_return_get_posts_url(self):
        response = self.client.get(reverse('get_posts'))
        self.assertEqual(response.status_code, 200)
        
    def setUp(self):
        self.post = Post.objects.create(title="newpost", content="hello")
        
    def test_BlogPostForm_valid(self):
        form = BlogPostForm(data={'title': "newpost", 'content': "hello"})
        form.save()
        self.assertTrue(form.is_valid())
   