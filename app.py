from flask import Flask, request, jsonify
import psycopg2
import os

from azure.storage.blob import ContainerClient
import json

app = Flask(__name__)

# Change the following values to match yours
db_name = os.getenv("db_name")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_port = os.getenv("db_port")

conn_str = os.getenv("conn_str")
container_name = os.getenv("container_name")

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(database=db_name, user=db_user, password=db_password,
                        host=db_host, port=db_port)
cur = conn.cursor()

# Define a route that accepts get requests to run SQL queries
@app.route("/query", methods=["GET"])
def query():
    cur.execute("select * from table1")
    result = cur.fetchall()

    # Return the result as JSON
    return jsonify(result)

# Define a route that accepts get requests to list blob
@app.route("/gfiles", methods=["GET"])
def gfiles():
    container = ContainerClient.from_connection_string(conn_str=conn_str, container_name=container_name)

    blob_list = container.list_blobs()

    # Return the result as JSON
    return json.dumps(blob_list)

# Run the Flask app on port 8080
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
