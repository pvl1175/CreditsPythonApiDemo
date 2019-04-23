from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TSocket import TSocket
import base58

from api.API import Client

publicKey = '[your public key]'

publicKeyBytes = base58.b58decode(publicKey)

try:

   tr = TSocket('[your node ip address]', 9090)
   protocol = TBinaryProtocol(tr)
   client = Client(protocol)
   tr.open()

   balance = client.WalletBalanceGet(publicKeyBytes)
   print(balance)

   transactionGetResult = client.WalletTransactionsCountGet(publicKeyBytes)
   print(transactionGetResult)

except:

   print("Oops. Unexpected error.")