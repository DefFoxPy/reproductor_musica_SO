import csv
import time
import sys
import random
from multiprocessing import Process


# Estructura de la canción
class Song:
    def __init__(self, title, artist, album, added_date, added_by, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.added_date = added_date
        self.added_by = added_by
        self.duration = duration


# Función para agregar una canción a la lista
def add_song(song, song_list):
    with open(song_list, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                song.title,
                song.artist,
                song.album,
                song.added_date,
                song.added_by,
                song.duration,
            ]
        )


# Función para mostrar el estado de la lista de canciones y las últimas dos ultimas
def display_song_list(song_list):
    while True:
        with open(song_list, "r") as file:
            reader = csv.reader(file)
            try:
                sonds = list(reader)
                last_sonds = sonds[-2:]
                print(f"\nEstado de la lista: {len(sonds)} canciones")
                for sond in last_sonds:
                    print(sond)
            except csv.Error as e:
                sys.exit("archivo {}, linea {}: {}".format(file, reader.line_num, e))
        time.sleep(5)


# Función para verificar si una canción ya está en la lista
def song_exists(song, song_list):
    with open(song_list, "r") as file:
        reader = csv.reader(file)
        try:
            for i in reader:
                if song.title == i[0] and song.artist == i[1] and song.album == i[2]:
                    return True
        except csv.Error as e:
            sys.exit("archivo {}, linea {}: {}".format(file, reader.line_num, e))
    return False


def user_process(song_list, username, new_songs):
    while True:
        new_song = random.choice(new_songs)
        new_song.added_by = username

        # Validar si la canción ya existe en la lista
        if not song_exists(new_song, song_list):
            add_song(new_song, song_list)
        else:
            print("La canción ya está en la lista.")

        time.sleep(5)


# Músicas de ejemplo
new_song1 = Song(
    "Brain Power",
    "NOMA",
    "Cytus II-Neko",
    time.strftime("%Y-%m-%d"),
    "Mint",
    "1:58",
)

new_song2 = Song(
    "MEGALOVANIA",
    "Toby Fox",
    "UNDERTALE Soundtrack",
    time.strftime("%Y-%m-%d"),
    "Soul",
    "2:36",
)

new_song3 = Song(
    "Brainiac Maniac",
    "Laura Shigihara",
    "Plans Vs. Zombies",
    time.strftime("%Y-%m-%d"),
    "Mint",
    "1:42",
)

new_song4 = Song(
    "El invisible",
    "Ricardo Arjona",
    "Blanco",
    time.strftime("%Y-%m-%d"),
    "Mint",
    "3:57",
)

if __name__ == "__main__":
    song_list_file = "song_list.csv"
    sounds_list = [new_song1, new_song2, new_song3, new_song4]

    p_display = Process(target=display_song_list, args=(song_list_file,))
    p_user1 = Process(
        target=user_process,
        args=(
            song_list_file,
            "Juan",
            sounds_list,
        ),
    )
    p_user2 = Process(
        target=user_process,
        args=(
            song_list_file,
            "Maria",
            sounds_list,
        ),
    )

    p_display.start()
    p_user1.start()
    p_user2.start()

    p_display.join()
    p_user1.join()
    p_user2.join()
