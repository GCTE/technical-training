{
    "name": "Estate",  # The name that will appear in the App list
    "version": "18.0.1.1.6",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [

    ],
    "installable": True,
    'license': 'LGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'view/estate_property_views.xml',
        'view/estate_property_type_views.xml',
        'view/estate_form.xml',
        'view/estate_list.xml',
        'view/estate_search.xml',
        'view/estate_menus.xml',
    ],
}