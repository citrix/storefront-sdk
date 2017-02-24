from __future__ import print_function
from HTMLParser import HTMLParser
import os
import sys

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    in_table = False
    table_index = 0
    output = ''
    folder = ''
    def unescape(self, s):
        s = s.replace("&lt;", "(LEFT)")
        s = s.replace("&gt;", "(RIGHT)")
        s = s.replace("&amp;", "(AND)")
        return s

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == 'table':
            self.table_index = self.table_index + 1
            self.in_table = True
            #1 Table overview
            #2 Table other
    def handle_data(self, data):
        data = data.strip()
        data = data.replace('(LEFT)', "<").replace('(RIGHT)', ">") #data = data.replace('(LEFT)',"&lt;").replace('(RIGHT)',"&gt;")
        if self.in_table and self.table_index == 1 and data != "":
            self.output = self.output + "   - " + data + ":\r\n"
            self.output = self.output + "       - Overview: " + data + "\\" + data + ".md\r\n"
            self.folder = data
        elif self.table_index == 2 and data != "":
            self.output = self.output + "       - "+data+": " + self.folder + "\\" + data + ".md\r\n" 
    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'table':
            self.in_table = False

parser = MyHTMLParser()
input_file = open('index.html', 'r')
input_content = input_file.read()
input_content = parser.unescape(input_content)
parser.feed(input_content)
print (parser.output)
input_file.close()