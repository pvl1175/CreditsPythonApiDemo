git clone https://github.com/CREDITSCOM/CS-API
thrift -gen py -out . ./CS-API/general.thrift
thrift -gen py -out . ./CS-API/api.thrift
python3 -m venv env
chmod +x env/bin/activate
env/bin/activate
pip3 install thrift
pip3 install base58
env/bin/deactivate
