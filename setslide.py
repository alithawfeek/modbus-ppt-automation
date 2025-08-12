import time
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('localhost', port=5020)
client.connect()

for slide in [1, 2, 3]:
    client.write_register(1, slide)
    print(f"Set slide to {slide}")
    time.sleep(15)  # Wait 5 seconds between slides

client.close()
