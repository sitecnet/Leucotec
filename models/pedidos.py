# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedidos(models.Model):
    _name = 'leucotec.pedidos'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Modelo principal para levantar pedidos"

    ###Funcion Fecha automatica######
    def _default_fecha(self):
        return fields.Date.context_today(self)
    ###Funcion direccion automatica######
    def _default_direccion(self):
        res = self.cliente.street + self.cliente.street2 + self.cliente.city
        return res(self)

    name = fields.Char(string='Pedido', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: ('New'))
    linea = fields.Many2one('leucotec.linea', 'Linea de Producto', required=True,)
    producto = fields.One2many('leucotec.lineas', 'linea_id', string='Productos', copy=True, auto_join=True)
    vendedor = fields.Many2one('res.users', string='Vendedor', default=lambda self: self.env.user)
    cliente = fields.Many2one('res.partner', 'Cliente')
    fecha = fields.Date('Fecha', default=_default_fecha)
    estado = fields.Selection([('vigente', 'Vigente'),
                               ('incompleto', 'Incompleto'),
                               ('facturado', 'Facturado'),
                               ('pagado', 'Pagado'),
                               ('entregado', 'Entregado'),
                               ], string='Estado', default='vigente')
    razon = fields.Char('Faltante')
    pago = fields.Selection([('01 - Efectivo', '01 - Efectivo'),
                               ('02 - Cheque', '02 - Cheque'),
                               ('03 - Transferencia', '03 - Transferencia'),
                               ('04 Tarjeta de Crédito', '04 Tarjeta de Crédito'),
                               ('28 - Tarjeta de débito', '28 - Tarjeta de débito'),
                               ('99 - Por Definir', '99 - Por Definir'),
                               ('Amex', 'Amex'),
                               ], string='Metodo de Pago', default='01')
    horario = fields.Char('Rango de horario de entrega')
    direccion = fields.Char('Direccion de Entrega', default=_default_direccion)
    entrega = fields.Date('Fecha de Entrega')
    factura = fields.Boolean('¿Requiere facturar?')
    observaciones = fields.Text('Observaciones')
    uso_cfdi = fields.Selection([('G01 - Adquisición de mercancias', 'G01 - Adquisición de mercancias'),
                               ('G03 - Gastos en general', 'G03 - Gastos en general'),
                               ('P01 - Por definir', 'P01 - Por definir'),
                               ('otro', 'Otro'),
                               ], string='Uso de CFDI')
    otro_cfdi = fields.Char('Uso de CFDI')
    #######Cobros#########
    fecha_cobro = fields.Date('Fecha', default=_default_fecha, groups='leucotec.pedidos_grupo_pagos') #groups='pedidos_grupo_pagos'
    importe = fields.Float('Importe', groups='leucotec.pedidos_grupo_pagos')
    comentarios = fields.Text('Comentarios')
    foto = fields.Binary('Foto del Pago', groups='leucotec.pedidos_grupo_pagos')
    #######Automatizacion de nombre consecutivo#########
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('pedidos') or ('New')
        res = super(pedidos, self).create(vals)
        return res

    class lineas(models.Model):
        _name = 'leucotec.lineas'
        _order = 'name'

        name = fields.Many2one('leucotec.catalogo', 'Producto', required=True, ondelete='cascade', index=True,
                               copy=False)
        linea_id = fields.Many2one('leucotec.pedidos', ondelete='cascade', index=True, copy=False)
        cantidad = fields.Integer('Cantidad')
        precio = fields.Char('Precio')
