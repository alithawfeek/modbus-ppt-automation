from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock

print("Modbus server starting on port 5020")

# Create 10 holding registers, with register 0 set to 1
data_block = ModbusSequentialDataBlock(0, [1] + [0]*9)

# Store the holding registers
store = ModbusSlaveContext(hr=data_block)

# Create a Modbus server context
context = ModbusServerContext(slaves=store, single=True)

# Start the server on localhost at port 5020
StartTcpServer(context, address=("localhost", 5020))
