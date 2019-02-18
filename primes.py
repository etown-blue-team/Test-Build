class Primes:
    def is_prime(number):
        for element in range(2,number):
            if number % element == 0:
                return False

        return True

    def get_next_prime(self,number):
        index = number
        while True:
            index += 1
            if self.is_prime(index):
                print(index)
                return index