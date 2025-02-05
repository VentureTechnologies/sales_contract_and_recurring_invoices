# -*- coding: utf-8 -*-
##############################################################################
#
#    Venture Technology
#
#    Copyright (C) 2024-TODAY Venture Technology(<https://www.venturetech.site>)
#    Author: Venture Technology(info@venturetech.site)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import fields, models


class SaleOrderLine(models.Model):
    """ Add contract reference in sale order line """
    _inherit = 'sale.order.line'

    contract_id = fields.Many2one(
        'subscription.contracts',
        string='Contracts',
        help='For adding Contracts in sale order line')
