from django.test import TestCase
from members.models import Member
import logging
from django.contrib.auth.models import User
from django.urls import reverse

logger = logging.getLogger(__name__)

# Create your tests here.
class memberModelTest(TestCase):
    def test_create_member(self):
        # Creating a new book instance
        book = Member.objects.create(firstname="Test Book", lastname="Author Test")
        # book.phone = 123456
        # id = [1]
        # Fetch the book from the database
        fetched_member = Member.objects.get(id=book.id)
        fetched_member.phone = 123456

        # Check if the values match
        self.assertEqual(fetched_member.firstname, "Test Book")
        # logger.error("Your debug information here")
        self.assertEqual(fetched_member.lastname, "Author Test")
        self.assertEqual(fetched_member.phone, 123456)

class UserAuthTest(TestCase):
    def setUp(self):
        # Create a user for testing purposes
        self.user = User.objects.create_user('chath', 'test@example.com', 'abc123')

    def test_create_user(self):
        # Check if user is created
        self.assertEqual(self.user.username, 'chath')
        self.assertTrue(self.user.check_password('abc123'))

    def test_login(self):
        # Log in the user
        login = self.client.login(username='chath', password='abc123')
        self.assertTrue(login)

        # Optionally, you can also check for the response after login
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # Log in the user
        self.client.login(username='chath', password='abc123')

        # Log out the user
        self.client.logout()

        # Check if user is logged out (e.g., by accessing a restricted page)
        response = self.client.get(reverse('main'))
        self.assertNotEqual(response.status_code, 201)  # e.g., should redirect to login page
