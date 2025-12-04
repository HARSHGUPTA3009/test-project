from django.test import TestCase
from core.models import Bank

class BankTestCase(TestCase):
    def setUp(self):
        Bank.objects.create(id=999, name="Test Bank")

    def test_bank_created(self):
        bank = Bank.objects.get(id=999)
        self.assertEqual(bank.name, "Test Bank")
