
@echo on

set ANS_PROTOCOL_ROOT=E:\AnsysDev\Protocols
set PYTHONPATH=%ANS_PROTOCOL_ROOT%\packages\python\dpf

set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

call jupyter notebook

 

