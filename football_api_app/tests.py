from django.contrib.auth import get_user_model
from django.db.models import manager
from django.test import TestCase
from .models import Football

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_Football = Football.objects.create(
            manager = test_user,
            player_name = 'ayman',
            position = 'modifier'
        )
        test_Football.save()

    def test_blog_content(self):
        football = Football.objects.get(id=1)
        actual_manager = str(football.manager)
        actual_name = str(football.player_name)
        actual_position = str(football.position)
        self.assertEqual(actual_manager, 'testuser')
        self.assertEqual(actual_name, 'ayman')
        self.assertEqual(actual_position, 'modifier')