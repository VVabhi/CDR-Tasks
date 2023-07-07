# from pyArango.connection import Connection

# # Create a connection to ArangoDB
# conn = Connection(
#     arangoURL='http://localhost:8529',
#     username='root',
#     password=''
# )

# db = conn['CDR_New_latest']

# collection = db['contacts']

# documents = collection.fetchAll()

# for doc in documents:
#     scientific_data = doc['scientific_data']
#     formatted_data = '8,170,000,000,000,000.00'
#     modified_data = float(formatted_data.replace(',', ''))    
#     print(modified_data)

import warnings
warnings.filterwarnings("ignore")
from arango import ArangoClient
import pyArango
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

client = ArangoClient()
db = client.db('CDR_New_latest')
coll = db.collection('contacts')
numbers = db.aql.execute(f'FOR doc IN contacts FILTER doc.IMEI == "8.17E+15" RETURN doc')
# print(numbers)
# formatted_numbers = []
for record in numbers:
    imei = record['IMEI']
    formatted_number = "{:.0f}".format(float(imei))
    print(formatted_number)
    record['IMEI'] = formatted_number
    print(record)
    coll.update(record)
# for record in numbers:
#     # print(record)
#     imei = record['IMEI']
#     imei = float(imei)
#     # formatted_number = "{:,.2f}".format(imei)
#     formatted_number ="{:.0f}".format(imei)clear
#     print(formatted_number)
# #     formatted_numbers.append(formatted_number)
# # print(formatted_numbers)

# for i in formatted_numbers:
#     upd_query='''FOR doc IN contacts
#         FILTER doc.IMEI=="8.17E+14"
#         UPDATE doc WITH { IMEI: @new_value } IN contacts'''
#     db.aql.execute(upd_query,bind_vars={'new_value':i})
    
# 
# 