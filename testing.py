#!/usr/bin/python

from suds.client import Client
import logging
import base64

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

# Username and Password, assigned by FINKOK
username = 'cfdi@vauxoo.com'
password = 'vAux00__'

# Read the xml file and encode it on base64
invoice_path = "request.xml"
file = open(invoice_path)
lines = "".join(file.readlines())
xml = base64.encodestring(lines)

# Consuming the stamp service
url = "https://demo-facturacion.finkok.com/servicios/soap/stamp.wsdl"
client = Client(url, cache=None)
contenido = client.service.stamp(xml, username, password)
xml = contenido.xml

# Get stamped xml
archivo = open("stamp.xml", "w")
archivo.write(str(xml))
archivo.close()

# Get SOAP Request
last_request = client.last_sent()
req_file = open('request.xml', 'w')
req_file.write(str(last_request))
req_file.close()

# Get SOAP Response
last_response = client.last_received()
res_file = open('response.xml', 'w')
res_file.write(str(last_response))
res_file.close()
