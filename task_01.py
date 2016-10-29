#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def sum_orders(customers, orders):
    """This function does some dictionary culculations.

    Args:
        customers(dict): Just a random dictionary of personal information.
        orders(dict): Just a random dictionary of orders and it amount.

    Returns:
        dict: Combined two datasets.

    Examples:

        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
                     3: {'customer_id': 2, 'total': 10},
                     4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                         3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers = CUSTOMERS, orders = ORDERS)
        {2: {'orders': 2, 'total': 20, 'name': 'Person One', 'email': 'email@one
        .com'},
        3: {'orders': 1, 'total': 15, 'name': 'Person Two', 'email': 'email@two.
        com'}}
    """
    total = 0
    order_sum = 0
    my_dict = {}

    for customer_id, value1 in customers.iteritems():
        for _, value2 in orders.iteritems():
            if customer_id == value2['customer_id']:
                order_sum += 1
                total += value2['total']
            my_dict[customer_id] = {'name': value1['name'],
                                    'email': value1['email'],
                                    'orders': order_sum,
                                    'total': total}

        total = 0
        order_sum = 0

    return my_dict
