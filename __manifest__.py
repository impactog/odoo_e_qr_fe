{
    'name': 'odoo_e_qr_fe',
    'version': '1.0',
    'category': 'l10n_ar',
    'summary': 'Codigo QR para factura electronica AFIP Argentina',
    'depends': ['account','l10n_ar','l10n_ar_edi'],
    'data': [
        'afip_view.xml',
        'report_template.xml'
    ],
    'demo': [
        ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
