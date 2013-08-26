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
# Exporter Version                    0.0.1
# Created on                          25-Aug-2013
# Author                              NodeBench
# --------------------------------------------------------------------------


import os
import zipfile


def create_release_package():
    '''
    create a taged release version from github will not do the trick.
    Since the folder structure in eclipse git is like proj/proj/src/sunflow
    and when tagged and zipped will contain all these sub folders
    but inside blender addon folder it requires in a form like 
    sunflow/modules. so zipped installer should only contain this sunflow sub folder.
    '''
    zip_version = '0.0.3'
    search_path = '../sunflow'
    zipit(zip_version, search_path)

def zipit(zip_version, rel_to_path):
    zip_to_path = r'E:\DevelProjects\gitRepository\Exporter.wiki\releases'
    
    rel_to_path = os.path.abspath(rel_to_path)
    zip_to_path = os.path.abspath(zip_to_path)
    
    zip_name = os.path.basename(rel_to_path)
    pth_in_zip = os.path.dirname(rel_to_path)
    zip_file = zip_name + '_exporter_v' + zip_version + '.zip'
    
    print(zip_file)
    zip_path = os.path.join(zip_to_path, zip_file)
    
    if os.path.exists(zip_path):
        os.unlink(zip_path)
    
    zip_f = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(pth_in_zip) + 1
    for base, dummy_dirs, files in os.walk(rel_to_path):
        for file_in in files:
            fn = os.path.join(base, file_in)
            zip_f.write(fn, fn[rootlen:])

if __name__ == '__main__':
    create_release_package()