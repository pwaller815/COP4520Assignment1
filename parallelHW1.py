# Parker Waller
# COP4520
# HW1
# 1/24/24

from threading import Thread
import time

end = 10**8
primes = [True for _ in range(end)]

def findPrimes(n):
    while n < end:
        if primes[n]:
           for i in range(n*n, end, n):
               primes[i] = False
        n += 8

def main():
    t = time.time()
    
    threads = []
    # Intialize and start threads
    for i in range(8):
        thr = Thread(target=findPrimes,args=(i+2,))
        thr.start()
        threads.append(thr)
    # Join threads
    for thr in threads:
        thr.join()
    t = time.time() - t
    
    # Convert and write to file
    result = []
    for i in range(2, len(primes)):
        if primes[i]:
            result.append(i)
    
    fp = open("primes.txt", "w")
    fp.write("" + str(t) + " " + str(len(result)) + " " + str(sum(result)) + "\n")
    for i in range(-10, 0):
        fp.write(str(result[i]) + " ")

main()
