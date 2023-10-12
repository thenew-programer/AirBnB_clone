#!/usr/bin/env python3
"""Unittest for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser class for testring User class"""

    def setUp(self):
        """Set up User for testing"""
        self.user = User()
        self.user.first_name = "youssef"
        self.user.last_name = "bouryal"
        self.user.email = "airbnb_clone@alx.com"
        self.user.password = "1234password"

    def test_user_instance(self):
        """Test user instance"""
        self.assertIsInstance(self.user, User)

    def test_user_email(self):
        """Test user email"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(self.user.email, "airbnb_clone@alx.com")

    def test_user_password(self):
        """Test user password"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(self.user.password, "1234password")

    def test_user_first_name(self):
        """Test user first_name"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(self.user.first_name, "youssef")

    def test_user_last_name(self):
        """Test user last_name """
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(self.user.last_name, "bouryal")
