# XML generation for RegExTools
# Created by Pierre van Male <vmalep@gmail.com> July 2017
# Inspired by Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>
# As a modification of DoobieDoo OOo Calc Add-in example.
# Created by jan@biochemfusion.com April 2009.

# A unique ID for the add-in.
addin_url = 'be.vmalep.libreoffice'
addin_name = 'Regextools'
addin_python_file = 'regextools.py'
excel_addin_name = 'Regextools.xlam'
addin_id = "%s.%s" % (addin_url, addin_name)
addin_version = "0.1.1"
addin_displayname = "Functions using RegEx"
addin_publisher_link = "https://github.com/vmalep/LORegExAdd-In"
addin_publisher_name = "Pierre van Male"
addin_functions = [
    {
        'function_name': 'regextract',
        'function_description': 'Extract string using RegEx',
        'parameters': [
            ('a', 'String to search into'),
            ('b', 'RegEx to apply'),
            ('c', 'Found group to return')
        ]},
]

# description.xml
#
#

desc_xml = open('description.xml', 'w')

desc_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
desc_xml.write('\t<description \
xmlns="http://openoffice.org/extensions/description/2006" \n')
desc_xml.write('xmlns:d="http://openoffice.org/extensions/description/2006" \
\n')
desc_xml.write('xmlns:xlink="http://www.w3.org/1999/xlink"> \n')
desc_xml.write('\t<dependencies> \n')
desc_xml.write('\t\t<OpenOffice.org-minimal-version value="2.4" \
d:name="OpenOffice.org 2.4"/> \n')
desc_xml.write('\t</dependencies> \n')
desc_xml.write('\t<registration>\n')
desc_xml.write('\t\t<simple-license accept-by="admin" \
default-license-id="ID0" suppress-on-update="true">\n')
desc_xml.write('\t\t<license-text xlink:href="resources/license_es.txt" \
lang="es" license-id="ID0"/>\n')
desc_xml.write('\t\t<license-text xlink:href="resources/license_en.txt" \
lang="en"/>\n')
desc_xml.write('\t\t</simple-license>\n')
desc_xml.write('\t</registration>\n')
desc_xml.write('\t<identifier value="%s" /> \n' % (addin_id))
desc_xml.write('\t<version value="%s" />\n' % (addin_version))
desc_xml.write('\t<display-name>\n')
desc_xml.write('\t\t<name lang="en">%s</name>\n' % (addin_displayname))
desc_xml.write('\t\t<name lang="es">%s</name>\n' % (addin_displayname))
desc_xml.write('\t</display-name>\n')
desc_xml.write('\t<publisher>\n')
desc_xml.write('\t\t<name xlink:href="%s" lang="en">%s</name>\n' % (
    addin_publisher_link, addin_publisher_name))
desc_xml.write('\t\t<name xlink:href="%s" lang="es">%s</name>\n' % (
    addin_publisher_link, addin_publisher_name))
desc_xml.write('\t</publisher>\n')
desc_xml.write('\t<icon>\n')
desc_xml.write('\t\t<default xlink:href="icons/icon.png"/>\n')
desc_xml.write('\t</icon>\n')
desc_xml.write('\t<extension-description>\n')
desc_xml.write('\t\t<src xlink:href="description/pkg-description_en.txt" \
lang="en"/>\n')
desc_xml.write('\t\t<src xlink:href="description/pkg-description_es.txt" \
lang="es"/>\n')
desc_xml.write('\t</extension-description>\n')
desc_xml.write('</description>')

desc_xml.close


def add_manifest_entry(xml_file, file_type, file_name):
    xml_file.write('<manifest:file-entry \
manifest:media-type="application/vnd.sun.star.%s" \n' % (file_type))
    xml_file.write('manifest:full-path="%s"/> \n' % (file_name))

# manifest.xml
#
# List of files in package and their types.

manifest_xml = open('manifest.xml', 'w')

manifest_xml.write('<manifest:manifest>\n')
add_manifest_entry(manifest_xml,
                   'uno-typelibrary;type=RDB',
                   'X%s.rdb' % (addin_name))
add_manifest_entry(manifest_xml,
                   'configuration-data',
                   'CalcAddIn.xcu')
add_manifest_entry(manifest_xml,
                   'uno-component;type=Python',
                   addin_python_file)
manifest_xml.write('</manifest:manifest> \n')

manifest_xml.close

# CalcAddIn.xcu
#
#

# instance_id references the named UNO component instantiated by Python code
# (that is my understanding at least).
instance_id = "%s.%s.python.%sImpl" % (addin_url, addin_name, addin_name)

# Name of the corresponding Excel add-in if you want to share documents across
# OOo and Excel.
# excel_addin_name = "DoobieExample.xlam"


def define_function(xml_file, function_name, description, parameters):
    xml_file.write('  <node oor:name="%s" oor:op="replace">\n' % (
        function_name))
    xml_file.write('    <prop oor:name="DisplayName"><value \
xml:lang="en">%s</value></prop>\n' % (function_name))
    xml_file.write('    <prop oor:name="Description"><value \
xml:lang="en">%s</value></prop>\n' % (description))
    xml_file.write('    <prop oor:name="Category"><value>\
Add-In</value></prop>\n')
    xml_file.write('    <prop oor:name="CompatibilityName">\
<value xml:lang="en">AutoAddIn.%s.%s</value></prop>\n' % (
        addin_name, function_name))
    xml_file.write('    <node oor:name="Parameters">\n')

    for p, desc in parameters:
        # Optional parameters will have a displayname enclosed in square
        # brackets.
        p_name = p
        xml_file.write(
            '      <node oor:name="%s" oor:op="replace">\n' % (p_name))
        xml_file.write(
            '        <prop oor:name="DisplayName">\
<value xml:lang="en">%s</value></prop>\n' % (p_name))
        xml_file.write(
            '        <prop oor:name="Description">\
<value xml:lang="en">%s</value></prop>\n' % (desc))
        xml_file.write('      </node>\n')
    xml_file.write('    </node>\n')
    xml_file.write('  </node>\n')

#
calcaddin_xml = open('CalcAddIn.xcu', 'w')

calcaddin_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
calcaddin_xml.write('<oor:component-data \
xmlns:oor="http://openoffice.org/2001/registry" \
xmlns:xs="http://www.w3.org/2001/XMLSchema" \
oor:name="CalcAddIns" oor:package="org.openoffice.Office">\n')
calcaddin_xml.write('<node oor:name="AddInInfo">\n')
calcaddin_xml.write('<node oor:name="%s" oor:op="replace">\n' % (instance_id))
calcaddin_xml.write('<node oor:name="AddInFunctions">\n')

for addin_function in addin_functions:
    define_function(calcaddin_xml,
                    addin_function['function_name'],
                    addin_function['function_description'],
                    addin_function['parameters'])

calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</oor:component-data>\n')

calcaddin_xml.close()

# Done
