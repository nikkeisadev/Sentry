import os

EMPTUM_CONSOLE_PREFIX = '[EMPTUM]> '
path = "C://Users//Nikke//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//"
ss_list = os.listdir(path)
illegalFileInStartup = False

print(f'{EMPTUM_CONSOLE_PREFIX}Found files in startup folder: {ss_list}\n{EMPTUM_CONSOLE_PREFIX}Start removing illegal files...')
for file in ss_list:
    if 'desktop.ini' in file: pass
    else:
        print(f'{EMPTUM_CONSOLE_PREFIX}{file} found, deleted!') 
        illegalFileInStartup = True
        os.remove(path + file)
if illegalFileInStartup != True: print(f'{EMPTUM_CONSOLE_PREFIX}No illegal file(s) found in Startup folder!') 