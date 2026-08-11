# Main script to test database connection

import sys
sys.path.append('./09-SQL')
import sql_connector  # noqa: E402

# This back to the root directory of the project, so that we can import my
# sql_connector module from the 09-SQL directory. This will allow me to test
# the connection.

# You won't find this file as it has details of my server.

mydb = sql_connector.connect_to_database()

# test db connection
if mydb.is_connected():
    print("Successfully connected to the database.")
