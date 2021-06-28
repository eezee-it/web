# -*- coding: utf-8 -*-
# ############################################################################
#
#    Copyright Eezee-It (C) 2021
#    Author: Eezee-It <info@eezee-it.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import _, api, fields, models


class Website(models.Model):
    _inherit = "website"

    @api.model
    def _get_product_sort_criterias(self):
        """Extend to add more sort criterias"""
        return [
            ('website_sequence desc', _('Relevance')),
            ('list_price desc', _('Catalog price: High to Low')),
            ('list_price asc', _('Catalog price: Low to High')),
            ('name asc', _('Name - A to Z')),
            ('name desc', _('Name - Z to A')),
        ]

    default_product_sort_criteria = fields.Selection(
        selection='_get_product_sort_criterias',
        string="Sort products by",
        help="Default criteria for sorting products in the shop",
        default='website_sequence desc',
        required=True,
    )
