# Scout Crooke, 11/5/19, This program


def list_nums():
    max_num = int(input("What is the maximum number you would like to use?"))
    num_list = []
    for x in range(2, max_num + 1):
        num_list.append(x)
    return num_list


def prime_list(num_list):
    primes = []
    while len(num_list) > 0:
        num = num_list[0]
        primes.append(num_list[0])
        for x in num_list:
            if x % num == 0:
                num_list.remove(x)
            print(num_list)
        return primes


def main():
    num_list = list_nums()
    print("The list of prime numbers is:", prime_list(num_list))


main()
