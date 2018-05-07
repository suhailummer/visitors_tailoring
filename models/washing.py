from odoo import models,fields,api

class washing_master(models.Model):
    _inherit='project.task'
#    @api.onchange('project_id')
#    def statusbar(self):
#       print"sssssssss"
#       self.write({'stage_id':'washing_charge'})
#    _default={'stage_id:'washing_chrg'}
        
    def service_washing(self):
        self.kanban_state="done"
    
    washing_chrg=fields.Float('Washing Charges')
    service_finished=fields.Char('Service Finished')
    task_id=fields.Many2one('project.project',string='task')
    
    class projectProject(models.Model):
     _inherit='project.project'
     
     additional_chrg=fields.One2many('project.task', 'task_id', string='Additional charges')
    
    