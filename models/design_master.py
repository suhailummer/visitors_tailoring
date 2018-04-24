from odoo import models, fields, api,_

class DesgnDesgn(models.Model):
     _name="desgn.desgn"
     
     name = fields.Char('name')
     image= fields.Binary("Image", help="Select image here")    
     type=fields.Selection([('neck',"Neck"),
                            ('collar','Collar'),
                            ('caf','Caf'),
                            ('pocket','pocket')
                            ], string="Design Type")
     test="hello"