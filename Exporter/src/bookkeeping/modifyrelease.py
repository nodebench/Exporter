# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENCE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender Version                     2.68
# Exporter Version                    0.0.4
# Created on                          26-Aug-2013
# Author                              NodeBench
# --------------------------------------------------------------------------

import os

def version_bump():
    '''
    Run this module after creating a release branch, to change the version number
    of the exporter in all files.
    Then manually merge the release branch to the master branch to finalise the release. 
    '''
    zip_version = '0.0.4'
    search_path = '../sunflow'
    bump(zip_version, search_path)

def bump(next_version , search_path):
    find_string = '# Exporter Version'    
    search_full = os.path.abspath(search_path)    
    for base, dummy_dirs, files in os.walk(search_full):
        for file_in in files:
            fn = os.path.join(base, file_in)
            if not os.path.exists(fn): continue
            cache = []
            curfile = open(fn, 'r')
            for lines in curfile:
                if lines.startswith(find_string):
                    lines = '# Exporter Version                    ' + next_version + '\n'
                cache.append(lines)
            curfile.close()
            curfile = open(fn, 'w')
            for lines in cache:
                curfile.write("%s" % lines)
            curfile.close()            
            
if __name__ == '__main__':
    version_bump()