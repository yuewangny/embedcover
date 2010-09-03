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


from xml.dom import minidom

class Parser:
    def __init__(self):
        pass
    def parse_result(self,result):
        pass

class XmlParser(Parser):
    def getText(self,nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                #print node.data
                rc = rc + node.data
        return rc

    def parse_result(self,result):
        elements = minidom.parseString(result)
        albums = [] 
        for entry in elements.getElementsByTagName("entry"):
            album = {}
            try:
                album["id"] = self.getText(entry.getElementsByTagName("id")[0].childNodes)
                album["title"] = self.getText(entry.getElementsByTagName("title")[0].childNodes)
                album["author"] = self.get_authors(entry.getElementsByTagName("author")[0].getElementsByTagName("name"))
                album["image"] = self.get_image(entry.getElementsByTagName("link"))
                albums.append(album)
            except IndexError:
                pass
        return albums

    def get_authors(self,authors):
        author_str = ""
        for author in authors:
            author_str = author_str + self.getText(author.childNodes)
        return author_str
    
    def get_image(self,links):
        for link in links:
            if link.attributes["rel"].value == "image":
                return link.attributes["href"].value


from douban_client import CoverGrabber
if __name__ == "__main__":
    grabber = CoverGrabber()
    result_xml = grabber.search_album_covers("best selection 2000 to 2005","","",1)
    parser = XmlParser()
    albums = parser.parse_result(result_xml)
    print albums
