from openerp.osv import fields, osv

class custom_items(osv.osv):
    
  _inherit = "product.product"

  _columns = {
    'item_specification': fields.char('Specifications / Size', size=500),
  }

  _defaults ={
    'item_specification': ''
  }

custom_items()