from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from articles.models import Article
from market.models import Product


class SiteSmokeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='strong-test-password',
        )
        self.article = Article.objects.create(
            title='Test Article',
            author=self.user,
            content='This is a test article.',
        )
        self.product = Product.objects.create(
            product_name='Test Product',
            details='This is a test product.',
            category='Demo',
            price='12.50',
        )

    def test_public_pages_render(self):
        urls = [
            reverse('home'),
            reverse('about'),
            reverse('contact'),
            reverse('articles_list'),
            reverse('article_detail', args=[self.article.pk]),
            reverse('product_list'),
            reverse('product_detail', args=[self.product.pk]),
            reverse('cart'),
            reverse('checkout'),
            reverse('login'),
            reverse('register'),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response['Location'])

    def test_logout_requires_post(self):
        self.client.login(username='tester', password='strong-test-password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 405)

        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
