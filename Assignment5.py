# ASSIGNMENT NO : 5
# NAME: Vaishnavi Sanjay Aher
# ROLL NO: 64
# Regular Expression for URL's,ip addresses,PAN number and Dates.

import re


#Regular Expression
def find_entities(text):

  result = {
      'URLs':
      re.findall(r'https?://\S+|www\.\S+', text),
      'IP Addresses':
      re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
      'Dates':
      re.findall(r'([1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}',
                 text),
      'PAN Numbers':
      re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
  }
  return result


# INPUT:
text = """
First Dataset:
Visit our website at https://www.microsoft.com.
For support, contact us at customer@example.com.
IP address: 192.168.0.1
Date: 09/12/2023
PAN number: KIWPM3895J

Second Dataset:
Visit our website at https://www.youtube.com.
For more info connect with  info@example.com.
IP address: 192.165.9.5
Date: 24/07/2023
PAN number: PYZJW9585O

Third Dataset:
Visit our website at https://www.replit.com.
For more info connect with  customer@example.com.
IP address: 192.162.9.5
Date: 26/10/2023
PAN number: SKUYT9542L
"""

r = find_entities(text)

for entity_type, entities in r.items():
  print(f"{entity_type}: {entities}")

#OUTPUT:
# URLs: ['https://www.microsoft.com.', 'https://www.youtube.com.', 'https://www.replit.com.']
# IP Addresses: ['192.168.0.1', '192.165.9.5', '192.162.9.5']
# Dates: [('9', '12', '20'), ('24', '07', '20')]
# PAN Numbers: ['KIWPM3895J', 'PYZJW9585O', 'SKUYT9542L']