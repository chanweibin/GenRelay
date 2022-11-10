import modbus_tk, serial, time
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


#* Settings for RS485
PORT = "COM7"
PARITY = "N"
BAUDRATE = 9600
STOPBITS = 1
BYTESIZE = 8
TIMEOUT = 1

#* Input changes
bit = 256
channel = 2

#* logger prof
logger = modbus_tk.utils.create_logger("console")

def main():
    
    # start connection
    device = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=BAUDRATE, bytesize=8, parity=PARITY, stopbits=1, xonxoff=0))
    device.set_timeout(5.0)
    device.set_verbose(True)
    
    try:
        output = bit * 3 
        logger.info(device.execute(1, cst.WRITE_SINGLE_REGISTER, channel, output_value=output))
        time.sleep(0.5)
        
    except Exception as E:
        print(E)
        pass
    
if __name__ == "__main__":
    main()