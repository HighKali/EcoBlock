#!/usr/bin/env python3
import time, os
from eco_zsona_miner import mine_block
from eco_zsona_syncnet import broadcast_chain

LOG = "wallet/miner.log"

def loop_mine():
    while True:
        result = mine_block()
        print(result)
        with open(LOG, "a") as f:
            f.write(result + "\n")
        broadcast_chain()
        time.sleep(30)

if __name__ == "__main__":
    loop_mine()
