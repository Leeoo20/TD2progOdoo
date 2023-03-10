{
    "name": "Gestion des étudiants",
    "version": "0.4",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants dans Odoo v14""",
    "author": "Vernier",
    "data": ["views/students_views.xml",
             "views/training_views.xml",
             "views/mark_views.xml",

       #      "data/students_training_data.xml",
        #     "data/students_student_data.xml",
         #    "data/students_mark_data.xml",
            ],

    "depends": ["base"],
    "installable": True,
    "Auto_install": False,
}
