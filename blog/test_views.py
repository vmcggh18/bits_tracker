from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Post, PostComment

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
    