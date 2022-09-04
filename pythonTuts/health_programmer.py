from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


    while True:
        input_of_user = input()
        if input_of_user==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt" , "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musicloop("ring.mp3" , "stop")
    init_water = time()
    init_eyes = time()
    init_exer = time()
    watersec = 30*60
    exersec = 60*60
    eyesec = 45*60

    while True:
        if time()-init_water>watersec:
            print("water drinking time , Enter 'drunk' to stop alarm...." )
            musicloop("ring.mp3" ,"drunk")
            init_water = time()
            log_now("Drunk water at")

        if time() - init_eyes > eyesec:
            print("water drinking time , Enter 'done eye' to stop alarm....")
            musicloop("ring.mp3", "done eye")
            init_eyes = time()
            log_now("Eye Relexed at")

        if time() - init_exer > exersec:
            print("water drinking time , Enter 'done' to stop alarm....")
            musicloop("ring.mp3", "done")
            init_exer = time()
            log_now("Pycical activity done at")




