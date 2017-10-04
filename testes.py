from Tkinter import * 
from PIL import Image, ImageTk 



class janela:
    def __init__(self, parent):
        self.frame = Frame(root, width="500", height="500")
        self.frame.pack_propagate(0)
        self.frame.pack()

 
    
  

        self.bt = Button(self.frame, text="teste")
      
        self.bt.pack()

        self.icon = Image.open('open.png')
        self.imagem_ico = ImageTk.PhotoImage(self.icon)

        self.lb = Label(self.frame)
        self.lb["image"] = self.imagem_ico
        self.lb.pack()
     


 







if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")
    janela(root)
    root.mainloop()