git clone https://github.com/CREDITSCOM/CS-API
thrift -gen py -out . ./cs-api/general.thrift
thrift -gen py -out . ./cs-api/api.thrift
python -m venv env
env/Scripts/activate
pip install thrift
pip install base58
