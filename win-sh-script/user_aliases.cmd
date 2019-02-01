;= @echo off
;= rem Call DOSKEY and use this file as the macrofile
;= %SystemRoot%\system32\doskey /listsize=1000 /macrofile=%0%
;= rem In batch mode, jump to the end of the file
;= goto:eof
;= Add aliases below here
e.=explorer .
gl=git log --oneline --all --graph --decorate  $*
ls=ls --show-control-chars -F --color $*
pwd=cd
clear=cls
history=cat "%CMDER_ROOT%\config\.history"
unalias=alias /d $1
vi=vim $*
cmderr=cd /d "%CMDER_ROOT%"

;= ================================================================
;= ********** do not use the fuckin none-ascii character **********
;= ================================================================

;= ================================================================
;= path & dir
;= ================================================================
..=cd ..
...=cd ../..
....=cd ../../..
.....=cd ../../../..
.....=cd ../../../../..
~=c: && cd c:\Users\dell\
home=c: && cd c:\Users\dell\
cc=c: && cd c:\
dd=d: && cd d:\
pacofuture=c: && cd c:\pacofuture\
personal=c: && cd c:\personal_project\

;= ================================================================
;= sys
;= ================================================================
ll=ls -al
open=start
edit=start notepad++ $1
hosts=start notepad++ c:\Windows\System32\drivers\etc\hosts
showinexplorer=start .

;= ================================================================
;= git
;= ================================================================
gb=git branch

;= ================================================================
;= shell
;= ================================================================
reloadshell=alias/reload
editshell=start notepad++ c:\Users\dell\Downloads\config\user-aliases.cmd
importshell=cat c:\personal_project\fee\win-sh-script\user_aliases.cmd > c:\Users\dell\cmder_mini\config\user_aliases.cmd && alias/reload
exportshell=cat c:\Users\dell\cmder_mini\config\user_aliases.cmd > c:\personal_project\fee\win-sh-script\user_aliases.cmd

;= ================================================================
;= local server
;= ================================================================
server=http-server
serverhere=http-server -c-1
adminlte=start chrome "http://localhost:9720/pages/UI/icons.html" && http-server -p 9720 "C:\pacofuture\AdminLTE"
navserver=http-server -sp 80 "C:\Users\dell\Desktop"

;= ================================================================
;= virtual machine
;= ================================================================
vm=ssh ho@vm
sendtovm=scp $1 ho@vm:$2
sendfromvm=scp ho@vm:$1 $2
sendfoldertovm=scp -r $1 ho@vm:$2
sendfolderfromvm=scp -r ho@vm:$1 $2
vmstart=vmrun -T player start "C:\Users\dell\Documents\Virtual Machines\Ubuntu Server 170717\Ubuntu Server 170717.vmx" nogui
vmsuspend=vmrun suspend "C:\Users\dell\Documents\Virtual Machines\Ubuntu Server 170717\Ubuntu Server 170717.vmx" hard
vmreset=vmrun reset "C:\Users\dell\Documents\Virtual Machines\Ubuntu Server 170717\Ubuntu Server 170717.vmx" hard
vmstop=vmrun stop "C:\Users\dell\Documents\Virtual Machines\Ubuntu Server 170717\Ubuntu Server 170717.vmx" hard

;= ================================================================
;= python
;= ================================================================
rmpipenv=pipenv --rm && rm -f Pipfile Pipfile.lock
newpipenv=bash -c 'if [ -e "/c/Python/$1/python.exe" ]; then pipenv --python "C:/Python/$1/python.exe"; sed -i "s/pypi.org\/simple/mirrors.aliyun.com\/pypi\/simple\//g" Pipfile; if [ -e "requirements.txt" ]; then echo "detect requirements.txt installing..."; pipenv install -r requirements.txt; fi; cat Pipfile; pipenv graph; pipenv run Python -V; else echo "version $1 not found,download: https://npm.taobao.org/mirrors/python/$1/"; fi'

;= ================================================================
;= netstat
;= ================================================================
ping114=ping 114.114.114.114 -t
pingali=ping 223.5.5.5 -t
pingbaidu=ping www.baidu.com -t
