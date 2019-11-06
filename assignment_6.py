# Scout Crooke, 11/5/19,
# This program finds all the prime numbers in a list of numbers from 2 to the user's given number


def list_nums():
    """
    This function gets the maximum number from the user and generates a list from 2 to that maximum number
    :return: a list from 2 to the user's maximum number
    """
    max_num = int(input("What is the maximum number you would like to use?"))
    num_list = []
    for x in range(2, max_num + 1):
        num_list.append(x)
    return num_list


def prime_list(num_list):
    """
    This function loops through the list from 2 to the maximum number and finds the prime numbers and eliminates
    the numbers that are not prime numbers (multiples of the prime numbers).
    :param num_list:
    :return: the list of prime numbers
    """
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
