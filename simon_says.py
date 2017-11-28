from Tkinter import Tk, Label, Button
import time
import random

class SimonSaysGUI:
    # ------------------------------------------------------------------------------
    # Here we're creating the gui and the buttons and placing the buttons in the GUI
    def __init__(self, master):        
        random.seed()
        # the init function is a special function that runs when we
        # "instantiate," or create, the SimonSaysGUI object.  It's called
        # in line 135, below.
        self.turn_number = 1
        self.playing_round = False

        self.master = master
        master.title("Simon Says")

        self.label = Label(master, text="Let's Play Simon Says!")
        self.label.grid(row=0, column=0, columnspan=2)

        # Create and place Buttons in GUI        
        self.red_button = Button(master, text="Red", highlightbackground='white', command=self.red)
        self.red_button.grid(row=1, column=0)

        self.green_button = Button(master, text="Green", highlightbackground='white', command=self.green)
        self.green_button.grid(row=1, column=1)

        self.blue_button = Button(master, text="Blue", highlightbackground='white', command=self.blue)
        self.blue_button.grid(row=2, column=0)

        self.yellow_button = Button(master, text="Yellow", highlightbackground='white', command=self.yellow)
        self.yellow_button.grid(row=2, column=1)       

        self.play_button = Button(master, text="Play!", command=self.play)
        self.play_button.grid(row=3, column=0, columnspan=2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=0, columnspan=2)

    # ------------------------------------------------------------------------------
    # Here's we're telling the buttons what to do when they're pressed    

    # These functions are stored on the SimonSaysGUI object, and we can call them
    # using "self." plus the function name.  For example, "self.red()" will click
    # the red button and print "Red!" in the terminal output.
    def press_color_button(self, button_color):        
        if self.playing_round == True:
            if self.button_sequence and self.button_sequence[0] == button_color:
                print("Correct!")
                self.button_sequence.pop(0)
            else:
                print("Oops! The correct button was %s!" % self.button_sequence[0])
                print("You lose!")
                self.playing_round = False
                self.turn_number = 1
        else:
            print(button_color + "!")

    # Notice that we call press_color_button in four places below but only have 
    # to write out the ten lines of code for it once. This should give you a 
    # taste of the power of functions and reusable code.
    def red(self):
        self.press_color_button("red")

    def green(self):
        self.press_color_button("green")

    def blue(self):
        self.press_color_button("blue")

    def yellow(self):
        self.press_color_button("yellow")

    # ----------------------------------------------------------------------
    # These functions will allow the game to change the button color so you 
    # can see what colors to memorize.

    def reset_to_white(self, which_button):
        which_button.configure(highlightbackground='white')

    # This flash function is kind of complicated.  Basically, it takes the button you 
    # clicked, and makes its background change color, then go back to white after waiting 
    # 1000 milliseconds, or one second.
    def flash_button(self, which_button):        
        if which_button == "red":
            self.red_button.configure(highlightbackground="red")
            # This says "change color back to white after 1 second!"
            self.master.after(1000, self.reset_to_white, self.red_button)                               
        if which_button == "blue":
            self.blue_button.configure(highlightbackground="blue")
            self.master.after(1000, self.reset_to_white, self.blue_button)
        if which_button == "green":
            self.green_button.configure(highlightbackground="green")
            self.master.after(1000, self.reset_to_white, self.green_button)                        
        if which_button == "yellow":
            self.yellow_button.configure(highlightbackground="yellow")
            self.master.after(1000, self.reset_to_white, self.yellow_button)     

    # ------------------------------------------------------------------------------    
    # This is the game logic itself.

    def poll_user_input(self):                
        if len(self.button_sequence) > 0:
            self.master.after(100, self.poll_user_input) # runs every 100 milliseconds   
        else:
            print("You win!!")
            self.turn_number += 1        
 
    def play(self):
        self.playing_round = True
        print("Let's play! Remember the color patterns, then press them in order!")
        print("Ready... remember!")                
        self.button_sequence = []                

        # count through the buttons and pick a random one to store
        for num in range(self.turn_number):
            which_button = random.choice(["red", "yellow", "blue", "green"])  
            self.button_sequence.append(which_button)
            # What happens if you change the number of seconds below?!
            self.master.after((num * 1100), self.flash_button, which_button)
            

        print("Now it's your turn!  Press the buttons!")
        # define new function that checks what buttons we're clicking
        self.poll_user_input() # start polling 

# Don't worry too much about the "root" thing yet; this is just a way of 
# telling the Python code to keep running and wait for us to do things like 
# click buttons. 
root = Tk()

# now we're creating the GUI!  This code calls the __init__() function we 
# defined above
my_gui = SimonSaysGUI(root)

# Loops are a common tool for code that's waiting for you to act.  Basically,
# it checks all the buttons to see whether you've clicked them, over and over
# and over again *really fast*.  If you've clicked a button, it checks to see
# what function it should run, and runs that function.
root.mainloop()
