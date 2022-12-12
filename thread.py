import threading
import random
import datetime
import mysql.connector
from mysql.connector import Error
class DataUploadThread(threading.Thread):

    def __init__(self,branch_id , variant_id , number_of_codes, cd_id ):
        self.cd_id = cd_id
        self.branch_id = branch_id
        self.variant_id = variant_id
        self.number_of_codes = number_of_codes
        threading.Thread.__init__(self)
    
    def run(self):
        i=0
        while i<self.number_of_codes:
            temp_code=''
            code=str(self.branch_id)+str(self.variant_id)
            temp_code+=code
            remaining_length=10-len(temp_code)
            numerical_code=temp_code+str(random.randint(10**(remaining_length-1), (10**remaining_length)-1))
            numerical_code=int(numerical_code)
            today=datetime.datetime.today().strftime('%Y-%m-%d')
            try:
                connection = mysql.connector.connect(host='localhost',database='test_db',user='root',password='Password&#123')
                if connection.is_connected():
                    cursor = connection.cursor()
                    if self.branch_id == 1:
                        mySql_insert_query = "INSERT INTO FourSquare(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)"
                    elif self.branch_id == 2:
                        mySql_insert_query = "INSERT INTO RedandWhite(cd_id,branch,variant,code,status,create_date) values( %s, %s, %s, %s, %s, %s)" 
                    elif self.branch_id == 3:
                        mySql_insert_query = "INSERT INTO CavendersGreen(cd_id,branch,variant,code,status,create_date) values( %s, %s, %s, %s, %s, %s)" 
                    elif self.branch_id == 4:
                        mySql_insert_query = "INSERT INTO CavendersGold(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)" 
                    elif self.branch_id == 5:
                        mySql_insert_query = "INSERT INTO CavendersSpecial(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)"
                    elif self.branch_id == 6:
                        mySql_insert_query = "INSERT INTO Stellar(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)"
                    elif self.branch_id == 7:
                        mySql_insert_query = "INSERT INTO NorthPole(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)"
                    elif self.branch_id == 8:
                        mySql_insert_query = "INSERT INTO Tipper(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)"
                    elif self.branch_id == 12:
                        mySql_insert_query = "INSERT INTO FlavourandLights(cd_id,branch,variant,code,status,create_date) values(%s, %s, %s, %s, %s, %s)"
                    val=(self.cd_id,self.branch_id,self.variant_id,numerical_code,1,today)
                    cursor.execute(mySql_insert_query,val)  
                    connection.commit()  
                    i+=1
                    cursor.close()
            except mysql.connector.Error as error:
                pass
            finally:
                if connection.is_connected():
                    connection.close()