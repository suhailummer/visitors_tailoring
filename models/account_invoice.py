from odoo import models, fields, api, _

class invoiceSmartButton(models.Model):
    _inherit="account.invoice"
    def action_show(self):
        
        view_id = self.env.ref('project.edit_project')
        
        context = self._context.copy()

        return {

                    'name': view_id.name,
                    'type': 'ir.actions.act_window',
                    'view_type': view_id.type,
                    'view_mode': 'tree,form',
                    'target': 'current',
                    'context': context,
                    'res_model':'project.project',
        
        
       }