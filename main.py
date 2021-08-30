import screen1
from threading import Thread

def screen1_check_for_exit_code():
    while True:
        if screen1.quit__ == 0:
            print('GOOD')
        elif screen1.quit__ == 1:
            print('BAD')

t= Thread(target=screen1_check_for_exit_code)
t.start()