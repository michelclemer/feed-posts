from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeUrlsTest(TestCase):
    def test_recipe_home_url_is_corret(self):
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipe_category_url_is_corret(self):
        url = reverse("recipes:category", kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipe_recipe_url_is_corret(self):
        url = reverse("recipes:recipe", kwargs={"id": 1})
        self.assertEqual(url, "/recipes/1/")
