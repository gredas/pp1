class Music():
    def __init__(self,artist,title,album,year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f'Performer: {self.artist}\nSong: {self.title}\nAlbum: {self.album}\nYear : {self.year}'    

song1 = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Music("Adele", "Hello", "25", 2015)
song3 = Music("Dua Lipa", "New Rules", "Dua Lipa", 2017)

print(song1)
print(song2)
print(song3)