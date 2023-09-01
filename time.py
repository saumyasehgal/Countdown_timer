//From Codewithstuti
### Let the user know if the timer has expired
        if(clockTime == 0):
            messagebox.showinfo("", "Your time has expired!")

        clockTime -= 1


setTimeButton = Button(clockWindow, text='Set Time', bd='5', command=runTimer)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)
### Keep looping
clockWindow.mainloop()
