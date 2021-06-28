# -*- coding: utf-8 -*-
# #############################################################################
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
###############################################################################.
{
    'name': 'Website Sale Product Sort',
    'summary': 'Allow to define default sort '
               'criteria for e-commerce',
    'version': '14.0.1.0.0',
    'development_status': 'Beta',
    'category': 'Website',
    'author': 'Eezee-It',
    'license': 'LGPL-3',
    'depends': [
        'website_sale',
    ],
    'data': [
        "views/website_sale_sort.xml",
        "views/res_config_settings_view.xml",
    ],
    'application': False,
    'installable': True,
}
