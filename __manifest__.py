# -*- coding: utf-8 -*-
{
    'name': "gestion_cours",

    'summary': """
        Resumé de mon module gestion_cours
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Bamba Diagne",
    'website': "http://www.tdsi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "views/cours_views.xml",
        "views/intervenant_views.xml",
        "views/bureau_views.xml",
        "views/specialite_views.xml",
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
