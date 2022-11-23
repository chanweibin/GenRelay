import modbus_tk, serial, time
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


# #* Settings for RS485
# PORT = "COM6"
# PARITY = "N"
# BAUDRATE = 9600
# STOPBITS = 1
# BYTESIZE = 8
# TIMEOUT = 5

# #* Input changes
# bit = 256
# channel = 0
# # address = 40001 + channel
# slaveid = 1

# #* logger prof
# logger = modbus_tk.utils.create_logger("console")

# def connect():
#     pass

# # def write(device, channel:int, value:int):
#     # device.execute(slaveid, cst.WRITE_SINGLE_REGISTER, channel, output_value=value)


# def main():
    
#     # start connection
#     rs845 = serial.Serial(port=PORT, baudrate=BAUDRATE, bytesize=8, parity=PARITY, stopbits=1, xonxoff=0)
#     device = modbus_rtu.RtuMaster(rs845)
#     device.set_timeout(5.0)
#     device.set_verbose(True)
    
#     try:
#         output = bit * 8
#         logger.info(device.execute(slaveid, cst.WRITE_SINGLE_REGISTER, channel, output_value=output))
#         logger.info(device.execute(slaveid, cst.READ_HOLDING_REGISTERS, 0, 5))
#         time.sleep(0.5)
        
    
    
#     except Exception as e:
#         print("Exception: ", end=": ")
#         print(e)
#         pass
        
#     except modbus_tk.modbus.ModbusError as E:
#         print("Modbus Exception ", end=": ")
#         print(E)
#         pass
    
#     device.close()


slaveid = 1
bitsize = 256
func = 3
output = bitsize * func 

def set_slaveid(id):
    global slaveid
    slaveid = id

def set_func(function):
    global func
    func = function
    
def connect(port, bytesize, parity, stopbits, baudrate=9600):
    try:
        rs845 = serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, xonxoff=0)
        device = modbus_rtu.RtuMaster(rs845)
        device.set_timeout(5.0)
        device.set_verbose(True)
        return device
    except Exception as E:
        print("Fail to connect...." + str(E))
    
def toggle_register(device, channel):
    device.execute(slaveid, cst.WRITE_SINGLE_REGISTER, channel, output_value=output)
    
    
def reset_output(device):
    print(device.execute(slaveid, cst.WRITE_SINGLE_REGISTER, 0, output_value=256*8))
    
    
def disconnect_client(client):
    try:
        client.close()
        return
    except:
        pass