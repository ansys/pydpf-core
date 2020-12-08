
@echo on

set ANSYS_PATH=C:\Program Files\ANSYS Inc\v211\
set DPF_CONFIGURATION=release
set DPF_PATH=C:\Program Files\ANSYS Inc\v211\aisol\bin\winx64\Ans.Dpf.Grpc.exe
set ANS_PROTOCOL_ROOT=D:\AnsysDev\Protocols
set DPF_CORE_PATH=D:\AnsysDev\DPF-Core

set PYTHONPATH=%ANS_PROTOCOL_ROOT%\packages\python\dpf;%DPF_CORE_PATH%

set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

call jupyter lab

 

