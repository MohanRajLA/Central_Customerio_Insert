
import pymysql
import ConfigParser
import customeriopostfunc
from customerio import CustomerIO


# Function to provide DB connection details
def py_db(HOST, USERNAME, PASSWD, PORT, DB_NAME):
    conn = pymysql.connect(HOST, user=USERNAME,
                           passwd=PASSWD, db=DB_NAME, connect_timeout=5)
    cursor=conn.cursor()
    return conn,cursor

#SQL Query to fetch the results from the DB
def queryData(conn,cursor,query):
    cursor.execute(query)
    stmt=cursor.fetchall()
    return stmt

def lambda_handler(event,context):
    config = ConfigParser.RawConfigParser()
    config.read('configcustomer.properties')
    conn, cursor = py_db(config.get('db-config', 'HOST'), config.get('db-config', 'USERNAME'),
                         config.get('db-config', 'PASSWD'), config.get('db-config', 'PORT'),
                         config.get('db-config', 'DB_NAME'))


    site_id=config.get('customerio-config', 'site_id')
    api_key=config.get('customerio-config', 'api_key')

    # write DB contents into csv file and inserting into customer.io
    queryprofileStmt=queryData(conn, cursor, config.get('query-config', 'profile'))
    cio=CustomerIO(site_id, api_key)
    customeriopostfunc.customerIOProfileAPICall(queryprofileStmt,cio)
    cursor.close()
    return "Success"


