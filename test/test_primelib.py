
import numpy as np

from primelib.primelib import isPrime2
from pathlib import Path

def test_prime():
    test_dir = Path.cwd() / 'test'
    text_files = test_dir.glob("*.txt")
    prime_list = np.array([])
    for file in text_files:    
        with open(file, encoding='utf-8-sig') as f:
            prime_list = np.append(prime_list, [int(prime) for prime in f.read().splitlines()])

    Pass = []
    for i in prime_list:
        Pass.append(isPrime2(i))

    assert len(Pass) == sum(Pass)
   