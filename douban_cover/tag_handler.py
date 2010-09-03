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

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

class TagHandler:
    filename = ""
    audio = None

    def __init__(self,file_name):
        #print file_name
        self.filename = file_name
        self.audio = MP3(self.filename, ID3=ID3)
        try:
            self.audio.add_tags()
        except error:
            pass

    def get_song_title(self):
        song = ""
        try:
            song = self.audio['title'][0]
        except KeyError:
            pass
        return song 

    def get_album_title(self):
        album = ""
        try:
            album = self.audio['TALB'][0]
        except KeyError:
            pass
        return album.encode("utf-8")

    def has_cover(self):
        if len(self.audio.tags.getall("APIC")) == 0:
            return False 
        return True

    def get_cover(self):
        frames = self.audio.tags.getall("APIC")
        for frame in frames:
            ext = ".img"
            if frame.mime == "image/jpeg" or frame.mime == "image/jpg":
                ext = ".jpg"
            elif frame.mime == "image/png":
                ext = ".png"
            elif frame.mime == "image/gif":
                ext = ".gif"
        return (ext,frame.data)

    def embed_cover(self,imagedata):
        self.audio.tags.add(APIC(encoding = 3,mime = "image/jpeg",type = 3,
            desc = u'Cover',data=imagedata))
        self.audio.save()

if __name__ == "__main__":
    th = TagHandler("test.mp3")
    print th.get_album_title()
    if th.has_cover():
        print "has cover~~"
        myfile = file("cover.jpg", 'wb')
        myfile.write((th.get_cover())[1])
        myfile.close()
    else:
        th.embed_cover(open("test.jpg").read())
