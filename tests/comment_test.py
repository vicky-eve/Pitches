from app.models import User,Comment
from app import db
import unittest

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.user_Victoria = User(username = 'victoria',password = 'awuor', email = 'vicky@gmail.com')
        self.new_comment = Comment("Good one",pitch_id = 1234,user = self.user_Victoria )
        
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"Good one")
        self.assertEquals(self.new_comment.pitch_id,1234)
        self.assertEquals(self.new_comment.user,self.user_Victoria)
        
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)