#
# Copyright 2010 Margaret Wang <pipituliuliu@gmail.com>
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


import sys
import os
import glob

class FileOperation:
    currentdir = ""

    def __init__(self):
        self.currentdir = os.getcwd()
        self.cd(self.currentdir)

    def get_current_dir(self):
        return self.currentdir

    def cd(self,subdir):
        if os.path.isdir(self.currentdir):
            try:
                os.chdir(subdir)
                if subdir != '..':
                    self.currentdir = os.path.join(self.currentdir,subdir)
                else:
                    self.currentdir = os.path.dirname(self.currentdir)
                return True
            except WindowsError,OSError:
                return False
        else:
            return False

    def ls_dir(self):
        subdirs = []
        
        for subdir in os.listdir(self.currentdir):
            if os.path.isdir(os.path.join(self.currentdir,subdir)) and subdir.find('.') != 0:
                subdirs.append(subdir)
        subdirs.append("..")
        return subdirs

    def ls_file(self,filetype):
        subdirs = []
        for subdir in os.listdir(self.currentdir):
            if os.path.isfile(os.path.join(self.currentdir,subdir)) and subdir.endswith(filetype):
                subdirs.append(subdir)
        return subdirs
