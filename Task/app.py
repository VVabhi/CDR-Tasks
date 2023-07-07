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

@app.route('/route', methods=('GET', 'POST'))
def get_page():
   if request.method == 'POST':
      number = request.form["number"]
      query_obj = db.aql.execute(f'FOR doc IN contacts FILTER doc.party_a == "{number}" RETURN doc')
      query_list = list(query_obj)
      count = {}
      for item in query_list:
         if item['party_a_ori'] in count:
            count[item['party_a_ori']] = count[item['party_a_ori']]+1
         else:
            count[item['party_a_ori']] = 1
         
         if item['IMSI'] in count:
            count[item['IMSI']] = count[item['IMSI']]+1
         else:
            count[item['IMSI']] = 1
         
         if item['IMEI'] in count:
            count[item['IMEI']] = count[item['IMEI']]+1
         else:
            count[item['IMEI']] = 1

      print(count)
      # df = pd.DataFrame(count.values(),columns=['party_a_ori','IMSI','IMEI'])
      return render_template('submit.html', data=count)



if __name__ == '__main__':
   app.run(port=5002,debug=True)
