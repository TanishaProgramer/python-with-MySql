from logging import exception
import mysql.connector

class User:
    UID=100
    name=''
    age=0
    email=''
    password =''

    def setPassword(self , password):
        self.password = password
         
    def getPassword(self):
        return self.password

    def getUID(self):
        return self.UID
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getEmail(self):
        return self.email
    
    def setUID(self , id):
        self.UID = id

    def setName(self , n):
        self.name=n
    
    def setAge(self , a):
        self.age = a

    def setEmail(self, mail):
        self.email = mail

class SQLConnector:

    def getData(self):
        userData=[]
        cnx = self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        query = 'select email from user'
        mycursor = self.mydb.cursor()
        mycursor = cnx.cursor(buffered=True)
        mycursor.execute('use mydatabase')
        mycursor.execute(query)
        self.mydb.commit()
        return mycursor.fetchall()
    
    def sendData(self ,userData):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        query = "INSERT INTO user (UID, name , age , email , password) VALUES (%s, %s,%s,%s,%s)"
        val = (userData.UID, userData.name , userData.age , userData.email , userData.password)
        mycursor = self.mydb.cursor()
        mycursor.execute('use mydatabase')
        mycursor.execute(query ,val)

        self.mydb.commit()
        print(mycursor.rowcount, "USER CREATED SUCCESS...")
        import emailSender
        print("sending mail...")
        emailSender.sendMail(val)

    def getRowCount(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        mycursor = self.mydb.cursor()
        mycursor.execute("USE mydatabase")
        mycursor.execute("SELECT count(UID) FROM user")
        myresult = mycursor.fetchone()[0]

        return myresult
             

if __name__ == '__main__':
    connector = SQLConnector()
    u = User()

    try:
        u.name=input("ENTER USER NAME : ")
        u.age = int(input("ENTER USER AGE : "))
        u.email = input("ENTER USER EMAIL : ")
        u.UID = u.getUID()+ connector.getRowCount()
        u.password = input("ENTER NEW PASSWORD : ")

        userdata=connector.getData()
        createUser = True

        for email in userdata:
            #print("Email : ",email[0] , " ",u.email)
            if(u.email.strip('\n') == email[0]):
                createUser = False
                break
            else:
                createUser= True

        if(createUser):    
            connector.sendData(u)
        else:
            print("USER ALREADY PRESENT IN DATABASE")  


    except Exception as exception:
        print(exception)


