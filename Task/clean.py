import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import os
import csv
import glob

# file_path = '/home/msi_ubuntu/Desktop/CDR-Latest/Upload_Files_Folder/'
# df = pd.read_csv(file_path)
# print(df)

path = os.getcwd()
csv_files = glob.glob(os.path.join('/home/msi_ubuntu/Desktop/CDR-Latest/Upload_Files_Folder', "*.csv"))

for f in csv_files:  
    df = pd.read_csv(f)
    # print(df)
    column_names = list(df.columns)
    print(column_names)



# 6357914825
# 9332060714
# 919881000000
# 918831990932
# 919279845346