import csv
import time
import sys
from multiprocessing import Process

TIME_DISPLAY = 7  # Cada cuanto se mostrará las canciones por pantalla


# Estructura de la canción
class Song:
    def __init__(self, title, artist, album, added_date, added_by, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.added_date = added_date
        self.added_by = added_by
        self.duration = duration


# Función para mostrar el estado de la lista de canciones y las últimas dos ultimas
def display_song_list(song_list_file):
    while True:
        with open(song_list_file, "r") as file:
            reader = csv.reader(file)
            try:
                sonds = list(reader)
                last_sonds = sonds[-2:]
                print(f"\nEstado de la lista: {len(sonds)} canciones")
                for sond in last_sonds:
                    print(sond)
            except csv.Error as e:
                sys.exit("archivo {}, linea {}: {}".format(file, reader.line_num, e))
        time.sleep(TIME_DISPLAY)


# Músicas de ejemplo
new_song1 = Song(
    "Brain Power",
    "NOMA",
    "Cytus II-Neko",
    time.strftime("%Y-%m-%d"),
    "x",
    "1:58",
)

new_song2 = Song(
    "MEGALOVANIA",
    "Toby Fox",
    "UNDERTALE Soundtrack",
    time.strftime("%Y-%m-%d"),
    "x",
    "2:36",
)

new_song3 = Song(
    "Brainiac Maniac",
    "Laura Shigihara",
    "Plans Vs. Zombies",
    time.strftime("%Y-%m-%d"),
    "x",
    "1:42",
)

new_song4 = Song(
    "El invisible",
    "Ricardo Arjona",
    "Blanco",
    time.strftime("%Y-%m-%d"),
    "x",
    "3:57",
)

new_song5 = Song(
    "Bury the Light",
    "Victor Borda",
    "Bury the Light",
    time.strftime("%Y-%m-%d"),
    "x",
    "9:42",
)

new_song6 = Song(
    "Devil Trigger",
    "Casey Edwards",
    "Devil May Cry 5",
    time.strftime("%Y-%m-%d"),
    "x",
    "2:36",
)

new_song7 = Song(
    "El Problema",
    "Ricardo Arjona",
    "Santo Pecado",
    time.strftime("%Y-%m-%d"),
    "x",
    "5:30",
)

new_song8 = Song(
    "Rise",
    "Justi Tranter",
    "Rise",
    time.strftime("%Y-%m-%d"),
    "x",
    "3:12",
)

if __name__ == "__main__":
    song_list_file = "song_list.csv"
    sounds_list = [
        new_song1,
        new_song2,
        new_song3,
        new_song4,
        new_song5,
        new_song6,
        new_song7,
        new_song8,
    ]

    p_display = Process(target=display_song_list, args=(song_list_file,))

    p_display.start()

    p_display.join()
