# COP4520Assignment1

To run this program first download the file parallelHW1.py; save the file anywhere you desire. Next using a command prompt navigate to the directory you saved the file in.
Once there, use the command following command to run the script:

python parallelHW1.py

# Evaluation/Summary of approach

When approaching the problem of finding all primes between 1 and 10^8 using 8 threads, I decided to make use of the Sieve of Eratosthenes algorithm. This was because the runtime limits for this assignment were demanding and I needed the fastest avaliable method of finding all primes between 1 and 10^8. I had to modify the Sieve of Eratosthenes because its base design is based on the use of only one thread. In-order to efficiently distribute the workload across all 8 threads this was necessary, I provided each thread with a different consecutive starting number (2,3..9) and consecutively made the call to start each thread using the Sieve of Eratosthenes. Once the thread started its call to the function it is met with a while loop which runs until the starting number it was given becomes greater than 10^8. At the end of the while loop the starting number is incremented by 8, this is to account for the total number of threads and prevent the threads from encountering the same number. 

The design of my program ensures the workload is efficiently distributed across all 8 threads. It also ensures that no thread will encounter the same number as another when evaluating primes.
