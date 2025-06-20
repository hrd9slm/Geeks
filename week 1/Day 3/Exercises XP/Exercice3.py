class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics  # on stocke la liste des paroles

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
if __name__ == "__main__":   
    stairway = Song(["There s a lady who's sure", "all that glitters is gold", "and she s buying a stairway to heaven"])
    stairway.sing_me_a_song()

