# 79.170.167.30

# HOST = '79.170.167.30'
# PORT = 58596

# test-client.py
import multiprocessing
import socket
import sys



# sockets
'''import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('79.170.167.30', 58596)
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:

    mess = 'Hello Wоrld!'
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)


    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')

finally:
    print('Закрываем сокет')
    sock.close()'''

import kivymd

from kivymd.app import MDApp

from kivymd.uix.screen import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem

class MyApp(MDApp):
    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(20):
            items = OneLineListItem(text='Item '+str(i))
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen
if __name__ == '__main__':
    MyApp().run()


'''import os
import multiprocessing as mp
from multiprocessing import Process
def c(tet,x):
    with open(tet, 'a') as n:
        n.write(x+" - "+multiprocessing.current_process().name+"\n")
def f(x):
    f.q.put('Doing: ' + str(x))
    print( multiprocessing.current_process().name+"\n")
    tet = multiprocessing.current_process().name +".txt"
    c(tet=tet, x=x)
    return x

def f_init(q):
    f.q = q

def func(jobs,q):
    time.sleep(20)
    for i in range(len(jobs)):
        print(q.qsize())
        print(q.get())
        time.sleep(5)

def main():
    jobs = ["polo","solo","olo","polo1","solo1","olo1"]

    q = mp.Queue()
    p = mp.Pool(3, f_init, [q])

    proc = Process(target=func, args=(jobs,q))
    proc.start()

    p.imap(f, jobs)
    p.close()

    while True:
        x = input("Узнать сколько в очереди: ")
        if x == 'q':
            print(q.qsize())



if __name__ == '__main__':
    main()
'''
'''import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())'''

















