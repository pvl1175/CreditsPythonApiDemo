from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TSocket import TSocket
import base58

from gen.api.API import Client

publicKey = 'H5ptdUUfjJBGiK2X3gN2EzNYxituCUUnXv2tiMdQKP3b'
publicKeyBytes = base58.b58decode(publicKey)

try:

    tr = TSocket('127.0.0.1', 9090)
    protocol = TBinaryProtocol(tr)
    client = Client(protocol)

    tr.open()

    balance = client.BalanceGet(publicKeyBytes, 0)
    print(balance)

    transactionGetResult = client.TransactionsGet(publicKeyBytes, 0, 5)
    print(transactionGetResult)

except:
    print("Oops. Unexpected error.")


