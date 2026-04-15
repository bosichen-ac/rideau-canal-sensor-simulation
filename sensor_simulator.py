import time
import random
import os
import json
import threading
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv

load_dotenv()
sensor_dow_s_lake = os.getenv("DOW_S_LAKE")
sensor_fifth_ave = os.getenv("FIFTH_AVENUE")
sensor_nac = os.getenv("NAC")

sensors = [
  { "location": "Dow's Lake", "conn_str": sensor_dow_s_lake }, 
  { "location": "Fifth Avenue", "conn_str": sensor_fifth_ave}, 
  { "location": "NAC", "conn_str": sensor_nac}
]

def generate_sensor_data(location):
  return {
    "location": location,
    "timestamp": datetime.now().isoformat(),
    "iceThickness": round(random.uniform(25, 40), 2),
    "surfaceTemp": round(random.uniform(-15, 5), 2),
    "snowAccumulation": round(random.uniform(0, 15), 2),
    "externalTemp": round(random.uniform(-25, 0), 2)
  }


def run_sensor(sensor):
  client = IoTHubDeviceClient.create_from_connection_string(sensor["conn_str"])
  print(f"{sensor["location"]} started...")

  count = 0 # just 5 sets of data for dev

  try:
    while count < 5:
      data = generate_sensor_data(sensor["location"])
      message = Message(json.dumps(data))
      client.send_message(message)
      print(f"[{sensor["location"]}] Sent: {data}")
      count+=1 # just 5 sets of data for dev
      time.sleep(10)
  except KeyboardInterrupt:
    print(f"{sensor["location"]} stopped...")
  finally:
    client.disconnect()


def main():
  print("Starting...?")

  threads = []

  for sensor in sensors:
    thread = threading.Thread(target=run_sensor, args=(sensor,))
    thread.start()
    threads.append(thread)

  for thread in threads:
    thread.join()

  print("Done...?")


if __name__ == "__main__":
  main()