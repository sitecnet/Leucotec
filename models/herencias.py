# -*- coding: utf-8 -*-

from odoo import fields, models, api

class resUsers(models.Model):
    _inherit = "res.users"
    _description = "Campos extra de Usuarios"
    agente = fields.Char(string='Agente')

resUsers()

class resPartner(models.Model):
    _inherit = "res.partner"
    _description = "Campos extra de clientes"

    pedidos = fields.One2many('leucotec.pedidos', 'cliente', string='Pedidos', copy=True, auto_join=True)
    RFC = fields.Char('RFC')
    cedula = fields.Char('Cedula Profesional')
    especialidad = fields.Many2one('leucotec.especialidades', 'Especialidad')

resPartner()
