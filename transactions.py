import logging
import asyncio
import sys

from kademlia.network import Server

if len(sys.argv) < 4:
    print("Not enough Information for transaction")
    sys.exit(1)

#Set up an asyncio loop to use functions from the network
loop = asyncio.get_event_loop()
loop.set_debug(True)

#set up a node to connect to the network to make transactions
server = Server()
server.listen(8471)
#Connected to the network
ip = "128.153.187.178"
bootstrap_node = (ip, 8468)
loop.run_until_complete(server.bootstrap([bootstrap_node]))

#Get current string of transactions
trans_key = "transactions"
trans_ret = loop.run_until_complete(server.get(trans_key))
#Send the transaction to the waiting pool
add_trans = str(sys.argv[1]) + " Sends " + str(sys.argv[2]) + " Coin to " + str(sys.argv[3]) + " : "
transactions = str(trans_ret) + add_trans
loop.run_until_complete(server.set(trans_key, transactions))
#Close the node
server.stop()
loop.close()