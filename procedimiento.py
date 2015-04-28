from openerp import models, fields, api

class procedimiento(models.Model):
    _name = 'procedimientos.procedimiento'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
    larea       = fields.Many2one('procedimientos.area')
    lproceso    = fields.Many2one('procedimientos.proceso')

