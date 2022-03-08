from datetime import date
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Cours(models.Model):
    _name = "gestion_cours.cours"
    _description = "Un cours"
    date_debut = fields.Date(string="Date de début",required=True,)
    annee=fields.Integer(string="Année",required=True)
    numero = fields.Integer(
        string="Numero",
        required=True,
    )
    titre = fields.Char(
        string="Titre",
        required=True,
    )
    type_cours=fields.Selection(selection=[
        ('Cours','C'),
        ('Travaux Dirigés','TD'),
        ('Travaux Pratiques','TP')
    ],required=True,)
    @api.constrains('annee','numero')
    def _check_telephone(self):
        for record in self:
            if(record.annee or record.numero ):
                if(not str(record.annee).isdigit() or not str(record.numero).isdigit()):
                    raise ValidationError("Le numero ou l'année doit etre composé de chiffres")
                 
    @api.depends("date_debut")
    def _compute_date_fin(self):
        for record in self:
            if record.date_debut:

                jour,mois,annee=record.date_debut.day,record.date_debut.month,record.date_debut.year
                self.date_fin=date(annee,mois,jour+5)
        return None
    date_fin = fields.Date(string="Date de fin",compute="_compute_date_fin")
    intervenant_id = fields.Many2one(
        "gestion_cours.intervenant",
        string="Intervenant",
        required=True,
    )

