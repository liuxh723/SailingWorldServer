@echo off
taskkill /f /t /im guiconsole.exe

set curpath=%~dp0

cd ..
set KBE_ROOT=%cd%
set KBE_RES_PATH=%KBE_ROOT%/kbe/res/;%curpath%/;%curpath%/scripts/;%curpath%/res/
set KBE_BIN_PATH=%KBE_ROOT%/kbe/bin/server/

set uid=%random%%%32760+1

cd %KBE_ROOT%/kbe/tools/server/guiconsole/
start guiconsole.exe