
@echo on

set ANSYS_PATH=C:\Program Files\ANSYS Inc\v212\
set DPF_CONFIGURATION=release
set DPF_PATH=C:\Program Files\ANSYS Inc\v212\aisol\bin\winx64\Ans.Dpf.Grpc.exe
set CODEDV_ROOT=D:\AnsysDev\CodeDV
set ANS_PROTOCOL_ROOT=D:\AnsysDev\Protocols

set OPERATORS_DATABASE_PATH = %CODEDV_ROOT%\DataProcessing\Ans.Dpf.Grpc\Python\
set PYTHONPATH=%ANS_PROTOCOL_ROOT%\packages\python\dpf;%CODEDV_ROOT%\DataProcessing\Ans.Dpf.Grpc\Python;%OPERATORS_DATABASE_PATH%

set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

call jupyter lab

 

