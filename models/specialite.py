from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Specialite(models.Model):
    _name = "gestion_cours.specialite"
    _description = "Une specialit√©"

    
    specialite = fields.Char(
        string="Specialit√©",
        required=True,
    )
    
    domaine=fields.Char(
        string='Domaine',
        required=True,

    )
