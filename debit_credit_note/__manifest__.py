# -*- encoding: utf-8 -*-
{
    'name': 'Notas de Débito Crédito',
    'version': '10.0.0.1.0',
    'author': "Miguel Angel",
    'maintainer': 'sapex.miguel@gmail.com',
    'license': 'AGPL-3',
    'category': 'Account',
    'summary': 'Accounting',
    'depends': ['sale', 'purchase', 'account'],
    'description': """
Contabilidad: Notas de Debito y Credito
=============================================================================
- Notas de Débito credito
        """,
    'data': [
        'data/journal_data.xml',
        'wizards/account_invoice_refund_view.xml',
        'wizards/account_invoice_debit_view.xml',
        'views/account_invoice_view.xml',
        'views/account_view.xml',
    ],
    'installable': True,
}
