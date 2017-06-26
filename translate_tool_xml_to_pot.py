#!/usr/bin/python
# -*- coding: utf_8 -*-
#
# dev version of tool xml schema is 
#  https://github.com/galaxyproject/galaxy/blob/dev/lib/galaxy/tools/xsd/galaxy.xsd

import os
from lxml import etree, objectify
import sys
reload(sys)
import codecs
import re

# for utf-8
sys.setdefaultencoding("utf-8")

# XML file name
xml_file = sys.argv[1]

# open po file
filepattern = re.compile(".xml")
potfilename = filepattern.sub("",  xml_file) + ".pot"
potfile = open(potfilename, 'w')
# msgid , msgstr and po file headers
potfile.write(u'msgid ""\n')
potfile.write(u'msgstr ""\n')
potfile.write(u'"Content-Type: text/plain; charset=utf-8\n"')
potfile.write(u'"Content-Transfer-Encoding: 8bit\n"')

# parse XML
tree = objectify.parse(xml_file, parser = etree.XMLParser())
root = tree.getroot()
#
# tool headers
potfile.write(u'"Tool-id: ' + root.get('id') + u"\\n\"\n")
potfile.write(u'"Tool-name: ' + root.get('name') + u"\\n\"\n")
potfile.write(u'"Tool-version: ' + root.get('version') + u"\\n\"\n")
# description
description = root.xpath("description")[0].text
potfile.write(u'\n')
potfile.write(u'msgid "' + description + u'"\n')
potfile.write(u'msgstr ""\n')

def write_as_po_file_format_single_line(text):
    if len(text) == 0:
        return
    potfile.write(u'\n')
    potfile.write(u'msgid "' + text.encode('utf-8') + u'"\n')
    potfile.write(u'msgstr ""\n')

def write_as_po_file_format(text):
    lines = text.split('\n')
    for i in range(len(lines)):
        if len(lines[i]) != 0:
            write_as_po_file_format_single_line(lines[i])

def extract_item_attribute(attrib, key):
    if key in attrib:
        text = attrib[key]
        write_as_po_file_format(text)


def extract_item_text(nodename):
    items = root.xpath('//' + nodename)
    for i in range(len(items)):
        try:
            item = items[i]
            write_as_po_file_format(item.text)
        except IndexError:
            pass
        except AttributeError:
            pass

# param
params = root.xpath('//param')
for i in range(len(params)):
    try:
        param = params[i]
        attrib = param.attrib
        extract_item_attribute(attrib, 'title')
        extract_item_attribute(attrib, 'label')
        extract_item_attribute(attrib, 'help')
    except IndexError:
        pass
    except AttributeError:
        pass



# option
extract_item_text('option')
extract_item_text('help')
