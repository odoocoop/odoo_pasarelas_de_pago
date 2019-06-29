# -*- coding: utf-8 -*-

{
    'name': 'Flow Payment Acquirer',
    'category': 'Accounting',
    'author': 'Daniel Santibáñez Polanco',
    'summary': 'Payment Acquirer: Flow Implementation',
    'website': 'https://globalresponse.cl',
    'version': "0.5.4",
    'description': """Flow Payment Acquirer""",
    'depends': ['payment'],
    'external_dependencies': {
            'python': [
                'urllib3',
            ],
    },
    'data': [
        'views/flow.xml',
        'views/payment_acquirer.xml',
        'views/payment_transaction.xml',
        'data/flow.xml',
    ],
    'installable': True,
    'application': True,
}
