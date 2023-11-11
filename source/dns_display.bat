@echo off

:DISPLAY

ipconfig /displaydns > dns.hs
timeout /nobreak 5 >nul 2>&1
sort history.txt /o history.txt

goto :DISPLAY