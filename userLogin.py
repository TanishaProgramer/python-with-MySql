from logging import log
from UserSignUp import User
import mysql.connector
class LoginUser:    

    def getUserData(self ,user):
        cnx = self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        mycursor = self.mydb.cursor()
        mycursor = cnx.cursor(buffered=True)
        id= str(user.UID).strip('\n')
        password = str(user.password).strip('\n')
        query = "select * from user where UID={} and password = '{}'".format(id , password)
        #print(query)
        mycursor.execute('use mydatabase')
        mycursor.execute(query )

        self.mydb.commit()
        output= mycursor.fetchall()
        return output

    def checkUserData(self , user):
        userData = self.getUserData(user)
        if(userData != None):
            print("USER LOGGED IN...")
            print('UID: ',userData[0][0])
        return userData

    def login(self):
        print('------- USER LOGIN -------')
        user = User()
        user.UID = int(input("ENTER UID"))
        user.password = input("ENTER PASSWORD")
        userData = self.checkUserData(user)

if __name__ == '__main__':
    logUser = LoginUser()
    logUser.login()