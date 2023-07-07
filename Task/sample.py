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

@app.route("/", methods=['GET', 'POST'])
def Home_Page():
   return render_template("index.html")

# Defining key mapping dictionary required
key_mapping = {
    "Name": "Name",
    "Address": "Address",
    "IMEI": "IMEI",
    "IMSI": "IMSI",
    "Type_of_Connection": "Type_of_Connection",
    "LRN_DESCRIPTION": "LRN_DESCRIPTION"
}

@app.route('/route', methods=['POST'])
def get_page():
    if request.method == 'POST':
        number = request.form["number"]
        query_obj = db.aql.execute(f'FOR doc IN contacts FILTER doc.party_a == "{number}" RETURN doc')
        query_list = list(query_obj)
        df = pd.DataFrame(query_list, columns=["Name", "Address", "IMEI","IMSI", "Type_of_Connection", "LRN_DESCRIPTION"])
        count = {}
        for item in query_list:
            for key in key_mapping.keys():
                value = item.get(key)
                if value is not None:
                    output_key = key_mapping[key]
                    if output_key not in count:
                        count[output_key] = {}
                    if value not in count[output_key]:
                        count[output_key][value] = 1
                    else:
                        count[output_key][value] += 1

        return render_template('submit.html', count=count)


if __name__ == '__main__':
   app.run(port=5002,debug=True)





# 1 components/page 
# 2 discription
# 3 status