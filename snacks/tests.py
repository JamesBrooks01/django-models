from django.test import TestCase
from django.urls import reverse

class SnacksTest(TestCase):
  def test_list_status(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_list_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')

  # def test_list_page_context(self):
  #   url = reverse('snack_list')
  #   response = self.client.get(url)
  #   snacks = response.context['snack_list']
  #   self.assertEqual(len(snacks), 4)
  #   self.assertEqual(snacks[0].name, "Pumpkin Seeds")
  #   self.assertEqual(snacks[0].purchaser.name, "James")

  # def test_detail_page_status_code(self):
  #   url = reverse('snack_detail',args=(1,))
  #   response = self.client.get(url)
  #   self.assertEqual(response.status_code, 200)

  # def test_detail_page_template(self):
  #   url = reverse('snack_detail',args=(1,))
  #   response = self.client.get(url)
  #   self.assertTemplateUsed(response, 'snack_detail.html')
  #   self.assertTemplateUsed(response, 'base.html')

  # def test_detail_page_context(self):
  #     url = reverse('snack_detail',args=(1,))
  #     response = self.client.get(url)
  #     snack = response.context['snack']
  #     self.assertEqual(snack.name, "Pumpkin Seeds")
  #     self.assertEqual(snack.purchaser.name, "James")