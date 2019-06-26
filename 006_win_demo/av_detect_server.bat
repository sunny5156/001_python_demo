@echo off  
call conda activate openvino_py3
call C:/Intel/computer_vision_sdk/bin/setupvars.bat
call python D:/02_av_object_detection/deploy/app.py  

pause