#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd


# In[2]:


connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "Raghu#456")
cursorObject =connection.cursor()


# In[3]:


Database_Creation = "Create database E_COMMERCE"
cursorObject.execute(Database_Creation)
connection.close()


# In[4]:


connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "Raghu#456",
                                     database ="E_COMMERCE")
cursorObject =connection.cursor()


# In[5]:


table_creation_query = """CREATE TABLE supplier (
  SUPP_ID INT PRIMARY KEY,
  SUPP_NAME VARCHAR(50),
  SUPP_CITY VARCHAR(50),
  SUPP_PHONE BIGINT(10)
);


CREATE TABLE customer (
  CUS_ID INT NOT NULL,
  CUS_NAME VARCHAR(20) DEFAULT NULL,
  CUS_PHONE VARCHAR(10),
  CUS_CITY VARCHAR(30),
  CUS_GENDER CHAR,
  PRIMARY KEY (CUS_ID)
);


CREATE TABLE category (
  CAT_ID INT NOT NULL,
  CAT_NAME VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (CAT_ID)
);

CREATE TABLE product (
  PRO_ID INT NOT NULL,
  PRO_NAME VARCHAR(20) DEFAULT NULL,
  PRO_DESC VARCHAR(60) DEFAULT NULL,
  CAT_ID INT NOT NULL,
  PRIMARY KEY (PRO_ID),
  FOREIGN KEY (CAT_ID) REFERENCES category (CAT_ID)
);


CREATE TABLE product_details (
  PROD_ID INT NOT NULL,
  PRO_ID INT NOT NULL,
  SUPP_ID INT NOT NULL,
  PROD_PRICE INT NOT NULL,
  PRIMARY KEY (PROD_ID),
  FOREIGN KEY (PRO_ID) REFERENCES product (PRO_ID),
  FOREIGN KEY (SUPP_ID) REFERENCES supplier (SUPP_ID)
);

CREATE TABLE order_table (
  ORD_ID INT NOT NULL,
  ORD_AMOUNT INT NOT NULL,
  ORD_DATE DATE,
  CUS_ID INT NOT NULL,
  PROD_ID INT NOT NULL,
  PRIMARY KEY (ORD_ID),
  FOREIGN KEY (CUS_ID) REFERENCES customer (CUS_ID),
  FOREIGN KEY (PROD_ID) REFERENCES product_details (PROD_ID)
);

CREATE TABLE rating (
  RAT_ID INT NOT NULL,
  CUS_ID INT NOT NULL,
  SUPP_ID INT NOT NULL,
  RAT_RATSTARS INT NOT NULL,
  PRIMARY KEY (RAT_ID),
  FOREIGN KEY (SUPP_ID) REFERENCES supplier (SUPP_ID),
  FOREIGN KEY (CUS_ID) REFERENCES customer (CUS_ID)
);"""
cursorObject.execute(table_creation_query)



# In[15]:


connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "Raghu#456",
                                     database ="E_COMMERCE")
cursorObject =connection.cursor()


# In[23]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = "SELECT * FROM supplier"
cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["SUPP_ID", "SUPP_NAME", "SUPP_CITY", "SUPP_PHONE"])

# Display the DataFrame
df

# Close the cursor and connection
cursor.close()
connection.close()


# In[27]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = "SELECT * FROM supplier"
cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["SUPP_ID", "SUPP_NAME", "SUPP_CITY", "SUPP_PHONE"])

# Display the DataFrame
df




# In[34]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT CUS_GENDER, COUNT(*) AS NUM_CUSTOMERS
FROM customer
INNER JOIN order_table ON customer.CUS_ID = order_table.CUS_ID
WHERE ORD_AMOUNT >= 3000
GROUP BY CUS_GENDER
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows with only two columns
df = pd.DataFrame(rows, columns=["CUS_GENDER", "NUM_CUSTOMERS"])[["CUS_GENDER", "NUM_CUSTOMERS"]]

# Display the DataFrame
df


# In[36]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT order_table.ORD_ID, product.PRO_NAME
FROM order_table
INNER JOIN product ON order_table.PROD_ID = product.PRO_ID
WHERE order_table.CUS_ID = 2
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["ORD_ID", "PRO_NAME"])

# Display the DataFrame
df


# In[37]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT supplier.*
FROM supplier
INNER JOIN product_details ON supplier.SUPP_ID = product_details.SUPP_ID
GROUP BY supplier.SUPP_ID
HAVING COUNT(DISTINCT product_details.PROD_ID) > 1
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["SUPP_ID", "SUPP_NAME", "SUPP_CITY", "SUPP_PHONE"])

# Display the DataFrame
df


# In[38]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT category.CAT_NAME
FROM order_table
JOIN product ON order_table.PROD_ID = product.PRO_ID
JOIN category ON product.CAT_ID = category.CAT_ID
WHERE order_table.ORD_AMOUNT = (
    SELECT MIN(ORD_AMOUNT)
    FROM order_table
)
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["CAT_NAME"])

# Display the DataFrame
df


# In[39]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT product.PRO_ID, product.PRO_NAME
FROM order_table
JOIN product ON order_table.PROD_ID = product.PRO_ID
WHERE order_table.ORD_DATE > '2021-10-05'
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["PRO_ID", "PRO_NAME"])

# Display the DataFrame
df


# In[40]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT supplier.SUPP_ID, supplier.SUPP_NAME, rating.RAT_RATSTARS, customer.CUS_NAME
FROM rating
JOIN supplier ON rating.SUPP_ID = supplier.SUPP_ID
JOIN customer ON rating.CUS_ID = customer.CUS_ID
ORDER BY rating.RAT_RATSTARS DESC
LIMIT 3
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["SUPP_ID", "SUPP_NAME", "RAT_RATSTARS", "CUS_NAME"])

# Display the DataFrame
df


# In[41]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT CUS_NAME, CUS_GENDER
FROM customer
WHERE CUS_NAME LIKE 'A%' OR CUS_NAME LIKE '%A'
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["CUS_NAME", "CUS_GENDER"])

# Display the DataFrame
df


# In[42]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT CUS_NAME, SUM(ORD_AMOUNT) AS TOTAL_ORDER_AMOUNT
FROM customer
INNER JOIN order_table ON customer.CUS_ID = order_table.CUS_ID
WHERE CUS_GENDER = 'M'
GROUP BY CUS_NAME
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["CUS_NAME", "TOTAL_ORDER_AMOUNT"])

# Display the DataFrame
df


# In[46]:


import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghu#456',
    database='E_COMMERCE'
)

# Create a cursor object
cursor = connection.cursor()

# Execute the SELECT query
select_query = """
SELECT *
FROM customer
LEFT OUTER JOIN order_table ON customer.CUS_ID = order_table.CUS_ID
"""

cursor.execute(select_query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["CUS_ID", "CUS_NAME", "CUS_PHONE", "CUS_CITY", "CUS_GENDER", "ORD_ID", "ORD_AMOUNT", "ORD_DATE", "PROD_ID","CUS_ID"])

# Display the DataFrame
df


# In[ ]:




