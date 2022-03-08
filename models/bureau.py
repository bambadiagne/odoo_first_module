from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Bureau(models.Model):
    _name = "gestion_cours.bureau"
    _description = "Un bureau"

    
    num_bureau = fields.Char(
        string="Numero Bureau",
        required=True,
    )
    
    centre=fields.Selection(selection=[
    ('Royallieu','R'),
    ('Benjamin Franklin','BF'),
    ('Pierre Guillaumat','PG')
    ],required=True)
    batiment=fields.Char(string="Bâtiment",size=1,required=True,)
    cours_id = fields.One2many(
        "gestion_cours.intervenant",
        "bureau_id",
        string="Intervenant",
    )
    @api.constrains('batiment')
    def _check_batiment(self):
        for record in self:
            if(not record.batiment.isalpha()):
                raise ValidationError("Le batiment est une lettre A-Z")
        
    @api.constrains('num_bureau')
    def _check_num_bureau(self):
        for record in self:
            if(record.num_bureau):
                if(not str(record.num_bureau).isdigit()):
                    raise ValidationError("Le numero du bureau doit etre composé de chiffres")
                if(int(record.num_bureau)<0):
                    raise ValidationError("Le numero du bureau doit etre positif")
                elif(int(record.num_bureau) >=1000):
                    raise ValidationError("Le numero du bureau doit etre inferieur à 1000")


    
    
    
