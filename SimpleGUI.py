import os
import platform
import sys

import tkinter as tk
from logging import Logger
import ModbusRTUMaster as MB


os_type = platform.system()

# Todo : add port list
# devices = []
# if os_type == "windows":
#     # Todo : Manual workaround, to add solution later 
#     devices = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]
# elif os_type == "linux":
#     pass
# else:
#     print("OS Not Supported")

#* Window GUI class
class WindowGUI:
    def __init__(self, title):
        self.master = tk.Tk()
        self.master.title(title)
        self.settings_frame = tk.Frame(self.master, borderwidth=5)
        self.control_frame = tk.Frame(self.master, borderwidth=5)
        # ToDo : add icons, path varies with OS
        # if platform.system() == "windows":
        #     self.master.iconbitmap()
        
        #* Initialize Modbus Client
        self.client = None
        
        #* Serial settings
        self.serial_port = None
        self.serial_parity = None
        self.serial_stopbits = None
        self.serial_baudrate = None
        self.serial_bytesize = None
        
        #* Selection for functions, data and address for Modbus command
        self.mb_slaveid = tk.StringVar() 
        self.mb_function = tk.StringVar()
        self.mb_address = tk.IntVar()
        self.mb_mode = tk.IntVar() 
        self.mb_mode_byte = tk.IntVar()
        
        #* Radio button option for 
        #* Drop down option for serial
        # ToDo : lsdev for linux & MAC, windows ??? 

        # ToDo : Create Serial object 
        self.button_connect = tk.Button(self.settings_frame, text="Connect", command=self.serial_popup, bg="white", width=20, height=5)
        self.button_disconnect = tk.Button(self.settings_frame, text="Disconnect", bg="white", width=20, height=5)
        
        #* Toggle button
        self.button_chan01 = tk.Button(self.control_frame, text="Channel 1", width=15, height=5, command=self.press_btn1, activebackground="green")
        self.button_chan02 = tk.Button(self.control_frame, text="Channel 2", width=15, height=5, command=self.press_btn2, activebackground="green")
        self.button_chan03 = tk.Button(self.control_frame, text="Channel 3", width=15, height=5, command=self.press_btn3, activebackground="green")
        self.button_chan04 = tk.Button(self.control_frame, text="Channel 4", width=15, height=5, command=self.press_btn4, activebackground="green")
        self.button_chan05 = tk.Button(self.control_frame, text="Channel 5", width=15, height=5, command=self.press_btn5, activebackground="green")
        self.button_chan06 = tk.Button(self.control_frame, text="Channel 6", width=15, height=5, command=self.press_btn6, activebackground="green")
        self.button_chan07 = tk.Button(self.control_frame, text="Channel 7", width=15, height=5, command=self.press_btn7, activebackground="green")
        self.button_chan08 = tk.Button(self.control_frame, text="Channel 8", width=15, height=5, command=self.press_btn8, activebackground="green")
        self.button_chan09 = tk.Button(self.control_frame, text="Channel 9", width=15, height=5, command=self.press_btn9, activebackground="green")
        self.button_chan10 = tk.Button(self.control_frame, text="Channel 10", width=15, height=5, command=self.press_btn10, activebackground="green")
        self.button_chan11 = tk.Button(self.control_frame, text="Channel 11", width=15, height=5, command=self.press_btn11, activebackground="green")
        self.button_chan12 = tk.Button(self.control_frame, text="Channel 12", width=15, height=5, command=self.press_btn12, activebackground="green")
        self.button_chan13 = tk.Button(self.control_frame, text="Channel 13", width=15, height=5, command=self.press_btn13, activebackground="green")
        self.button_chan14 = tk.Button(self.control_frame, text="Channel 14", width=15, height=5, command=self.press_btn14, activebackground="green")
        self.button_chan15 = tk.Button(self.control_frame, text="Channel 15", width=15, height=5, command=self.press_btn15, activebackground="green")
        self.button_chan16 = tk.Button(self.control_frame, text="Channel 16", width=15, height=5, command=self.press_btn16, activebackground="green")
        
        self.initialize()
        self.master.mainloop()
        
        
        
    def disconnect_button(self):
        if self.client == None:
            return
        MB.disconnect_client(self.client)
            
        
    #* Pop up window when clicking connect
    def serial_popup(self, title="Serial Settings"):
        self.pop_window = tk.Toplevel(self.master)
        self.pop_window.wm_title(title)
        self.pop_window.config(borderwidth=10)
        
        self.pw_port = tk.StringVar()
        self.pw_baudrate = tk.StringVar()
        self.pw_stopbits = tk.StringVar()
        self.pw_parity = tk.StringVar()
        self.pw_bytesize = tk.StringVar()
        
        #* Inputs label and entry
        pw_port_label = tk.Label(self.pop_window, text="Port")
        # Todo : drop down with list from lsdev
        pw_port_sel = tk.Entry(self.pop_window, textvariable=self.pw_port, width=15, justify="center")
        
        baudrate_list = ["4800", "9600", "19200", "38400", "57600", "115200"]
        self.pw_baudrate.set(baudrate_list[1])
        pw_baudrate_label = tk.Label(self.pop_window, text="Baudrate")
        pw_baudrate_sel = tk.OptionMenu(self.pop_window, self.pw_baudrate, *baudrate_list)
        
        pw_stopbits_label = tk.Label(self.pop_window, text="Stop Bits")
        pw_stopbits_sel = tk.Entry(self.pop_window, textvariable=self.pw_stopbits, width=15, justify="center")
        
        parity_list = ["[N]one", "[E]ven", "[O]dd"]
        self.pw_parity.set(parity_list[0])      
        pw_parity_label = tk.Label(self.pop_window, text="Parity")
        pw_parity_sel = tk.OptionMenu(self.pop_window, self.pw_parity, *parity_list)

        bytesize_list = ['5','6','7','8']
        self.pw_bytesize.set(bytesize_list[-1])
        pw_bytesize_label = tk.Label(self.pop_window, text="Bytesize")
        pw_bytesize_sel = tk.OptionMenu(self.pop_window, self.pw_bytesize, *bytesize_list)
        
        #* Apply and Cancel button
        pw_button_ok = tk.Button(self.pop_window, text="Connect", command=self.parse_serial_settings)
        pw_button_cancel = tk.Button(self.pop_window, text="Cancel", command=self.pop_window.destroy)
        
        
        #* Initialize
        pw_port_label.grid(column=0,row=1)
        pw_port_sel.grid(column=1,row=1, padx=(5,0), pady=5, columnspan=2, sticky=tk.W )
        pw_baudrate_label.grid(column=0,row=2)
        pw_baudrate_sel.grid(column=1,row=2, padx=(5,0), pady=5, columnspan=2, sticky=tk.W )
        pw_stopbits_label.grid(column=0,row=3)
        pw_stopbits_sel.grid(column=1,row=3, padx=(5,0), pady=5, columnspan=2, sticky=tk.W )
        pw_bytesize_label.grid(column=0,row=4)
        pw_bytesize_sel.grid(column=1,row=4, padx=(5,0), pady=5, columnspan=2, sticky=tk.W )
        pw_parity_label.grid(column=0,row=5)
        pw_parity_sel.grid(column=1,row=5, padx=(5,0), pady=5, columnspan=2, sticky=tk.W )
        
        pw_button_ok.grid(column=2, row=6, sticky=tk.E ,pady=(20,0))
        pw_button_cancel.grid(column=3, row=6, sticky=tk.E , pady=(20,0))
       
        
        
        
    #* Parse arguments 
    def parse_serial_settings(self):
        # Todo : parse arguments to 1. MB object 2. self. settings
        self.serial_port = self.pw_port.get()
        self.serial_baudrate = self.pw_baudrate.get()
        self.serial_bytesize = self.pw_bytesize.get()
        self.serial_stopbits = self.pw_stopbits.get()
        self.serial_parity = self.pw_parity.get()[1]
        self.client = MB.connect(self.serial_port, int(self.serial_bytesize), self.serial_parity, int(self.serial_stopbits), int(self.serial_baudrate))
        self.pop_window.destroy()

    #* ===== Event handler =====
    def press_btn1(self):
        self.toggle_output(1)
        
    def press_btn2(self):
        self.toggle_output(2)
        
    def press_btn3(self):
        self.toggle_output(3)

    def press_btn4(self):
        self.toggle_output(4)
        
    def press_btn5(self):
        self.toggle_output(5)
        
    def press_btn6(self):
        self.toggle_output(6)
        
    def press_btn7(self):
        self.toggle_output(7)
        
    def press_btn8(self):
        self.toggle_output(8)
        
    def press_btn9(self):
        self.toggle_output(9)

    def press_btn10(self):
        self.toggle_output(10)
        
    def press_btn11(self):
        self.toggle_output(11)
        
    def press_btn12(self):
        self.toggle_output(12)
        
    def press_btn13(self):
        self.toggle_output(13)
        
    def press_btn14(self):
        self.toggle_output(14)

    def press_btn15(self):
        self.toggle_output(15)       
         
    def press_btn16(self):
        self.toggle_output(16)
        
    
    # todo : set up device settings 
    def toggle_output(self, channel):
        if self.client == None:
            Logger.info("No device connected...")
            return
        toggle_output = MB.toggle_register(self.client, channel)
        return
        
        
        
        
    #* Initialize geometry manager 
    def initialize(self):
        #* Create a grid layout manager
        self.master.grid()
        self.settings_frame.grid(column=0, row=0, columnspan=2)
        self.control_frame.grid(column=0, row=1)
        
        self.button_connect.grid(column=0, row=1, padx=(0, 15))
        self.button_disconnect.grid(column=1, row=1)
        
        self.button_chan01.grid(column=0, row=2)
        self.button_chan02.grid(column=1, row=2)
        self.button_chan03.grid(column=2, row=2)
        self.button_chan04.grid(column=3, row=2)
        self.button_chan05.grid(column=4, row=2)
        self.button_chan06.grid(column=5, row=2)
        self.button_chan07.grid(column=6, row=2)
        self.button_chan08.grid(column=7, row=2)
        self.button_chan09.grid(column=0, row=3)
        self.button_chan10.grid(column=1, row=3)
        self.button_chan11.grid(column=2, row=3)
        self.button_chan12.grid(column=3, row=3)
        self.button_chan13.grid(column=4, row=3)
        self.button_chan14.grid(column=5, row=3)
        self.button_chan15.grid(column=6, row=3)
        self.button_chan16.grid(column=7, row=3)
    
    
    
        
    
    
    
        
# ToDo : call from MB 
class SerialSettingsWindow:
    def __init__(self) -> None:
        pass
    
    def press_connect(self):
        # ToDo : parse inserted value
        pass    
    
myapp = WindowGUI("test")
