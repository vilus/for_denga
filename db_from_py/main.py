# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import sqlite3
from contextlib import closing


"""
Print all products (category_name, product_name, price) from tables:
Category['id', 'name'] and Products['id', ('category_id', FK(Category), 'name', 'price']
Implemented for [sqlite3, ]
ave PEP-249
"""


def get_conn(*args, **kwargs):
    return sqlite3.connect(*args, **kwargs)


def get_all_products(_conn, _cursor):
    query = '''
            SELECT "shop_category"."name", "shop_product"."name", "shop_product"."price" 
            FROM "shop_product" LEFT JOIN "shop_category" ON 
            ("shop_product"."category_id" = "shop_category"."id");
    '''
    _cursor.execute(query)
    return _cursor.fetchall()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='db.sqlite3')
    args = parser.parse_args()

    with closing(get_conn(args.file)) as conn, closing(conn.cursor()) as cursor:
        for p in get_all_products(conn, cursor):
            print('{0:<24} {1:<24} {2:<12}'.format(*p))
