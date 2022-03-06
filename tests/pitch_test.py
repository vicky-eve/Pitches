from app.models import Pitch,User
from app import db
import unittest

class PitchTest(unittest.TestCase):

    def setUp(self):
        self.user_Victoria = User(username = 'victoria',password = 'awuor', email = 'vicky@gmail.com')
        self.new_pitch = Pitch(title="Promote me",word = "Better pay better service delivery",category="Promotion",user = self.user_Victoria )
            
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
            
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,"Money")
        self.assertEquals(self.new_pitch.word,"Better pay better service delivery")
        self.assertEquals(self.new_pitch.category,"Promotion")
        self.assertEquals(self.new_pitch.user,self.user_Victoria)
        
    def test_save_pitch(self):
        self.new_pitch.save_review()
        self.assertTrue(len(Pitch.query.all())>0)