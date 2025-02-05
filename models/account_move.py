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


class AccountMove(models.Model):
    """ Inheriting account move model to add id of subscription """
    _inherit = 'account.move'

    contract_origin = fields.Integer(string='Subscription Contract',
                                     help='Reference of Subscription Contract')
