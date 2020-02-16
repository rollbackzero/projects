class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "happy birthday to you",
                   "happy birthday, happy birthday",
                   "happy birthday to you"])


# Get user input then put that into a list
awit = [input("> ")]

# Pass the variable to class
#awit = ["Bahay kubo kahit munti",
#        "Ang halaman duon",
#        "Ay sari sari"]

happy_bday.sing_me_a_song()

# Call the function and pass awit variable then assign to separate variable  
kanta = Song(awit)
kanta.sing_me_a_song()
