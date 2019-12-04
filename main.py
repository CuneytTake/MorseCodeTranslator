from tkinter import *
import winsound
from winsound import SND_ASYNC
from time import sleep


class Application(Frame):

    def showresult(self):
        message = self.textbox.get("1.0", "end-1c")
        self.result = encrypt(message.upper())
        self.resultbox.delete("1.0", END)
        self.resultbox.insert(END, self.result)

        self.ditFrequency = self.ditFrequencyScale.get()
        self.ditDuration = self.ditDurationScale.get()

        self.dahFrequency = self.dahFrequencyScale.get()
        self.dahDuration = self.dahDurationScale.get()

        self.letterwait = self.letterwaitScale.get()
        self.wordwait = self.wordwaitScale.get()

        self.ditdahcount = self.result

        for letter in self.ditdahcount:

            if letter == ".":
                winsound.Beep(self.ditFrequency, self.ditDuration | SND_ASYNC)
                sleep(0.010)
            if letter == "-":
                winsound.Beep(self.dahFrequency, self.dahDuration | SND_ASYNC)
                sleep(0.010)
            if letter == " ":
                sleep(self.letterwait / 1000)
            if letter == "  ":
                print(self.wordwait)
                sleep(self.wordwait / 1000)
                print(self.wordwait / 1000)

        print(len(self.result))

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # 'Message' text label
        Label(self,
              text="  Message:"
              ).grid(row=0, column=0)

        # Entry textbox
        self.textbox = Text(self, height=5, width=80)
        self.textbox.grid(row=0, column=1, padx=10, pady=10)

        # Morse result textbox
        self.resultbox = Text(self, height=5, width=46, wrap=CHAR, font="Calibri 20 bold")
        self.resultbox.grid(row=1, column=1, padx=10, pady=10)

        # 'Morse' text label
        Label(self, text="Morse:"
              ).grid(row=1, column=0)

        # ' Translate ' button
        self.buttonCommit = Button(self, height=1, width=10, text="Translate",
                                   command=self.showresult)
        self.buttonCommit.grid(row=4, column=1)

        # Dot/Dit frequency and duration var
        Label(self, text="DIHZ").grid(row=5, column=0)
        self.ditFrequencyScale = Scale(self, from_=40, to=1200, orient=HORIZONTAL, length=750)
        self.ditFrequencyScale.set(500)
        self.ditFrequencyScale.grid(row=5, column=1, sticky=W)

        Label(self, text="DIDR").grid(row=6, column=0)
        self.ditDurationScale = Scale(self, from_=100, to=1000, orient=HORIZONTAL, length=750)
        self.ditDurationScale.set(220)
        self.ditDurationScale.grid(row=6, column=1, sticky=W)

        # Stripe/Dah frequency and duration var
        Label(self, text="DAHZ").grid(row=7, column=0)
        self.dahFrequencyScale = Scale(self, from_=40, to=1200, orient=HORIZONTAL, length=750)
        self.dahFrequencyScale.set(500)
        self.dahFrequencyScale.grid(row=7, column=1, sticky=W)

        Label(self, text="DADR").grid(row=8, column=0)
        self.dahDurationScale = Scale(self, from_=100, to=3000, orient=HORIZONTAL, length=750)
        self.dahDurationScale.set(660)
        self.dahDurationScale.grid(row=8, column=1, sticky=W)

        # Wait time var
        Label(self, text="LWAIT").grid(row=9, column=0)
        self.letterwaitScale = Scale(self, from_=10, to=3000, orient=HORIZONTAL, length=750)
        self.letterwaitScale.set(660)
        self.letterwaitScale.grid(row=9, column=1)

        Label(self, text="WWAIT").grid(row=10, column=0)
        self.wordwaitScale = Scale(self, from_=10, to=3000, orient=HORIZONTAL, length=750)
        self.wordwaitScale.set(1540)
        self.wordwaitScale.grid(row=10, column=1)


# Alphabet to morse dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters

            cipher += MORSE_CODE_DICT[letter] + ' '
        else:

            # 1 space indicates different characters
            # and 2 indicates different words

            cipher += ' '

    return cipher


root = Tk()
root.title("MorseMind")
app = Application(root)
root.geometry("900x600")
root.resizable(FALSE, FALSE)
root.mainloop()
