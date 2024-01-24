import time,hashlib,os.path,mysql.connector
from colorama import Fore

def consolePrefix (terminal_state): return f'{Fore.MAGENTA}[{Fore.WHITE}{terminal_state}{Fore.MAGENTA}]{Fore.WHITE}> '
def sqlConnector(secret):
    mydb = mysql.connector.connect(
                host = "127.0.0.1",
                port = 8080,
                user = "root",
                password = secret,
                database = "token_storage"
            )
    mycursor = mydb.cursor()

def main():

    print(Fore.MAGENTA + 'SENTRY ADMINISTRATOR TERMINAL | ' + Fore.WHITE + '2023-2024\nProgrammed by nikkeisadev. github.com/nikkeisadev\n')
    time.sleep(2)
    
    secret = input(consolePrefix('login_sql')+"Root password: ")

    try:
        sqlConnector(secret)
        pass
    except:
        print(consolePrefix('err')+"Wrong root password, exiting...")
        time.sleep(2), exit()
    print(consolePrefix('menu')+ Fore.WHITE + f"\n\nWelcome to the administrator terminal!\nHere are the commands to manage the database." + Fore.MAGENTA + f"\n Register a new user => user register <name> <password>\n Remove a user => user delete <name>\n Check all activity => get activity\n Requests from Clients => get requests\n{Fore.RED} Exit from terminal => exit\n")
    
    def menuInput():
        mydb = mysql.connector.connect(
                host = "127.0.0.1",
                port = 8080,
                user = "root",
                password = secret,
                database = "token_storage"
            )
        mycursor = mydb.cursor()
        menu = input(consolePrefix('menu'))
        try:
            if menu.startswith("user register"):
                user, register, name, password = menu.split(" ")
                sql = "INSERT INTO user_token (user_name, user_token) VALUES (%s, %s)"
                val = (name, hashlib.sha256(bytes(password, encoding="utf-8")).hexdigest())
        
                mycursor.execute(sql, val)
                mydb.commit()
                print(consolePrefix('success')+f"Registered with credentials: {Fore.MAGENTA}[{name}|{password}]")
                menuInput()

            elif menu.startswith("user delete"):
                user, delete, name = menu.split()
                print(name)
                sql = "DELETE FROM user_token WHERE user_name = %s"
                val = (name, )  # Note the comma after 'name' to create a tuple
                mycursor.execute(sql, val)
                mydb.commit()
                print(consolePrefix('deleted') + f"{Fore.RED}Deleted user: {Fore.MAGENTA}[{name}]")
                menuInput()

            elif menu == "get activity":
                mycursor.execute("SELECT * FROM report_table")
                result = mycursor.fetchall()
                print(Fore.BLUE + 'Querying the database...\n' + Fore.MAGENTA + 'REPORTS FROM CLIENTS:')
                for row in result:
                    row_items = ', '.join(row)
                    print(Fore.YELLOW + row_items)

                print(Fore.GREEN + 'Querying the database was successful!')
                menuInput()
            
            elif menu == "get requests":
                mycursor.execute("SELECT request_table, username_table FROM token_requests_table")
                result = mycursor.fetchall()
                print(Fore.BLUE + 'Querying the database...\n' + Fore.MAGENTA + 'TOKEN REQUESTS FROM CLIENTS:')
                for row in result:
                    row_items = ', '.join(row)
                    print(Fore.YELLOW + row_items)

                print(Fore.GREEN + 'Querying the database was successful!')
                menuInput()
                            
            elif menu == 'exit':
                exit()
            else:
                print(consolePrefix('err') + f"{Fore.RED}Wrong command, or error in console.")
                menuInput()
        except:
            print(consolePrefix('err') + f"{Fore.RED}Wrong command, or error in console.")
            menuInput()
    menuInput()
main()