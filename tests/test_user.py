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


