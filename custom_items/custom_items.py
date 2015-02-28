from openerp.osv import fields, osv

class custom_items(osv.osv):
    
  _inherit = "product.product"

  _columns = {
    'item_specification': fields.char('Specifications / Size', size=500),
    'item_group':fields.many2one("x.itemgroup", 'Group'),
    'item_subgroup': fields.many2one("x.itemsubgroup") 
  }

  _defaults ={
    'item_specification': ''
  }

def location_name_search(self, cr, user, name='', args=None, operator='ilike',
                         context=None, limit=100):
    if not args:
        args = []

    ids = []
    if len(name) == 2:
        ids = self.search(cr, user, [('code', 'ilike', name)] + args,
                          limit=limit, context=context)

    search_domain = [('name', operator, name)]
    if ids: search_domain.append(('id', 'not in', ids))
    ids.extend(self.search(cr, user, search_domain + args,
                           limit=limit, context=context))

    locations = self.name_get(cr, user, ids, context)
    return sorted(locations, key=lambda (id, name): ids.index(id))

class Itemgroup(osv.osv):
    _name = 'x.itemgroup'
    _description = 'Item Group'
    _columns = {
        'name': fields.char('Group', size=64,
            help='The full name of the item group.', translate=True),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !')
    ]

    _order='name'

    name_search = location_name_search
    
class Itemsubgroup(osv.osv):
    _name = 'x.itemsubgroup'
    _description = 'Item Sub Group'
    _columns = {
        'name': fields.char('Sub Group', size=64,
            help='The full name of the item sub group.', translate=True),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !')
    ]

    _order='name'

    name_search = location_name_search


custom_items()