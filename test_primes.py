from primes import is_prime

def test_is_prime():
    assert is_prime(5) == True

def test_is_not_prime():
    assert is_prime(4) == False