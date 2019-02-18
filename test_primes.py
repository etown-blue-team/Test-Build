from primes import Primes



def test_is_prime():
    assert Primes.is_prime(5) == True

def test_is_not_prime():
    assert Primes.is_prime(4) == False

def test_next_prime():
    assert Primes.get_next_prime(Primes,542) == 547