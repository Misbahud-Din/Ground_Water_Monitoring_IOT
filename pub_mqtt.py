import random, time
import paho.mqtt.client as mqtt
import json
 
broker_address = "127.0.0.1" 
# broker_address = "example.com" 
client = mqtt.Client("Publisher")
client.connect(broker_address)


while (True):

  msg = {
  "sensor": {
    "water": {
      "level": random.random()*100,
      "ph": random.random()*100
    },
    "ground": {
      "moisture": random.random()*100
    } 
  }
}
  msg_json = json.dumps(msg)
  time.sleep(1)
  client.publish("sensor/data", msg_json)
  print(msg_json)
