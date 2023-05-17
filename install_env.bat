@echo off
::编码utf-8
chcp 65001
::升级pip
python -m pip install --upgrade pip
echo upgradeing pip
timeout 10
python -m venv test_folder
echo.
call %~dp0test_folder\Scripts\activate
echo creating folder
timeout 3
python.exe -m pip install --upgrade pip
echo.
pip install selenium
echo.
pip install openpyxl
echo.
pip install requests
echo.
deactivate