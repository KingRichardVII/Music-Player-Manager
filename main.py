# Richard Phan
# COMP282 – Project 1: Music Playlist Manager
# Date: 10/3/25

# Description:
#   See README file

#Syllabus requirements
#   Ensured no more than 80 chars per line
#   Ensured indent size is 2 or 4 (no tab)
#______________________________________________________________________________

#NOTE - cursor == current node

#Class which represents a track in the playlist
#Creates our CDLL
class Node:
    #each node can only have these 5 attributes
    __slots__ = ("title", "artist", "duration", "prev", "next")
    #self.title/artist/duration stores user input
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration #duration = int
        self.prev = self
        self.next = self #completes a CDLL (.prev to head, .next to head)

#Class which makes an empty playlist
class Playlist:
    def __init__(self):
        self.head = None
        self.cursor = None #cursor = the current node or "song"
        self._size = 0 #length = 0

    def add_after_cursor(self, title, artist, duration):
        #creates a node
        new_node = Node(title, artist, duration)
        #if empty make one-node ring that becomes head and current node
        if self.head is None:
            self.head = new_node
            self.cursor = new_node
        else: #otherwise, stick new node b/w current node and whatever after
            #Update pointers to account for newly inserted node
            nxt = self.cursor.next
            self.cursor.next = new_node #left most node points to inserted node
            new_node.prev = self.cursor #inserted node back points to left node
            new_node.next = nxt #inserted node points to right node (old left)
            nxt.prev = new_node #left node is now right node, points to inserted
            if self.cursor == self.head.prev:  # if cursor at tail
                self.head.prev = new_node
            self.cursor = new_node #move cursor to new node or "song"

        self._size += 1 #increment by 1

    def remove_at_cursor(self):
        if self.head is None:
            print("EMPTY") #bc no node for us to remove
            return
        #if one song, remove to make playlist empty
        if self._size == 1:
            self.head = None
            self.cursor = None
            self._size = 0
            return

        prev_node = self.cursor.prev
        next_node = self.cursor.next

        #Delinks current node (middle) from previous and next nodes
        #connects P and N by rearranging pointers
        prev_node.next = next_node
        next_node.prev = prev_node

        #update head if removed node was head
        if self.cursor == self.head:
            self.head = next_node

        self.cursor = next_node
        self._size -= 1 # decrement to account for 1 removal of a song
    #Makes next node in list current node
    def move_next(self):
        if self.cursor is None:
            print("EMPTY")
            return
        self.cursor = self.cursor.next
    #Makes previous node in list current node
    def move_prev(self):
        if self.cursor is None:
            print("EMPTY")
            return
        self.cursor = self.cursor.prev
#Displays the current song (cursor)
#ex- bad guy | Billie_Eilish | 194(s)
    def print_current(self):
        if self.cursor is None:
            print("EMPTY")
        else:
            print(f"-> {self.cursor.title} | {self.cursor.artist} | {self.cursor
                  .duration}(s)")
#Displays ENTIRE playlist, not just current song
    #Essentially, this function traverses through the CDLL
    def print_playlist(self):
        if self.head is None:
            print("EMPTY")
            return

        node = self.head #start at head
        #loop to traverse CDLL _size times
        for _ in range(self._size):
            # displays '->' next to current song
            prefix = "-> " if node == self.cursor else ""
            print(f"{prefix}{node.title} | {node.artist} | {node.duration}(s)")
            node = node.next #goes to next node

    #How many songs in CDLL
    def length(self):
        print(self._size) #stores all increments and decrements from ADD/REMOVE
    #Reset list - clean slate
    def clear(self):
        self.head = None
        self.cursor = None
        self._size = 0

#Main method
def main():
    playlist = Playlist() #calls our class to initialize empty playlist

    while True: #loop forever until user breaks (type QUIT)
        try:
            cmd_line = input("Enter command (ADD/REMOVE/NEXT/PREV/CURRENT/PRINT"
                             "/LEN/CLEAR/QUIT): ").strip()
            if not cmd_line:
                continue
            # Cuts the input line in 2 pierces (command + argument [string])
            parts = cmd_line.split(maxsplit=1)
            cmd = parts[0].upper() #make case-insensitive

            if cmd == "ADD":
                # Handle quotes around title
                args = parts[1].strip()
                if args[0] == '"':
                    end_quote = args.find('"', 1)
                    title = args[1:end_quote]
                    rest = args[end_quote + 1:].strip().split()
                else:
                    # Handle no quotes around title
                    rest = args.split()
                    title = rest[0]
                    rest = rest[1:]
                artist = rest[0]
                duration = int(rest[1])
                #insert song into playlist
                playlist.add_after_cursor(title, artist, duration)

            #calls other functions
            elif cmd == "REMOVE":
                playlist.remove_at_cursor()

            elif cmd == "NEXT":
                playlist.move_next()

            elif cmd == "PREV":
                playlist.move_prev()

            elif cmd == "CURRENT":
                playlist.print_current()

            elif cmd == "PRINT":
                playlist.print_playlist()

            elif cmd == "LEN":
                playlist.length()

            elif cmd == "CLEAR":
                playlist.clear()

            elif cmd == "QUIT": #break loop and end program
                break

            else: #input validation
                print("Invalid command. Please try again.")
        #Basic exception handling
        except (EOFError, KeyboardInterrupt): #KeyboardInterrupt = ctrl + c
            break

#entry point guard
#Allows us to call main and start program
if __name__ == "__main__":
    main()
