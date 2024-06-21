from django.db import DataError, IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User 
""""
Define a new class for the 'User' model test case
"""
class UserTestCase(TestCase):
    
    def setUp(self):
        User.objects.create(
             first_name="John", 
             last_name="Doe", 
             email="johndoe@email.com", 
             password="password"
        )
"""
Define a new method for the 'User' model test case to test the user's information
"""                            
def test_user(self):
        user = User.objects.get(first_name="John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "johndoe@email.com")
        self.assertEqual(user.password, "password")

def test_email_field_cannot_be_blank(self):
        with self.assertRaises(ValueError):
            User.objects.create(
                first_name="Jane", 
                last_name="Doe", 
                email="", 
                password="password"
            )

def test_password_field_cannot_be_blank(self):
        with self.assertRaises(ValueError):
            User.objects.create(
                first_name="Jane", 
                last_name="Doe", 
                email="janedoe@gmail.com",
                password=""
            )

def test_first_name_and_last_name_cannot_be_blank(self):
        with self.assertRaises(ValueError):
            User.objects.create(
                first_name="", 
                last_name="Doe", 
                email="janedoe@email.com",
                password="password"
            )

def test_max_length_exceeded(self):
        with self.assertRaises(DataError):
            User.objects.create(
                first_name="J" * 201,
                last_name="Doe",
                email="johndoe@email.com",
                password="password"
            )

def test_email_uniqueness(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(
                first_name="Jane", 
                last_name="Doe", 
                email="johndoe@email.com",
                password="password"
            )      
