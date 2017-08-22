#coding=utf-8
import threading
import time
import numpy as np
import os,re,sys,shutil
reload(sys)
sys.setdefaultencoding('utf8')  # @UndefinedVariable
########################################################################
class print_data(threading.Thread):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        threading.Thread.__init__(self)
    #----------------------------------------------------------------------
    def run(self):
        """"""
        while True:
            global text_array, mutex
            print "====================print begin!======================"
            print "%s: %s" %(self.name, time.ctime(time.time()))  
            if mutex.acquire():
                print "len:" + str(len(text_array))
                for i in range(0, len(text_array)):
                    print str(i) + text_array[i]
                mutex.release()
            print "====================print finished!======================"        
            time.sleep(2) 
        

########################################################################
class chanage(threading.Thread):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        threading.Thread.__init__(self)
    #----------------------------------------------------------------------
    def run(self):        
        while True:
            print "====================refresh begin!======================"
            print "%s: %s" %(self.name, time.ctime(time.time()))
            global text_array, mutex
            if mutex.acquire():
                text_array = np.loadtxt("0.txt", dtype=np.str)   
                mutex.release()
            print "====================refresh finished!======================"
            time.sleep(2)         
    
    
## 为线程定义一个函数
#def print_data(threadName, delay):
    #while True:
        #global text_array
        #print "====================print begin!======================"
        #print "%s: %s" %(threadName, time.ctime(time.time()))  
        #print "len:" + str(len(text_array))
        #for i in range(0, len(text_array)):
            #print "len:" + str(len(text_array))
            #print str(i) + text_array[i]
        #print "====================print finished!======================"
         
#def change(threadName, delay):
    #while True:
        #print "====================refresh begin!======================"
        #print "%s: %s" %(threadName, time.ctime(time.time()))
        #global text_array
        #text_array = np.loadtxt("0.txt", dtype=np.str)     
        #print "====================refresh finished!======================"
        #time.sleep(delay)       

text_array = np.zeros(10000, dtype=np.str)
mutex = threading.Lock()

if __name__ == '__main__':
    # 创建两个线程
    try:
        #thread.start_new_thread( change, ("Thread-change", 5))
        #thread.start_new_thread( print_data, ("Thread-print_data", 10))
        
        #for i in range(0, len(text_array)):
            #print str(i) + text_array[i]    
        chanageThread = chanage()
        #printThread = print_data()
        chanageThread.start()
        #printThread.start()
        
        while True:
            print "====================print begin!======================"
            print "%s" %(time.ctime(time.time()))  
            if mutex.acquire():
                print "len:" + str(len(text_array))
                for i in range(0, len(text_array)):
                    print str(i) + text_array[i]
                mutex.release()
            print "====================print finished!======================"        
            time.sleep(2) 
    except:
        print "Error: unable to start thread"
    
    while 1:
        pass
