from odoo import models, fields, api, tools

class entregas(models.Model):
    _name = 'leucotec.entregas'
    _description = "Registro de entregas de productos"
    _inherit = ['image.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char('Numero de pedido', required=True,)
    usuario = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user)
    image_1024 = fields.Image("Image", max_width=1024, max_height=1024)
    image_1920 = fields.Image("Image", max_width=1024, max_height=1024)
    firma = fields.Binary('Firma')
    comentarios = fields.Binary('Comentarios')
    comentarios2 = fields.Text('Comentarios')
    picture = fields.Binary('Comentarios')

    @api.model
    def create(self,vals):
        if 'picture' in vals:
            image = tools.ImageProcess(vals['picture'])
            # resize uploaded image into 250 X 250
            resize_image = image.resize(1024, 1024)    
            resize_image_b64 = resize_image.image_base64()   
            vals['picture'] = resize_image_b64
        obj = super(entregas, self).create(vals)
        return obj
