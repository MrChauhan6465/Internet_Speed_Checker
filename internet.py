import tkinter  
import speedtest as spd

def speed_checker():
    sp = spd.Speedtest()
    sp.get_servers()
    download_s = str(round(sp.download()/(10**6),3))+" Mbps "
    upload_s = str(round(sp.upload()/(10**6),3))+" Mbps "
    label_down .config(text=download_s)
    label_upload.config(text = upload_s)

st = tkinter.Tk()

st.title(" Internet Speed Test")
st.geometry("500x700")
st.config(bg="Yellow")

lb = tkinter.Label(st,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="Yellow",fg="Red")
lb.place(x=60,y=40,height=50,width=380)

lb = tkinter.Label(st,text="Download Speed",font=("Time New Roman",30,"bold"),bg="light yellow",fg="red")
lb.place(x=60,y=130,height=50,width=380)

label_down = tkinter.Label(st,text="00",font=("Time New Roman",30,"bold"),bg="light yellow",fg="red")
label_down.place(x=60,y=200,height=50,width=380)

lb = tkinter.Label(st,text="Upload Speed",font=("Time New Roman",30,"bold"),bg="light yellow",fg="red")
lb.place(x=60,y=290,height=50,width=380)

label_upload = tkinter.Label(st,text="00",font=("Time New Roman",30,"bold"),bg="light yellow",fg="red")
label_upload.place(x=60,y=360,height=50,width=380)

button = tkinter.Button(st,text="Check Speed",font=("Time New Roman",30,"bold"),relief=tkinter.RAISED,bg="light yellow",fg="red",command=speed_checker)
button.place(x=60,y=460,height=50,width=380)

st.mainloop()