# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from custom_manager.models import Item


class CustomQuerySetTestCase(TestCase):
    fixtures = ['test_data.json']

    def test_pseudo_delete(self):
        with_first_item = Item.objects.filter(pk=1)
        self.assertTrue(with_first_item[0].active)
        upd_count = with_first_item.delete()
        self.assertEqual(upd_count, 1)
        self.assertTrue(not with_first_item[0].active)

        all_active_count = 14
        upd_count = Item.objects.filter(active=True).delete()
        self.assertEqual(all_active_count, upd_count)
        self.assertEqual(Item.objects.filter(active=True).count(), 0)

    def test_real_delete(self):
        self.assertEqual(Item.objects.filter(pk=1).count(), 1)
        Item.objects.filter(pk=1).delete_real()
        self.assertEqual(Item.objects.filter(pk=1).count(), 0)

        all_count = 14
        del_res = Item.objects.all().delete_real()
        self.assertEqual(del_res[0], all_count)
        self.assertEqual(Item.objects.count(), 0)
