from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('localhost', port=5020)
if not client.connect():
    print("Cannot connect to Modbus server")
    exit()

response = client.read_holding_registers(1, 1)
if response.isError():
    print("Error reading register 1")
else:
    print(f"Value at register 1: {response.registers[0]}")

client.close()
