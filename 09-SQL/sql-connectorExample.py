# Create a connection to the MySQL database using the mysql.connector module.

# this is an example module for demonstration purposes.

# why create a connection module? Because it allows you to reuse the
# connection code across multiple scripts, making your code more modular and
# easier to maintain. By having a separate module for database connections,
# you can easily update the connection details (like host, user, and password)
# in one place without having to change it in every script that connects to
# the database.

import mysql.connector


def connect_to_database():
    """Connect to the MySQL database.

    Returns:
        mysql.connector.connection.MySQLConnection: The connection object to
        the MySQL database.
    Args:
        host (str): The hostname of the MySQL server. Default is "localhost".
        user (str): The username to connect to the MySQL server.

        password (str): The password for the MySQL user.

    Outputs:
        mysql.connector.connection.MySQLConnection: The connection object to
        the MySQL database.
        >>> connect_to_database()
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="username",
        password="Password"
    )
    return mydb

# SQL security best practices:
# https://www.geeksforgeeks.org/mysql/mysql-security-best-practices/
