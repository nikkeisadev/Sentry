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
    print(consolePrefix('menu')+ Fore.WHITE + f"Welcome to the administrator terminal!\nHere are the commands to manage the database." + Fore.MAGENTA + f"\nRegister a new user => user register <name> <password>\nRemove a user => user delete <name>\nCheck all activity => get activity\n{Fore.RED}Exit from terminal => exit")
    
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
                print(Fore.BLUE + 'Querying the database...')
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