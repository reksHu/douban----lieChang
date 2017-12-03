import sqlite3
import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np
dbPath='E:\pythonProjects\lieChang\data\doubanDB1.db'
conn = sqlite3.connect(dbPath)

#sql = 'DELETE FROM douban'
sql = 'select * from douban'
c = conn.cursor()
result = pd.read_sql(sql,conn)
print(result.head())
result['commentTime'] = pd.to_datetime(result['commentTime'])

# # print(result['commentTime'].value_counts())
# newResult = result['2017-11-06':'2017-11-15']
# print(newResult)
sentimentslist = []
i=0
while(i< len(result['comment'])):
    s = SnowNLP(result['comment'][i])
    # print(s.sentiments)
    sentimentslist.append(s.sentiments)
    i = i+1
plt.hist(sentimentslist,bins=np.arange(0,1,0.01))
plt.show()
conn.close()