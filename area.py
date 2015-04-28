from openerp import models, fields, api

class area(models.Model):
    _name = 'procedimientos.area'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()


