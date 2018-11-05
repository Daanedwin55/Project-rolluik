import serial
import tkinter

var = serial.Serial('COM3', 19200)

def led_on():
    var.write('1'.encode("ascii"))
    s =var.read()
    print(s)
   
def led_off():
    var.write('0'.encode("ascii"))
    s =var.read()
    print(s)

led_control_windows= tkinter.Tk()


button = tkinter.Button 


knopaan = button(led_control_windows, text="aan", command=led_on)
knopuit = button(led_control_windows, text="uit", command=led_off)


knopaan.grid(row=0, column=1)
knopuit.grid(row=1, column=1)

led_control_windows.mainloop()

input("Press enter to exit")





