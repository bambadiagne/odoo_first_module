from datetime import datetime
from odoo.exceptions import ValidationError

from odoo import models, fields, api


class Intervenant(models.Model):
    _name = "gestion_cours.intervenant"
    _description = "Un intervenant"

    nom = fields.Char(
        string="Nom",
        required=True,
    )
    prenom = fields.Char(
        string="Prénom",
        required=True,
    )

    date = fields.Date(string="Date de Naissance")
    age = fields.Integer(string="Age", compute="_compute_age")
    telephone1 = fields.Char(
        string="Telephone",
        required=True,
    )
    telephone2 = fields.Char(
        string="Telephone 2",
    )
    telephone3 = fields.Char(
        string="Telephone 3",
    )

    @api.constrains('telephone1', 'telephone2', 'telephone3')
    def _check_telephone(self):
        for record in self:
                
            if(record.telephone1):
                if(not str(record.telephone1).isdigit()):
                    raise ValidationError(
                        "Le numero doit etre composé de chiffres")
                if(len(str(record.telephone1)) != 10):
                    raise ValidationError(
                            "Le numero doit etre de longueur 10")
            if(record.telephone2):
                if( not str(record.telephone2).isdigit()):
                    raise ValidationError(
                        "Le numero doit etre composé de chiffres")
                if(len(str(record.telephone2)) != 10):
                    raise ValidationError(
                            "Le numero doit etre de longueur 10")
            if(record.telephone3):
                if(not str(record.telephone3).isdigit()):
                    raise ValidationError(
                        "Le numero doit etre composé de chiffres")
                if(len(str(record.telephone3)) != 10):
                    raise ValidationError(
                            "Le numero doit etre de longueur 10")

    cours_id = fields.One2many(
        "gestion_cours.cours",
        "intervenant_id",
        string="Cours",
    )
    bureau_id = fields.Many2one(
        "gestion_cours.bureau",
        string="Bureau",
        required=True,
    )

    specialite_id = fields.Many2many(
        "gestion_cours.specialite", "liste_specialites", "intervenant_id", "specialite_id", string='Liste des specialités',required=True)

    _sql_constraints = [
        ('nom', 'unique(nom)', 'Ce nom existe déjà'),
        ('unique_telephone','unique(telephone,telephone2,telephone3)',"Les numéros de telephone doivent être différents")
    ]
