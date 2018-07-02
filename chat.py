#imports
from socket import *
import tkinter
import _thread

# sending messages
def sending():
    message = bytes(myMessage01.get(), 'UTF-8')
    myMessage01.set("")
    clientSocket.sendto(message, addr)
    label = tkinter.Label(frame3,text = message)
    label.pack(anchor=tkinter.SE)

# receiving messages
def receiving(clientSocket):
    while True:
        data, server = clientSocket.recvfrom(1024)
        label = tkinter.Label(frame3,text = data)
        label.pack(anchor=tkinter.SW)

# main
def main():
    global addr
    global clientSocket
    try:
        port = int (port01.get())
        myPort = int(myPort01.get())
    except:
        print("Invalid port.")
        exit(1)
    ipAddress = ipAddress01.get()
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.bind(("",myPort))
    addr = (ipAddress, port)
    _thread.start_new_thread ( receiving, (clientSocket,))


#GUI
# scrollable frame help from:
# http://stackoverflow.com/questions/16188420/python-tkinter-scrollbar-for-frame

#Scrollable frame
def configure_frame(event):
    # update the scrollbars to match the size of the inner frame
    size = (frame3.winfo_reqwidth(), frame3.winfo_reqheight())
    canvas.config(scrollregion="0 0 %s %s" % size)
    if frame3.winfo_reqwidth() != canvas.winfo_width():
        # update the canvas's width to fit the inner frame
        canvas.config(width=frame3.winfo_reqwidth())
#Help from above mentioned link fro scrollable frame
def configure_canvas(event):
    if frame3.winfo_reqwidth() != canvas.winfo_width():
        # update the inner frame's width to fill the canvas
        canvas.itemconfigure(canvas_id, width=canvas.winfo_width())


#creating interface
#window
window = tkinter.Tk()
window.minsize(width=200, height=600)
#creating a frame
frame = tkinter.Frame(window, borderwidth=5, relief=tkinter.RAISED)
#adding this frame to the north-west side of the window
frame.pack(anchor=tkinter.NW)
#labels and entry fields for address information
label1 = tkinter.Label(frame, text="My port: ")
label1.pack(side = tkinter.LEFT)
myPort01 = tkinter.StringVar()
myPort02 = tkinter.Entry(frame, textvariable=myPort01)
myPort02.pack(side = tkinter.LEFT)
label2 = tkinter.Label(frame, text="IP Address:")
label2.pack(side = tkinter.LEFT)
ipAddress01 = tkinter.StringVar()
ipAddress02 = tkinter.Entry(frame,textvariable=ipAddress01)
ipAddress02.pack(side = tkinter.LEFT)
label3 = tkinter.Label(frame, text="Friend's port: ")
label3.pack(side = tkinter.LEFT)
port01 = tkinter.StringVar()
port02 = tkinter.Entry(frame,textvariable=port01)
port02.pack(side = tkinter.LEFT)

#button to submit the entry in above fields and read main function for it
save01 = tkinter.Button(frame, text='Submit', command=main)
save01.pack(side = tkinter.BOTTOM)

#frame for message sending at the bottom of the window expanding along x-axis
frame2 = tkinter.Frame(window, borderwidth=5, relief=tkinter.RAISED)
frame2.pack(side=tkinter.BOTTOM,anchor = tkinter.SE,fill=tkinter.X)
label4 = tkinter.Label(frame2, text="Your Message ")
label4.pack(side = tkinter.TOP)
myMessage01 = tkinter.StringVar() #The message typed will be string type
myMessage02 = tkinter.Entry(frame2,textvariable=myMessage01)
myMessage02.pack(side=tkinter.RIGHT,expand = tkinter.TRUE)
#button that calls the sending function and sends the message
save02 = tkinter.Button(frame2, text='Send', command=sending)
save02.pack(side = tkinter.BOTTOM)

#Help from above mentioned link for scrollbar
scrollbar = tkinter.Scrollbar(window)
scrollbar.pack(side=tkinter.RIGHT, fill='y')
canvas = tkinter.Canvas(window, yscrollcommand = scrollbar.set)
canvas.pack(side=tkinter.BOTTOM,expand=tkinter.TRUE,fill=tkinter.BOTH)
#canvas.configure(yscrollcommand = scrollbar.set)
scrollbar.config(command=canvas.yview)
canvas.bind('<Configure>', configure_canvas)

#frame inside canvas for the display of the chat(both sent and received)
frame3 = tkinter.Frame(canvas, borderwidth=5)
frame3.pack(expand=tkinter.TRUE,fill=tkinter.BOTH) #packing it in the main body of the window
frame3.bind('<Configure>', configure_frame)
canvas_id = canvas.create_window(0, 0, window=frame3, anchor=tkinter.NW) #made a window inside canvas in which frame is inserted

window.mainloop()









