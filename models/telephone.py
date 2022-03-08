from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Telephone(models.Model):
    _name = "gestion_cours.telephone"
    _description = "Numero de telephone"

    
    telephone = fields.Integer(
        string="Telephone",
        required=True,
    )
    
    @api.constrains('num_bureau')
    def _check_telephone(self):
        for record in self:
            if(record.num_bureau!=10):
                raise ValidationError("Le numero doit etre de longueur 10")
            

    
    
    
