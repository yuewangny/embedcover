#!/usr/bin/env python
#
# This file is part of embedcover.
#
# Embedcover is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Embedcover is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup
import os, glob

if os.name == "posix":
    data_files = [('share/man/man1', glob.glob("man/*.1"))]
else:
    data_files = []

setup(name='embedcover',
        version='0.1',
        description='Embedding covers automatically into mp3 files',
        author='Margaret Wang',
        author_email='pipituliuliu@gmail.com',
        url='http://github.com/pipitu/embedcover',
        license='GNU GPL v3',
        packages=['douban_cover'],
        scripts=['embedcover'],
        data_files=data_files,
        requires=[
            'Python',
            'mutagen'
            ],
    )
