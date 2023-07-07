import warnings
warnings.filterwarnings("ignore")
from arango import ArangoClient
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

client = ArangoClient()
db = client.db('test')
coll = db.collection('data2')

@app.route("/")
def index():
    df = pd.read_csv(r'/home/msi_ubuntu/Desktop/CDR_Data/doc3.csv')
    data = df.to_dict("records")
    coll.insert(data)
    rows = coll.all()
    cols = df.columns.tolist()
    return render_template('result.html', rows=rows, cols=cols)


if __name__ == '__main__':
    sys_db = client.db('_system', username='root')
    if not sys_db.has_database('test'):
        sys_db.create_database('test')
    if db.has_collection('data3'):
        coll = db.collection('data3')
    else:
        coll = db.create_collection('data3')
    app.run(port=4000, debug=True)