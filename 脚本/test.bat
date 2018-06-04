@echo off

rem 接受用户输入文件名保存到filename变量里
set /p filename=请输入文件名:

rem 接受用户输入生成个数保存到num变量里
set /p num=请输入生成个数:

rem 开始循环，设置标记 N=0
set N = 0
rem 设置循环体标记test 
:test
set /a n=%n%+1

rem 输出文件名和序号到 序号.文件名.txt文件内
echo %filename%,%n% >%n%#%filename%.txt

rem 如果n等于需要的个数 跳到最后结束，否则跳到标记test处
if "%n%"=="%num%" goto end
goto test

:end
echo (づ￣ 3￣)づ 搞定~
pause