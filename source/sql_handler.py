import mysql.connector
import hashlib
import time

subprefix = """
  ______ _________          _     _ _______ _______ ______  _       _______ ______    
 / _____| ____ |(_)        ( )   ( |_______|_______|______)(_)     (_______|_____ \   
( (____ | |  | | _         | |___| |_______ _     _ _     _ _       _____   _____) )  
 \____ \| |  | || |        |  ___  |  ___  | |   | | |   | | |     |  ___) |  __  /   
 _____) ) |__| || |_____   | |   | | |   | | |   | | |__/ /| |_____| |_____| |  \ \   
(______/ \______)_______)  |_|   |_|_|   |_|_|   |_|_____/ |_______)_______)_|   |_|  

                        <= The main SQL connection handler =>
                <= Writing, and reading data from the SQL server =>
                            Made with love, by: Nikke
"""
print(subprefix)

EMPTUM_CONSOLE_PREFIX = '[EMPTUM]> '
usersList = []
hashList = []

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = 8008,
    user = "root",
    password = "emptum-chan",
    database = "token_storage"
)
mycursor = mydb.cursor()

def connectingDatabase():
    print(f'{EMPTUM_CONSOLE_PREFIX}Trying connection to the SQL database!')
    if mydb.is_connected:
        print(f'{EMPTUM_CONSOLE_PREFIX}Connected to {mydb._host}:{mydb._port} with {mydb._user}!')
    else:
        print(f'{EMPTUM_CONSOLE_PREFIX}Connection failed! Retrying at {mydb._host}:{mydb._port} with {mydb._user}!')
        time.sleep(2)
        connectingDatabase()

def insertingToken():
    sql = "INSERT INTO user_token (user_name, user_token) VALUES (%s, %s)"
    val = [
        ('Barta Attila', 'f74a79401b956093c283e579097c08fd501cc5965564248e7d525a28bcbbfdb7'),
        ('Varga Tamás', '7158f341e1c6334c7664b27d34a34f9eb5febfc4563885369e193024c3c84cef'),
        ('Péter Miklós', '26a5130d84b621043ec0dafe2db5d66905d815ad7986944fc869d83e02eaebc7'),
        ('Nemes Tamás', '7820dab3c2d7384c4a5433585f89bc774b02ecb38535381bd5907b2226eaa025'),
        ('Hagymási Gyula', '2af8128a8d37459cfe27b2a34e8d8a803b743993d921484b2f41fdf96aa8e23b'),
    ]

    mycursor.executemany(sql, val)
    mydb.commit()

    print(f'{EMPTUM_CONSOLE_PREFIX} Table updated!')

def readingTable():
    mycursor.execute("SELECT user_name FROM user_token")
    myresult = mycursor.fetchall()

    for x in myresult:
        nameString = ''
        nameString = str(x[0])
        print(f'{EMPTUM_CONSOLE_PREFIX}Registered user found: {nameString}!')
        usersList.append(nameString)
    
    mycursor.execute("SELECT user_token FROM user_token")
    myresult = mycursor.fetchall()

    for x in myresult:
        loginTokenHash = ''
        loginTokenHash = str(x[0])
        hashList.append(loginTokenHash)

def basicLoginDefinition():
    username = str(input(f'{EMPTUM_CONSOLE_PREFIX}Username: '))
    login_token_input = str(input(f'{EMPTUM_CONSOLE_PREFIX}Login token: '))

    hashedTokenInput = hashlib.sha256(bytes(login_token_input, encoding="utf-8")).hexdigest()

    if usersList.__contains__(username) and hashList.__contains__(hashedTokenInput):
        print(f'Seems to be legit...')
        
        userIndex = usersList.index(username)
        hashIndex = hashList.index(hashedTokenInput)
        
        if userIndex == hashIndex:
            print(f'{EMPTUM_CONSOLE_PREFIX} Login Successful as {username}!')
    else:
        print(f'{EMPTUM_CONSOLE_PREFIX}The login credentials were wrong! ')
        basicLoginDefinition()
def refreshingTokenColumm():
    sql = "UPDATE user_token SET user_token = '7158f341e1c6334c7664b27d34a34f9eb5febfc4563885369e193024c3c84cef' WHERE user_token = 'f74a79401b956093c283e579097c08fd501cc5965564248e7d525a28bcbbfdb7'"
    mycursor.execute(sql)
    mydb.commit()

def refreshingTokenColummAgain():
    sql = "UPDATE user_token SET user_token = 'f74a79401b956093c283e579097c08fd501cc5965564248e7d525a28bcbbfdb7' WHERE user_token = '7158f341e1c6334c7664b27d34a34f9eb5febfc4563885369e193024c3c84cef'"
    mycursor.execute(sql)
    mydb.commit()

def chooseTokenRefresh():
    if int(input(f'{EMPTUM_CONSOLE_PREFIX}Choose a token refresh type >[ 1 ; 2 ]: ')) == 1:
        refreshingTokenColumm()
    else:
        refreshingTokenColummAgain()

print(mycursor.rowcount, "record(s) affected")
connectingDatabase()
readingTable()
chooseTokenRefresh()