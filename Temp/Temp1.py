import NoteUtilities

def runNotes():
    print("Welcome to KiedesNote - For All YOur Temporary Note Needs.")
    print("Please don't confuse us with other (lesser known) products like Evernote....")
    print("The best temporary notes system on the market - just ask us.")
    print("In order to get started, select from one of the options below:")
    print("1. Add a note.")
    print("2. Display all notes.")
    print("3. Display a random note.")
    print("4. Add and display all notes.")
    print("5. Display a random note.")
    print("6. Delete a note.")
    print("7. Quit program.")
    makeSelection()

def makeSelection():
    run = True
    while(run):
        choice = int(input("What would you like to do?"))
        match choice:
            case 1: NoteUtilities.addNote()
            case 2: NoteUtilities.displayNotes()
            case 3: NoteUtilities.displayRandomNote()
            case 4: NoteUtilities.addAndDisplay()
            case 5: NoteUtilities.displayRandomNote()
            case 6:
                note = int(input("What note would you like to delete?"))
                NoteUtilities.deleteNote(note)
            case 7: run = False
            case _: print("Sorry I couldn't understand that.  Please try again")

import random as rand

noteList = ["test1", "test2", "test3", "test4"]
lastNote = 4

def addNote():
    global lastNote, noteList
    newNote = input("What would you like to add to the note?")
    noteList.append(newNote)
    lastNote += 1

def displayNotes():
    global noteList
    for note in range(0, lastNote):
        print(str(note + 1) + ". " + noteList[note] + "\n")

def displayRandomNote():
    global noteList, lastNote
    randNote = rand.randint(0, lastNote)

    print(noteList[randNote] + "\n")

def addAndDisplay():
    addNote()
    displayNotes()

def removeLastNote():
    global noteList, lastNote
    noteList[lastNote-1] = ""
    lastNote -= 1

def deleteNote(numNote):
    global noteList, lastNote

    if numNote < 0 or numNote > lastNote:
        print("Sorry, but you made an invalid selection.")
        print("Please try again.")

    elif numNote == lastNote:
        removeLastNote()
    else:
        for index in range(numNote-1, lastNote-1):
            noteList[index] = noteList[index + 1]
        removeLastNote()
        print("Note deleted.")



runNotes()