from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Specialite(models.Model):
    _name = "gestion_cours.specialite"
    _description = "Une specialité"

    
    specialite = fields.Char(
        string="Specialité",
        required=True,
    )
    
    domaine=fields.Char(
        string='Domaine',
        required=True,

    )
