
@echo on

rem set ANSYS_PATH=C:\Program Files\ANSYS Inc\v211\
rem set DPF_CONFIGURATION=release
rem set DPF_PATH=C:\Program Files\ANSYS Inc\v211\aisol\bin\winx64\Ans.Dpf.Grpc.exe
rem set ANS_PROTOCOL_ROOT=D:\AnsysDev\Protocols
rem set DPF_CORE_PATH=D:\AnsysDev\DPF-Core

rem set PYTHONPATH=%ANS_PROTOCOL_ROOT%\packages\python\dpf;%DPF_CORE_PATH%

rem Assume DPF server is already running
rem set DPF_START_SERVER=False
rem set DPF_IP=10.<...>

rem set DPF_PORT=50054

set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

call jupyter lab

rem testsync
 

