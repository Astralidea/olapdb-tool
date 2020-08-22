import argparse
import pymysql

parser = argparse.ArgumentParser(description="dorisdump  Ver 0.1", add_help=False)
parser.add_argument('--host', '-h', help='Connect to host.')
parser.add_argument('--port', '-P', type=int, help='Port number to use for connection.')
parser.add_argument('--user', '-u', help='User for login.')
parser.add_argument('--password', '-p', help='Password to use when connecting to server.')
parser.add_argument('--database', '-d', help='One database name.')
args = parser.parse_args()

host = '127.0.0.1'
port = 9030
user = ''
password = ''
database = 'information_schema'

if args.host:
    host = args.host
if args.port:
    port = int(args.port)
if args.user:
    user = args.user
if args.password:
    password = args.password
if args.database:
    database = args.database

db = pymysql.connect(host=host, port=port, user=user,
                     password=password, db=database)
cursor = db.cursor()
all_dump_idx = cursor.execute("show tables;")
# print("Database {} has {} table(s)".format(database, all_dump_idx))

tables = cursor.fetchall()

cur_dump_idx = 0
for table in tables:
    cur_dump_idx += 1
#    print("Progressing {}/{}. current table is {}".format(cur_dump_idx, all_dump_idx, table[0]))
    cursor.execute("show create table {};".format(table[0]))
    meta_info = cursor.fetchall()
    print(meta_info[0][1])

# print("Database {} dump successful!".format(database))
db.close()