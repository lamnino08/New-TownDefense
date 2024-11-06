from django.test import TestCase
from .models import Table
from .service import TableService

class TableServiceTests(TestCase):
    def setUp(self):
        self.table1 = Table.objects.create(table_number=1, is_available=True, capacity=4)
        self.table2 = Table.objects.create(table_number=2, is_available=False, capacity=6)

    def test_get_all_tables(self):
        tables = TableService.get_all_tables()
        self.assertEqual(len(tables), 2)

    def test_reserve_table(self):
        TableService.reserve_table(self.table1.id)
        self.table1.refresh_from_db()
        self.assertFalse(self.table1.is_available)

    def test_release_table(self):
        TableService.release_table(self.table2.id)
        self.table2.refresh_from_db()
        self.assertTrue(self.table2.is_available)

    def test_update_table_capacity(self):
        TableService.update_table_capacity(self.table1.id, 10)
        self.table1.refresh_from_db()
        self.assertEqual(self.table1.capacity, 10)
