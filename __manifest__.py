# -*- coding: utf-8 -*-
{
    'name': "Leucotec",

    'summary': """
        Modulos completos desarrollados para Leucotec""",

    'description': """
       Modulo de visitas para los vendedores de Leucotec
       
       Catalogo de productos
       
       Modulo para levantar pedidos

	Complemento de CRM
    """,

    'author': "Sitecnet.com",
    'website': "http://www.sitecnet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '2',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts', 'base_setup', 'web_google_maps'],

    # always loaded
    'data': [
        'security/leucotec_security.xml',
        'security/ir.model.access.csv',
        'views/catalogo.xml',
        'views/pedidos.xml',
        'views/herencias.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}