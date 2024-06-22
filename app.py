from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Change the following values to match yours
db_name = os.getenv("db_name")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_port = os.getenv("db_port")

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(database=db_name, user=db_user, password=db_password,
                        host=db_host, port=db_port)
cur = conn.cursor()

# Define a route that accepts POST requests to run SQL queries
@app.route("/query", methods=["GET"])
def query():
    cur.execute("select * from table1")
    result = cur.fetchall()

    # Return the result as JSON
    return jsonify(result)

# Run the Flask app on port 8080
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
