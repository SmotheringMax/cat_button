import tkinter as tk
import random
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("cat2.wav")

done = False

while not done:
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            cat_image = tk.PhotoImage(file="cat.gif")
            self.hi_there = tk.Button(self, image=cat_image)

            self.hi_there["text"] = "Number generator\n(click me)"
            self.hi_there["command"] = self.say_hi

            self.hi_there.config(image=cat_image)
            self.hi_there.pack(side="left")
            self.hi_there = cat_image



            self.hi_tot = tk.Button(self)
            self.hi_tot["text"] = "Ololo\n(vurka)"
            self.hi_tot.pack(side="right")

            self.hi_rr = tk.Button(self)
            self.hi_rr["text"] = "Mamky\n(kopal)"
            self.hi_rr.pack(side="right")

            self.quit = tk.Button(self, text="QUIT", fg="red",
                                  command=root.destroy)
            self.quit.pack(side="bottom")

        def say_hi(self):
            a = random.randrange(80630000000, 80639999999)
            sound.play()
            print("Is it your number?:", a)
            if a == 80633900968:
                print("WOW!")
            else:
                print("Wrong")



    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
    quit()
