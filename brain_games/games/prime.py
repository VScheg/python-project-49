def is_prime(number: int) -> bool:
    """Check if number is prime."""
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
