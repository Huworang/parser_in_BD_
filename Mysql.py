from types import EllipsisType
import pymysql, time, re
from Data import table_names_fields


class Working_database(object):

    def __init__(self):

        #self.list_types = [" int, ", " varchar(255), ", " int PRIMARY KEY, "]

        self.dict_fields = dict()

        for name in table_names_fields:
            self.dict_fields[name] = re.sub(r'\d, ', ', ', table_names_fields[name])
            

        try:
            self.connection = pymysql.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '228666Labbjoil8',
                database = 'Parsing',
                cursorclass = pymysql.cursors.DictCursor
            )
            print("The connection to the database is established")
            
        except:
            print("Error: The database is not responding")
            



    def Create_db(self):

        for fields_string in table_names_fields:

            fields = table_names_fields[fields_string].replace("*0", " int").replace("*1", " varchar(255)").replace("*2", " int PRIMARY KEY")
            
            create_table = f"CREATE TABLE {fields_string} ({fields});"

            try:
                with self.connection.cursor() as cr:
                    #create_table = f"CREATE TABLE {name_db} (id int, name varchar(255), city varchar(255), phone_number varchar(255), email  varchar(255), PRIMARY KEY (id));"
                    cr.execute(create_table)
                    print(f"Table '{fields_string}' create")

            except pymysql.err.OperationalError:
                print(f"Table '{fields_string}' already exists")




    def Add_data(self, name_table, list_vars):
        
        values_list = ", ".join(list_vars)
        fields = re.sub(r'\*\d', '', table_names_fields[name_table])

        with self.connection.cursor() as cr:
            insert = f"INSERT INTO {name_table} ({fields}) VALUES ({values_list})"
            cr.execute(insert)
            self.connection.commit()





    def Close_connection(self):
        self.connection.close()

