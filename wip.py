import websocket
import json
#import asyncio

params = json.dumps({"method": "SUBSCRIBE",
  "params": [
    "avaxusdt@aggTrade"
  ],
  "id": 1})
ws = websocket.WebSocket()
ws.connect("wss://stream.binance.com:9443/ws")
ws.send(params)
sub_message = ws.recv()
print(sub_message)


while __name__ == "__main__":
    response = ws.recv()
    response = json.loads(response)
    amt = float(response["q"])
    if amt > 10.0:
        f = open("trades.txt", "a")
        f.write(str(response) + "\n")
        f.close()
        if response["m"] == True:
          print(f"Sell for {amt}")
        else:
          print(f"Buy for {amt}")
      