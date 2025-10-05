# Music Player Manager
## *By Richard Phan*

### Description
This is a command-line Music Playlist Manager that stores tracks in a Circular 
Doubly Linked List. The app supports adding/removing tracks, moving to 
next/previous songs, and simple playback navigation with a cursor pointing at 
the “current song.”

### Node/Link Design & Invariants
- `head`: first node in CDLL
- `cursor`: current node
- `_size`: number of nodes
- Empty Playlist
  - `head is None`
  - `cursor is None`
  - `_size == 0`
### Commands
- `ADD "title" artist duration`: add new song after current song
- `REMOVE`: delete current song
- `NEXT`: next song becomes current
- `PREV`: previous song becomes current
- `CURRENT`: print selected song
- `PRINT`: print entire playlist
- `LEN`: print number of songs in playlist
- `CLEAR`:resets playlist to clean slate
- `QUIT`: Exit program

### Sample
Input:
```
ADD bad_guy Billie_Eilish 194
CURRENT
QUIT
```
Output:
```
-> bad_guy | Billie_Eilish | 194(s)
```