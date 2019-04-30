rmdir /S /Q CS-API
rmdir /S /Q api
rmdir /S /Q general
rmdir /S /Q env

git clone https://github.com/CREDITSCOM/CS-API
thrift -gen py -out . .\cs-api\general.thrift
thrift -gen py -out . .\cs-api\api.thrift
python -m venv env
call env\Scripts\activate.bat
pip install thrift
pip install base58
call env\Scripts\deactivate.bat
