@echo off

rem �����û������ļ������浽filename������
set /p filename=�������ļ���:

rem �����û��������ɸ������浽num������
set /p num=���������ɸ���:

rem ��ʼѭ�������ñ�� N=0
set N = 0
rem ����ѭ������test 
:test
set /a n=%n%+1

rem ����ļ�������ŵ� ���.�ļ���.txt�ļ���
echo %filename%,%n% >%n%#%filename%.txt

rem ���n������Ҫ�ĸ��� �����������������������test��
if "%n%"=="%num%" goto end
goto test

:end
echo (�ţ� 3��)�� �㶨~
pause