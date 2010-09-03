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



import urllib,urllib2

class CoverGrabber:
    api_key = ""
    site_url = ""

    def __init__(self):
        self.api_key = "0343d933b8806a1609cb8b9b29813e42"
        self.site_url = "http://api.douban.com/music/subjects"

    def search_album_covers(self,album_title,song_title,file_name,count):
        if (not album_title) or len(album_title) == 0:
            album_title = song_title
        if (not album_title) or len(album_title) == 0:
            album_title = file_name

        values = {}
        values['apikey'] = self.api_key
        values['q'] = album_title
        values['max-results'] = str(count)
        url_data = urllib.urlencode(values)

        req = urllib2.Request(self.site_url+"?"+url_data)
        response = urllib2.urlopen(req)
        result_xml = response.read()

        return result_xml

if __name__ == '__main__':
    grabber = CoverGrabber()
    print grabber.search_album_covers("Best selection 2000 to 2005","flying","flying",1)
