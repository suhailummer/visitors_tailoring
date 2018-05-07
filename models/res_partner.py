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
    address=fields.Char('Address')
    seq_number=fields.Char('ID',readonly=True)
    
    def _compute_measurement_count(self):
        for partner in self:
            partner.measurement_count = len(partner.measurement_ids)
    
    @api.model
    def create(self, vals):
         seq= self.env['ir.sequence'].get('seq.seq')
         vals['seq_number'] = seq
         return super(ResPartner, self).create(vals)
               
    
