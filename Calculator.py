import tkinter as tk
class Calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.window.configure(background="#000000")

        self.dframe = self.createdframe()
        self.bframe = self.createbframe()

        self.total = ""
        self.current = ""

        self.totall, self.currentl = self.createtext()

        self.bframe.rowconfigure(0, weight = 1)
        for j in range(0,5):
            self.bframe.rowconfigure(j, weight = 1)
        for k in range(1,5):
            self.bframe.columnconfigure(k, weight = 1)

        self.digits = {
            7:(2,1), 8:(2,2), 9:(2,3),
            4:(3,1), 5:(3,2), 6:(3,3),
            1:(4,1), 2:(4,2), 3:(4,3),
            ".":(5,3), "(":(0,1), ")":(0,2)}

        self.operators = {"/":"\u00F7", "*":"\u00D7", "+":"+", "-":"-"}

        self.createdigit()
        self.createoperator()
        self.createclear()
        self.createequal()
        self.erase()
        self.delete()
        self.squarebutton()
        self.sqrtbutton()
        self.modbutton()
        self.square()
        self.createzero()
        self.sqrt()

    def createdframe(self):
        frame=tk.Frame(self.window, height = 221, bg="#000000")
        frame.pack(expand = True,fill = "both")
        return frame
    
    def createbframe(self):
        frame = tk.Frame(self.window, bg = "#000000")
        frame.pack(expand = True, fill = "both")
        return frame

    def addtoexpression(self, value):
        self.current += str(value)
        self.updatecurrentl()

    def createtext(self):
        total = tk.Label(self.dframe, text = self.total, anchor = tk.E, fg = "#D4D4D2", bg = "#1C1C1C", padx = 24, font = ("Helvetica", 20))
        total.pack(expand = True, fill = "both")

        current = tk.Label(self.dframe, text = self.current, anchor = tk.E, fg = "#D4D4D4", bg = "#1C1C1C", padx = 24, font = ("Helvetica", 50,))
        current.pack(expand = True, fill = "both")

        return total, current

    def createdigit(self):
        for digit, gridvalues in self.digits.items():
            button = tk.Button(self.bframe, text = str(digit), bg = "#505050", fg = "#D4D4D2", font = ("Arial", 24, "bold"), borderwidth=0, command = lambda x=digit: self.addtoexpression(x))
            button.grid(row = gridvalues[0], column = gridvalues[1], sticky = tk.NSEW)
    
    def createzero(self):
        button = tk.Button(self.bframe, text = "0", bg = "#505050", fg = "#D4D4D2", font = ("Helvetica", 24, "bold"), borderwidth = 0, command = lambda x=0: self.addtoexpression(x))
        button.grid(row = 5, column = 1, columnspan = 2, sticky = tk.NSEW)

    def appendop(self, op):
        self.current += op
        self.total+=self.current
        self.current = ""
        self.updatetotall()
        self.updatecurrentl()

    def createoperator(self):
        i = 1
        for operator, symbol in self.operators.items():
            button = tk.Button(self.bframe, text = symbol, bg = "#FF9500", fg = "#D4D4D2", font = ("Arial", 24), borderwidth = 0, command = lambda x=operator: self.appendop(x))
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i+=1

    def clear(self):
        self.current = ""
        self.total = ""
        self.updatetotall()
        self.updatecurrentl()

    def createclear(self):
        button = tk.Button(self.bframe, text = "C", bg = "#D4D4D2", fg = "#1C1C1C", font = ("Arial", 20), borderwidth = 0, command = self.clear)
        button.grid(row = 0, column = 3, sticky = tk.NSEW)

    def evaluate(self):
        self.total += self.current
        self.updatetotall()
        try:
            self.current = str(eval(self.total))
            self.total = ""
        except:
            self.current = "Error"
        finally:
            self.updatecurrentl()

    def delete(self):
        self.current = str(self.current[0:len(self.current)-1])
        self.updatecurrentl()

    def erase(self):
        button = tk.Button(self.bframe, text = "Del", bg = "#D4D4D2", fg = "#1C1C1C", font = ("Arial", 20), borderwidth = 0, command = self.delete)
        button.grid(row = 0, column = 4, sticky = tk.NSEW)

    def square(self):
        if len(self.current)==0:
            pass
        else:
            self.current = eval(self.current)**2
            self.updatecurrentl()

    def sqrt(self):
        if len(self.current)==0:
            pass
        else:
            self.current = str(int(eval(self.current)**0.5))
            self.updatecurrentl()        

    def squarebutton(self):
        button = tk.Button(self.bframe, text = "x\u00b2", bg = "#D4D4D2", fg = "#1C1C1C", font = ("Arial", 20), borderwidth = 0, command = self.square)
        button.grid(row = 1, column = 2, sticky = tk.NSEW)

    def sqrtbutton(self):
        button = tk.Button(self.bframe, text = "\u221ax", bg = "#D4D4D2", fg = "#1C1C1C", font = ("Arial", 20), borderwidth = 0, command = self.sqrt)
        button.grid(row = 1, column = 3, sticky = tk.NSEW)

    def modbutton(self):
        button = tk.Button(self.bframe, text = "%", bg = "#D4D4D2", fg = "#1C1C1C", font = ("Arial", 20), borderwidth = 0, command = lambda x= "%": self.appendop(x))
        button.grid(row = 1, column = 1, sticky = tk.NSEW)

    def createequal(self):
        button = tk.Button(self.bframe, text = "=", bg = "#FF9500", fg = "#D4D4D2", font = ("Arial", 20), borderwidth = 0, command = self.evaluate)
        button.grid(row = 5, column = 4, sticky = tk.NSEW)

    def updatetotall(self):
        exp = self.total
        for operator, symbol in self.operators.items():
            exp = exp.replace(operator, f' {symbol} ')
        self.totall.config(text = exp)

    def updatecurrentl(self):
        self.currentl.config(text = self.current[:7])

    def run(self):
        self.window.mainloop()
    
calc=Calc()
calc.run()
