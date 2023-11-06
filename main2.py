import csv
import time
import sys
import random
from multiprocessing import Process, Lock

# Constantes
TIME_WRITE = 10  # lo que tarda en escribir los datos de una música

# lo que tarda en volver a intentar agregar una música
TIME_WAIT_MIN = 7
TIME_WAIT_MAX = 15

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


# Función para agregar una canción a la lista
def add_song(song, song_list_file, lock):
    print(f"(>) {song.added_by} intenga agregar una música")
    if not lock.acquire(block=False):
        print("(!) Ya Existe un usuario que está agregando una canción")
        time.sleep(1)
        return False
    elif song_exists(song, song_list_file):
        time.sleep(TIME_WRITE)
        print(f"(-) La música '{song.title}' ya está agregada")
        lock.release()
        return False

    time.sleep(TIME_WRITE)
    with open(song_list_file, "a", newline="") as file:
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
    lock.release()
    return True


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


# Función para verificar si una canción ya está en la lista
def song_exists(song, song_list_file):
    with open(song_list_file, "r") as file:
        reader = csv.reader(file)
        try:
            for i in reader:
                if song.title == i[0] and song.artist == i[1] and song.album == i[2]:
                    return True
        except csv.Error as e:
            sys.exit("archivo {}, linea {}: {}".format(file, reader.line_num, e))
    return False


def user_process(song_list_file, username, new_songs, lock):
    while True:
        new_song = random.choice(new_songs)
        new_song.added_by = username

        # Validar si la canción ya existe en la lista
        if add_song(new_song, song_list_file, lock):
            print(f"(+) Música '{new_song.title}' agregada por {new_song.added_by}")
        time.sleep(random.randint(TIME_WAIT_MIN, TIME_WAIT_MAX))


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
    sounds_list = [new_song1, new_song2, new_song3, new_song4, new_song5, new_song6, new_song7, new_song8]

    lock = Lock()

    p_display = Process(target=display_song_list, args=(song_list_file,))
    p_user1 = Process(
        target=user_process,
        args=(
            song_list_file,
            "Juan",
            sounds_list,
            lock,
        ),
    )
    p_user2 = Process(
        target=user_process,
        args=(
            song_list_file,
            "Maria",
            sounds_list,
            lock,
        ),
    )
    #p_display.start() # en display.py se ejecuta por separado para no molestar visualmente
    p_user1.start()
    p_user2.start()

    #p_display.join()
    p_user1.join()
    p_user2.join()
