from multiprocessing import Process

from messaging import launcher

if __name__ == '__main__':
    p1 = Process(target=launcher.start_process("192.168.0.14"), args=('bob',))
    p1.start()



