# ModBus implementation to control PPT slides
- modbus_server.py – Simulates a Modbus server locally holding modbus values.
- setslide.py – Sends Modbus values (1, 2, 3) to simulate control input.
- modbuspptcontrol.py – Reads Modbus values and switches slides in a presentation (The presentation I have is 3 slides).

### Dependencies to install
- ```bash
    pip install pypiwin32
    ```
- Check the name of the ppt in 'modbuspptcontrol.py' script

### Steps to run
- Open a Windows powershell tab and navigate to the directory where this repository lives and run:
```bash
        python modbus_server.py
    ```
- To check if the port is running:
```bash
        netstat -ano | findstr :502
        ```
- Open another powerhsell tab and run:
```bash
        python modbuspptcontrol.py
        ```
- Similarly open another tab to run the script to change the slides:
```bash
        python setslide.py
        ```
