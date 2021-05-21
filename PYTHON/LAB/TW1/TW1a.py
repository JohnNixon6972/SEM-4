# WAP to Demonstrate the algorithm Seive of eratosthenes
# to print the prime numbers from 1 to till N

import math

def sieveOfEratosthenes(N):

    prime = [True] * N
    prime[0] = False
    for i in range(2, int(math.sqrt(N))+1):
        for j in range(i*2, N, i):
            prime[j] = False

    print("All the prime numbers till",N,"are: ")
    for i in range(2, N):
        if prime[i]:
            print(i, end=" ")
    print()

def main():
    N = int(input("Enter the value of N: "))
    sieveOfEratosthenes(N)

if __name__ == "__main__":
    main()