from tkinter import *
from tkinter import ttk
from anagram_checker import AnagramChecker

root = Tk()
root.title("Anagram Finder")
frm = ttk.Frame(root, padding=10)
frm.pack(fill=BOTH, expand=True)
ttk.Label(frm, text="Anagram Finder").pack(pady=5)
input_text = StringVar() 
entry = ttk.Entry(frm, textvariable=input_text)
entry.pack(pady=5)
checker = AnagramChecker() 
infoLabel =  ttk.Label(frm)
def checkIfValid(word):
    infoLabel.pack_forget()
    if checker.is_valid_word(word):
        anagrams = checker.get_anagrams(word)
        if len(anagrams) > 0:
            infoLabel.config(text=f"YOUR WORD: '{word}'\n'{word}' is a valid English word\nAnagrams for {word} are: {", ".join([w.lower() for w in anagrams])}")
        else:
            infoLabel.config(text=f"YOUR WORD: '{word}'\n'{word}' is a valid English word\nThere are no anagrams for '{word}'")
        infoLabel.pack(pady=5)
    else: 
        infoLabel.config(text=f"'{word}' is not a valid word")
        infoLabel.pack(pady=5)
ttk.Button(frm, text="Get Anagrams", command=lambda: checkIfValid(entry.get())).pack(pady=5)
ttk.Button(frm, text="Quit", command=root.destroy).pack(pady=5)

root.mainloop()