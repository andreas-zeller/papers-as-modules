import random

def fuzzer(max_length=100, char_start=32, char_range=32):
    """A string of up to `max_length` characters 
       in the range [`char_start`, `char_start` + `char_range`]"""
    string_length = random.randrange(0, max_length)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out
    
def evaluation(fuzzer=fuzzer, tries=100):
    """Evaluate `fuzzer()` function `tries` times;
       report average and max length"""

    sum_length = 0
    max_length = 0
    for i in range(tries):
        s = fuzzer()
        sum_length += len(s)
        max_length = max(max_length, len(s))

    avg_length = sum_length / tries
    result = {
        "average_length": avg_length,
        "max_length": max_length
    }
    return result

    
    