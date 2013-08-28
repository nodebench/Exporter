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
# Exporter Version                    0.0.3
# Created on                          27-Aug-2013
# Author                              NodeBench
# --------------------------------------------------------------------------

import os 

path = r"."
main = 'Scene'

def convert_file():
    for index in range(0, 100):
        filename = "%s.%03d.sc" % (main, index)
        if os.path.exists(filename):
            newname = "%s.%d.sc" % (main, index)
            if os.path.exists(newname):
                os.unlink(newname)                
            os.rename(filename, newname)
            print("%s replaced with %s" % (filename, newname))

def animation_java():
    anim = []
    anim.append('public void build() {\n')
    anim.append('    include("Scene" + "." +  currentFrame()  + ".sc"); \n')
    anim.append('}\n') 
    
    fi = open('animation.java' , 'w')
    for lines in anim:
        fi.write(lines)
    fi.close()


def run_render(start_, end_):
    jardir = '"E:\\Graphics\\Sunflow\\sunflow.jar"'
    javadir = '"E:\\Program Files\\Java\\jdk1.7.0_25\\jre\\bin\\java.exe"'
    commands = [
                javadir,
                '-Xmx1200m',
                '-server',
                '-jar',
                jardir,
                '-anim' ,
                str(start_) ,
                str(end_) ,
                '-o',
                '"pictures\\output.#.png"',
                'animation.java' 
                ]
    open('runthis.bat', 'w').write(" ".join(commands))


if __name__ == '__main__':
    start_ = 1
    end_ = 40
    convert_file()
    animation_java()
    run_render(start_, end_)
    raw_input()
