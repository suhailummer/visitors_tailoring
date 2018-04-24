# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.


from odoo.exceptions import Warning, ValidationError
from odoo import models, fields, api, _
from datetime import datetime
from dateutil.relativedelta import relativedelta

class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "Partner"

    measurement_ids = fields.One2many('measurement.measurement', 'partner_id', string='Tasks')
    measurement_count = fields.Integer(compute='_compute_measurement_count', string='# Measurements')
    mobile_num1=fields.Char('Mobile No 1')
    mobile_num2=fields.Char('Mobile No 2')
    mobile_num3=fields.Char('Mobile No 3')
    mobile_num4=fields.Char('Mobile No 4')
    address=fields.Char('Address')
    
    def _compute_measurement_count(self):
        for partner in self:
            partner.measurement_count = len(partner.measurement_ids)

