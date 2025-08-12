import time
import win32com.client
from pymodbus.client.sync import ModbusTcpClient

# Connecting to Modbus server
client = ModbusTcpClient('localhost', port=5020)

if not client.connect():
    print("Could not connect to Modbus server.")
    exit()

# Starting PPT
ppt = win32com.client.Dispatch("PowerPoint.Application")
ppt.Visible = True

# PPT file path
ppt_file = r"C:\Users\me4mamt\Downloads\testformodbus.pptx"
presentation = ppt.Presentations.Open(ppt_file)

# Starting slideshow
presentation.SlideShowSettings.Run()

print("Listening for Modbus values (1 to 3)... Press Ctrl+C to stop.")

last_slide = 0  #Track last slide to avoid repeats

try:
    while True:
        response = client.read_holding_registers(1, 1)

        if not response.isError():
            slide_number = response.registers[0]
            print("Modbus value:", slide_number)

            if slide_number in [1, 2, 3] and slide_number != last_slide:
                try:
                    ppt.SlideShowWindows(1).View.GotoSlide(slide_number)
                    print(f"Switched to slide {slide_number}")
                    last_slide = slide_number

                    # Reset Modbus register to 0
                    client.write_register(1, 0)

                except:
                    print("Slideshow not running. Restarting")
                    presentation.SlideShowSettings.Run()
        else:
            print("Error reading Modbus")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopped by user")

client.close()
