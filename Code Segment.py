from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image, ImageDraw, ImageGrab

root=Tk()
root.title("Paint")
root.geometry("1000x1000")

brushColor = 'black'

def paint(e):
    # Brush Parameters
    brushSize = int(mySlider.get())
    brushType2 = brushType.get()

    x1 = e.x -1           # Starting Point
    y1 = e.y -1
    x2 = e.x + 1          # Ending Point
    y2 = e.y + 1

    myCanvas.create_line(x1, y1, x2, y2, fill=brushColor, width=brushSize, capstyle=brushType2, smooth=True)

def changeBrushSize(e):       # Change brush Size
    sliderLabel.config(text=int(mySlider.get()))

def changeBrushColor():     # Change Brush Color
    global brushColor
    brushColor = 'black'
    brushColor= colorchooser.askcolor(color=brushColor)[1]

def changeCanvasColor():      # Change Canvas Color
    global bgColor
    bgColor = 'black'
    bgColor= colorchooser.askcolor(color=bgColor)[1]
    myCanvas.config(bg=bgColor)

def clearScreen():          # Change Canvas Color
    myCanvas.delete(ALL)
    myCanvas.config(bg='white')

def piSym():                  #Defining Pi
    myCanvas.create_text(200,200,text="π")
    myCanvas.pack()

def sigmaSym():             #Defining Sigma
    myCanvas.create_text(70,80,text='ξ')
    myCanvas.pack()

def tauSym():             #Defining Tau
    myCanvas.create_text(600,580,text='τ')
    myCanvas.pack()

def saveImage():            #Save Image
    result = filedialog.asksaveasfilename(initialdir="/Users/mac/Desktop/foldersvskla/Pelumi's Class/GUI", filetypes=(('JPEG files', '*.jpeg'), ('All Files', '*.*')))
    
    if result.endswith('.jpeg'):
        pass
    if result:
        x=root.winfo_rootx() + myCanvas.winfo_rootx()
        y=root.winfo_rooty() + myCanvas.winfo_rooty()
        x1=x+myCanvas.winfo_width()
        y1=y+myCanvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result,format="jpeg",dpi=(300,300))


w = 1000            #Create Canvas
h = 400
myCanvas = Canvas(root, width=w, height=h, bg='white')
myCanvas.pack(pady=20)


myCanvas.bind('<B1-Motion>', paint)

brushFrame = Frame(root)        # Create brush option frame
brushFrame.pack(pady=20)

brushSizeFrame = LabelFrame(brushFrame, text='Brush Size')      # Brush Size
brushSizeFrame.grid(row=0, column=0, padx=50)

mySlider = ttk.Scale(brushSizeFrame, from_=1, to=50, command=changeBrushSize, orient=VERTICAL, value=10)  # Brush Size
mySlider.pack(pady=10, padx=10)

sliderLabel = Label(brushSizeFrame, text=mySlider.get())    # Brush Size
sliderLabel.pack(pady=5)

brushTypeFrame = LabelFrame(brushFrame, text='Brush Type', height=400)  # Brush Size
brushTypeFrame.grid(row=0, column=1, padx=50)

brushType = StringVar()
brushType.set('round')

# Create Radio Button for Brush type
brushTypeRadio1 = Radiobutton(brushTypeFrame, text='Round', variable=brushType, value='round')
brushTypeRadio1.pack(anchor=W)
brushTypeRadio2 = Radiobutton(brushTypeFrame, text='Slash', variable=brushType, value='butt')
brushTypeRadio2.pack(anchor=W)
brushTypeRadio3 = Radiobutton(brushTypeFrame, text='Diamond', variable=brushType, value='projecting')
brushTypeRadio3.pack(anchor=W)

changeColorsFrame = LabelFrame(brushFrame, text='Change Color')     # Change Color
changeColorsFrame.grid(row=0, column=3)

brushColorButton = Button(changeColorsFrame, text='Brush Color', command=changeBrushColor)  # Change brush color button
brushColorButton.pack(pady=10, padx=10)

canvasColorButton = Button(changeColorsFrame, text='Canvas Color', command=changeCanvasColor)   # Change Canvas color button
canvasColorButton.pack(pady=10, padx=10)

optionFrame1 = LabelFrame(brushFrame, text='Symbols')     # Symbols
optionFrame1.grid(row=0, column=4, padx=50)

optionFrame2 = LabelFrame(brushFrame, text='Program Option')     # Program Options Frame
optionFrame2.grid(row=0, column=5, padx=50)

symbolbutton = Button(optionFrame1, text='Pi', command=piSym)    #Pi Symbol
symbolbutton.pack(pady=10, padx=10)

symbolbutton = Button(optionFrame1, text='Sigma' , command=sigmaSym)     #Sigma Symbol
symbolbutton.pack(pady=10, padx=10)

symbolbutton = Button(optionFrame1, text='Tau' , command=tauSym)     # Tau Symbol
symbolbutton.pack(pady=10, padx=10)

clearButton = Button(optionFrame2, text='Clear Screen', command=clearScreen)     # Clear Screen Button
clearButton.pack(pady=10, padx=10)

saveImageButton = Button(optionFrame2, text='Save as JPEG', command=saveImage)   # Save Image
saveImageButton.pack(pady=10, padx=10)


root.mainloop()
