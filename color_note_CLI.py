import os

class Note:
    def __init__(self, title, content, priority, created_at):
        self.title = title
        self.content = content 
        self.priority = priority
        self.created_at = created_at

    def __str__(self):
        return f"title : {self.title}\ncontent : {self.content}\npriority :{self.priority}\ncreated at : {self.created_at}"

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'priority': self.priority,
            'created_at': self.created_at
        }

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file: 
                for line in file:
                    title, content, priority, created_at = line.strip().split('|')
                    note = Note(title, content, priority, created_at)
                    self.notes.append(note)

    def save_notes(self):
        with open(self.filename, 'w') as file:
            for note in self.notes:
                file.write(f"{note.title}|{note.content}|{note.priority}|{note.created_at}\n")

    def add_note(self, title, content, priority, created_at):
        note = Note(title, content, priority, created_at)
        self.notes.append(note)
        self.save_notes()

    def delete_note(self, title):
        self.notes = [note for note in self.notes if note.title != title]
        self.save_notes()

    def color_notes(self):
        for note in self.notes:
            if note.priority == "high":
                print(f"033[31m{note}033[0m")
            elif note.priority == "medium":
                print(f"033[33m{note}033[0m")
            elif note.priority == "low":
                print(f"033[32m{note}033[0m")

my_file = NoteManager('notes.txt')
print("===== colornote CLI =====")
print("1. Add new note")
print("2. View all notes")
print("3. Delete a note")
print("4. Exit")
print("===============")

while True:
    choice = int(input("Enter your choice: "))
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice, please try again.")
        continue

    match choice:
        case 1:
            title = input("Enter your title: ")
            content = input("Enter your content: ")
            priority = input("Choose your priority (high/medium/low): ")
            created_at = input("Enter your time: ")
            my_file.add_note(title, content, priority, created_at)
        case 2:
            my_file.color_notes()
        case 3:
            title = input("Enter your title: ")
            my_file.delete_note(title)       
        case 4:
            print("Exiting...")
            break
