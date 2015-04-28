from openerp import models, fields, api

class proceso(models.Model):
    _name = 'procedimientos.proceso'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()


