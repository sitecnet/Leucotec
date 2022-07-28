# -*- coding: utf-8 -*-

from odoo import models, fields, api

class catalogo(models.Model):
    _name = 'leucotec.catalogo'
    _description = "Catalogo de productos"
    _rec_name = 'name'

    name = fields.Char('Nombre', required=True,)
    imagen = fields.Binary()
    precio = fields.Float('Precio')
    proveedor = fields.Many2one('leucotec.proveedor')
    presentacion = fields.Many2one('leucotec.presentacion')
    linea = fields.Many2one('leucotec.linea')

class proveedor(models.Model):
    _name = 'leucotec.proveedor'
    _description = "Proveedor de Prodcuto"
    name = fields.Char('Proveedor')

class presentacion(models.Model):
    _name = 'leucotec.presentacion'
    _description = "Presentación del producto"
    name = fields.Char('Presentacion')

class linea(models.Model):
    _name = 'leucotec.linea'
    _description = "Linea del Producto"
    name = fields.Char('Linea de Productos')