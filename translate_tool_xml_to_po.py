#!/usr/bin/python
# -*- coding: utf_8 -*-
#
# dev version of tool xml schema is
#  https://github.com/galaxyproject/galaxy/blob/dev/lib/galaxy/tools/xsd/galaxy.xsd

import os
from lxml import etree, objectify
import sys
import codecs
import re


# XML file name
xml_file = sys.argv[1]

# open po file
filepattern = re.compile(".xml")
pofilename = filepattern.sub("",  xml_file) + ".po"
pofile = open(pofilename, 'w')

# parse XML
tree = objectify.parse(xml_file, parser = etree.XMLParser())
root = tree.getroot()
# tool
pofile.write('"Tool-id: ' + root.get('id') + "\\n\"\n")
pofile.write('"Tool-name: ' + root.get('name') + "\\n\"\n")
pofile.write('"Tool-version: ' + root.get('version') + "\\n\"\n")
# description
description = root.xpath("description")[0].text
pofile.write('\n')
pofile.write('msgid "' + description + '"\n')
pofile.write('msgstr ""\n')

params = root.xpath('//param')

for i in range(len(params)):
    try:
        param = params[i]
        #print("--param")
        #print(param)
        attrib = param.attrib
        if 'title' in attrib:
            text = attrib['title']
            pofile.write('\n')
            pofile.write('msgid "' + text + '"\n')
            pofile.write('msgstr ""\n')
        if 'label' in attrib:
            text = attrib['label']
            pofile.write('\n')
            pofile.write('msgid "' + text + '"\n')
            pofile.write('msgstr ""\n')
        if 'help' in attrib:
            text = attrib['help']
            pofile.write('\n')
            pofile.write('msgid "' + text + '"\n')
            pofile.write('msgstr ""\n')

    except IndexError:
        pass
    except AttributeError:
        pass
