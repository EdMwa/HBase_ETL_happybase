# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:36:27 2019

@author: Ed
"""

#%%IMPORTS
from happybase import Connection
#%%SET CONNECTION VARIABLES & DATA PATH
host = "127.0.0.1"
port = 8000
batch_size = 50000
file_path = "../input/u.data"
namespace = "sample_data"
row_count = 0
table_name = "movies"
#%%

def connect_to_hbase():
    """ Connect to HBase server.
    This will use the host, namespace, table name, and batch size as defined in
    the global variables above.
    """
    conn = Connection(host = host,
        port = port,             
        table_prefix = namespace,
        table_prefix_separator = ":")
    conn.open()
    table = conn.table(table_name)
    batch = table.batch(batch_size = batch_size)
    return conn, batch

def insert_row(batch, row):
    """ Insert a row into HBase.
    Write the row to the batch. When the batch size is reached, rows will be
    sent to the database.
    Rows have the following schema:
        [userID, movieID, rating, timestamp]
    """
    batch.put(row[0], { "data:movieId": row[1], "data:rating": row[2], "data:timestamp": row[3]})
    
def read_file():
    data = []
    with open(file_path, "r") as file:
        for line in file:
            infile = line.split()
            data.append(infile)
            #print(data)
            return data

#%%
# After everything has been defined, run the script.
conn, batch = connect_to_hbase()
print("Connecting to HBase. table name: {}, batch size: {}".format(table_name, batch_size))
data = read_file()
print("Connected to file. name: {}".format(file_path))

try:
    """
    Loop through the rows. The first row contains column headers, so skip that
    row. Insert all remaining rows into the database.
    """
    for row in data:
        row_count += 1
        if row_count == 1:
            pass
        else:
            insert_row(batch, row)

    # If there are any leftover rows in the batch, send them now.
    batch.send()
finally:
    conn.close()

print("Done!row count: {}".format(row_count))
