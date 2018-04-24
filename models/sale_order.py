# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo.exceptions import Warning, ValidationError
from odoo import models, fields, api, _

class saleorderline(models.Model):
    _inherit='sale.order.line'
    
    customer=fields.Many2one('res.partner','Customer')