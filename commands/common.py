from xml.dom import minidom

def print_xml(xml_str: str, indent: str='\t') -> None:
   xml_doc = minidom.parseString(xml_str)
   print(xml_doc.toprettyxml(indent=indent)) 