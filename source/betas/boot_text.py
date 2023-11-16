import sys
import time
import colorama
from colorama import Fore

print(f"""{Fore.MAGENTA}
                                        _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
 ^^
{Fore.WHITE}
""")
def loading_bar(loading_steps):
    total_length = 40  # Total length of the loading bar
    fill_char = f'{Fore.WHITE}█'   # Character used to fill the loading bar
    empty_char = f'{Fore.MAGENTA}-'  # Character used for empty portion of the loading bar
    
    progress = 0
    while progress <= 100:
        filled_length = int(total_length * progress / 100)
        empty_length = total_length - filled_length
        
        bar = fill_char * filled_length + empty_char * empty_length
        percentage = f'{Fore.WHITE}{progress}%'
        
        sys.stdout.write('\r' + f'{Fore.MAGENTA}|{bar}{Fore.MAGENTA}| {percentage}')
        sys.stdout.flush()
        
        progress += loading_steps
        time.sleep(0.1)

print(Fore.MAGENTA + f"[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE}> Inintializing Sentry, please wait.", Fore.WHITE)
loading_bar(2)

print(Fore.MAGENTA + f"\n[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE}> Looking up directories.", Fore.WHITE)
loading_bar(10)