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
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    def _get_search_order(self, post):
        """We can configure default sort criteria for every website"""
        return "website_published desc,%s , id desc" % post.get(
            "order", request.website.default_product_sort_criteria
        )

    @route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        """We can configure default sort criteria for every website"""
        response = super().shop(
            page=page, category=category, search=search, **post
        )
        response.qcontext["order"] = post.get(
            "order", request.website.default_product_sort_criteria)
        return response
