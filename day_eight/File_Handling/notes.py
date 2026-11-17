#2. Notes Reader Program

#open the file in read mode

file=open("notes.txt","r")


#read and display all notes

notes = file.read()
print(notes)


#colse the file

file.close()
