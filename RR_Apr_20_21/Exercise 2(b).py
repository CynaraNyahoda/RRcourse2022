##### Exercise 2(b)

def reverse_digits(number: int) -> int:
    """Return number with its digits in the opposite order."""
    return int(str(number)[::-1]) # reverse characters in number parameter converted to string
print (reverse_digits(12345678))
