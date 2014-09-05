# -*- coding: utf-8 -*-
################################################################################
#
# Automated Clearing House module
# Copyright (C) 
#    2013 Emile van Sebille.  All Rights Reserved.
#
# Automated Clearing House module is free software: you can redistribute
# it and/or modify it under the terms of the Affero GNU General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Automated Clearing House module is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Affero GNU
# General Public License for more details.
#
# You should have received a copy of the Affero GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
    "name": "Automated Clearing House HR",
    "version": "0.1",
    "author": "Emile van Sebille",
    'website': 'http://salesinq.com',
    "category": "Specific Modules/Automated Clearing House",
    "description": """
Automated Clearing House HR adds the necessary field to the hr.employee record to
enable Direct Deposit.
""",
    'depends': [
        'base',
        'automated_clearing_house',
        'hr',
        ],
    'data': [
        'hr_view.xml',
        'security/ach_hr_security.xml',
        'security/ir.model.access.csv',
        ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
