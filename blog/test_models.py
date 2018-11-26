from django.test import TestCase
from .models import Post, PostComment

class TestBlogModel(TestCase):
    def test_can_create_an_item_with_a_title_and_content(self):
        post = Post(title="Create a Test", content=True)
        post.save()
        self.assertEqual(post.title, "Create a Test")
        self.assertTrue(post.content)
    # def test_text_defaults_to_False(self):
    #     post = PostComment(text="Create a Test")
    #     post.save()
    #     self.assertEqual(post.text, "Create a Test")
    #     self.assertFalse(post.text)
    def test_post_as_a_string(self):
        post = Post(title="Create a Test")
        self.assertEqual("Create a Test", str(post))
    def test_postcomment_as_a_string(self):
        post = PostComment(text="Create a Test")
        self.assertEqual("Create a Test", str(post))