## Mode 4 - Reading phrases and passwords as a stream from an external generator
<img width="954" height="401" alt="Image" src="https://github.com/user-attachments/assets/e7b4980d-09f9-4ed1-b34b-d6fd50d6de42" /><br>
Accepts everything. Generate passwords, phrases, numbers, seeds, hex...<br>
```passwords -> pbkdf2_hmac_sha512 -> addresses```

### Generate datatimes
```
from datetime import datetime, timedelta

for i in range(500000000):
	v = datetime.now() - timedelta(seconds=i)
	print(v.strftime("%a %b %d %H:%M:%S %Y"))
	dw = v.strftime("%Y-%m-%d %H:%M:%S")
	print(dw)
```

### Generate electrum v1 phrases 12 words from pass

```
import string
import itertools
import hashlib
from hdwallet.entropies import (
    ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics import (
    ElectrumV1Mnemonic, ELECTRUM_V1_MNEMONIC_LANGUAGES
)
from hdwallet.seeds import ElectrumV1Seed
from hdwallet.hds import ElectrumV1HD
from hdwallet.derivations import ElectrumDerivation
from hdwallet.consts import PUBLIC_KEY_TYPES


def alphanumeric_strings():
    for n in itertools.count():
        for t in itertools.product(string.ascii_lowercase + string.digits, repeat=n):
            yield ''.join(t)

for x in alphanumeric_strings():
    #keypair = hashlib.sha256(x.encode()).hexdigest()
    keypair = hashlib.md5(x.encode()).hexdigest()
    # Generate Electrum-V1 entropy
    entropy: str = ElectrumV1Entropy.generate(
    strength=ELECTRUM_V1_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
    )
    electrum_v1_entropy: ElectrumV1Entropy = ElectrumV1Entropy(entropy=keypair)


    # Generate Electrum-V1 mnemonic
    mnemonic: str = ElectrumV1Mnemonic.from_entropy(
    entropy=electrum_v1_entropy, language=ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH)
    electrum_v1_mnemonic: ElectrumV1Mnemonic = ElectrumV1Mnemonic(mnemonic=mnemonic)
    print(electrum_v1_mnemonic.mnemonic())

```

## Mode 6 - Reading entropy stream from external generator
<img width="681" height="648" alt="Image" src="https://github.com/user-attachments/assets/75f3f580-bb3e-435a-a6e3-d4264de95fdd" /><br>
Make a random generator with vulnerable entropy 64, 96, 128, 160, 192, 224, 256 bit. <br>
Search, there are many different randoms on github.
How does it work?
The generator passes the hash to the program.<br>
bip39scan creates (based on the length) of the hash a mnemonic phrase, checks the addresses against the database<br>
```87659e70ff0aeb3c272f219f8806ae1fc96b13626c85a73d35ca569f7056f5c9 -> create mnemonic -> pbkdf2_hmac_sha512 -> addresses```

## C++ random 256 bit (simplest)
```
#include <iostream>
#include <time.h>
using namespace std;

int main() {

    for (int ik = 0; ik < 2000000000; ik++) {
        char result[64];
        char word[] = "abcdef1234567890";
        srand(time(NULL));

        for (int i = 0; i < 64; i++) {
            result[i] = word[rand() % 16];
            cout << result[i];
        }
        cout << "\n";
    }
}

```
## Python (pass -> sha256 = 256 bit entropy)
### Three lines of code

```
import os

while True:
	print(os.urandom(32).hex())
```


```
import string
import itertools
import hashlib
# + string.digits
def alphanumeric_strings():
    for n in itertools.count():
        for t in itertools.product(string.ascii_lowercase + string.digits, repeat=n):
            yield ''.join(t)

for x in alphanumeric_strings():
    keypair = hashlib.sha256(x.encode()).hexdigest()
    print(keypair)

```

## Mode 9 - BIP32
Here is a slightly different algorithm, salt.<br>
![Image](https://github.com/user-attachments/assets/f8c053d4-4a0f-461e-9bf6-34fb8d5ca3c9)<br>
```000102030405060708090a0b0c0d0e0f0f0e0d0c0b0a09080706050403020100 -> hmac_sha512 salt = "Bitcoin seed" -> addresses```

## Python passwords from file -> sha256 + md5 -> entropy
```
import hashlib
import string

with open("file.txt", "r", encoding='utf_8_sig', errors='ignore') as f:
       while True:
           line = f.readline()
           if not line:
               break
           keypair = hashlib.sha256(line.encode()).hexdigest()
           print(keypair1)
           keypair2 = hashlib.md5(line.encode()).hexdigest()
           print(keypair2)
```


# List of other generator examples 
### Radmom 16 bytes (128 bit)

```
import base64
import hashlib
import random

for i in range(2000000000):
	entropy = bytes([random.getrandbits(8) for i in range(16)])
	print(entropy.hex())
```

```
import os
import random

size = 32;

def generate_medium_entropy_block(size):
    """Generate a block with medium entropy using a biased random pattern."""
    # Use a limited set of bytes to reduce entropy slightly
    byte_pool = bytes([random.randint(0, 255) for _ in range(32)])
    return bytes(random.choice(byte_pool) for _ in range(size))

def generate_high_entropy_block(size):
    """Generate a block of pure random bytes (high entropy)."""
    return os.urandom(size)


for i in range(2000000000):
	block = generate_high_entropy_block(32)
	print(block.hex())
	block2 = generate_medium_entropy_block(32)
	print(block2.hex())

```

```
import hashlib
import string

with open("file.txt", "r", encoding='utf_8_sig', errors='ignore') as f:
       while True:
           line = f.readline()
           if not line:
               break
           keypair = hashlib.sha256(line.encode()).hexdigest()
           print(keypair)
           keypair32 = keypair[:32]
           print(keypair32)
           keypair33 = keypair[32:]
           print(keypair33)
           for i in range(10):
           	   keypair = hashlib.sha256(keypair.encode()).hexdigest()
           	   print(keypair)
           	   keypair322 = keypair[:32]
           	   print(keypair322)
           	   keypair333 = keypair[32:]
           	   print(keypair333)
```

```
import string
import itertools
import hashlib
def alphanumeric_strings():
    for n in itertools.count():
        for t in itertools.product(string.ascii_lowercase + string.digits, repeat=n):
            yield ''.join(t)

for x in alphanumeric_strings():
	keypair = hashlib.sha256(x.encode()).hexdigest()
	print(keypair)
	for i in range(100):
		keypair = hashlib.sha256(keypair.encode()).hexdigest()
		print(keypair)
		keypair32 = keypair[:32]
		print(keypair32)
		keypair33 = keypair[32:]
		print(keypair33)

```
### List of vulnerable generators (examples)

```
import asyncio
import datetime
import json
import os
import random
import keyboard
import aiohttp
import re
import configparser
import pyfiglet
import hashlib
from bitcoinlib.keys import Key
from bitcoinlib.mnemonic import Mnemonic as BitcoinMnemonic
import secrets
from collections import deque
import itertools
import struct
import time

for i in range(2000000000):
	entropy = secrets.token_bytes(16 if 12 == 12 else 32)
	print(entropy.hex())
	entropy2 = secrets.token_bytes(16 if 24== 12 else 32)
	print(entropy2.hex())
	
	bulka = random.choice([bytes([random.randint(1, 255)] * 32), bytes([0xAA, 0xBB] * 16)])
	bulka2 = random.choice([b'\x00' * 28 + os.urandom(4), os.urandom(4) + b'\x00' * 28])
	bulka3 = random.choice([bytes(range(32)), b'\xDE\xAD\xBE\xEF' * 8])
	print(bulka.hex())
	print(bulka2.hex())
	print(bulka3.hex())
	
	bulka11 = random.choice([bytes([random.randint(1, 255)] * 16), bytes([0xAA, 0xBB] * 8)])
	bulka22 = random.choice([b'\x00' * 28 + os.urandom(4), os.urandom(4) + b'\x00' * 14])
	print(bulka11.hex())
	print(bulka22.hex())

	timestamp = int(datetime.datetime.now().timestamp() * 1000000)
	weak_entropy = secrets.randbits(32)
	seed = (timestamp ^ weak_entropy) & 0xFFFFFFFF
	random.seed(seed + random.getrandbits(16))
	weak_bytes = bytes([random.randint(0, 255) for _ in range(32)])
	print(weak_bytes.hex())
	
	timestamp = int(datetime.datetime.now().timestamp() * 1000000)
	weak_entropy = secrets.randbits(16)
	seed = (timestamp ^ weak_entropy) & 0xFFFFFFFF
	random.seed(seed + random.getrandbits(16))
	weak_bytes = bytes([random.randint(0, 255) for _ in range(16)])
	print(weak_bytes.hex())
	
	bobr = bytes([random.randint(1, 255)] * 32)  # Повторяющийся случайный байт
	print(bobr.hex())
	bobra = bytes([random.randint(1, 255)] * 16)  # Повторяющийся случайный байт
	print(bobra.hex())
	bobr2 = b'\x00' * 16 + os.urandom(16)  # Половина нулей, половина случайных
	print(bobr2.hex())
	bobr22 = b'\x00' * 8 + os.urandom(8)  # Половина нулей, половина случайных
	print(bobr22.hex())
	
	bobr3 = bytes([i % 256 for i in range(32)])  # Последовательные байты
	print(bobr3.hex())
	
	bobr4 = bytes([0xAB, 0xCD] * 16)  # Чередование двух байтов
	print(bobr4.hex())
	bobr44 = bytes([0xAB, 0xCD] * 8)  # Чередование двух байтов
	print(bobr44.hex())
	
	bobr5 = bytes(list(range(16)) + list(range(15, -1, -1)))  # Зеркальная последовательность
	print(bobr5.hex())

	
	bobr6 = bytes([(i + random.randint(1, 255)) % 256 for i in range(32)])  # Сдвиг случайного байта
	print(bobr6.hex())
	bobr66 = bytes([(i + random.randint(1, 255)) % 256 for i in range(16)])  # Сдвиг случайного байта
	print(bobr66.hex())
	
	bobr7 = struct.pack(">32s", int(time.time() * 1000).to_bytes(32, byteorder='big'))  # Ключ на основе времени
	print(bobr7.hex())
	bobr77 = struct.pack(">32s", int(time.time() * 1000).to_bytes(16, byteorder='big'))  # Ключ на основе времени
	print(bobr77.hex())
	
	bobr8 = bytes([random.randint(0, 255) if i % 2 == 0 else 0xAA for i in range(32)])  # Чередование случайного и фиксированного
	print(bobr8.hex())
	bobr88 = bytes([random.randint(0, 255) if i % 2 == 0 else 0xAA for i in range(16)])  # Чередование случайного и фиксированного
	print(bobr88.hex())
	
	bobr9 = bytes([min(i * 17 % 255, 255) for i in range(32)])  # Пилообразный узор
	print(bobr9.hex())
	bobr99 = bytes([min(i * 17 % 255, 255) for i in range(16)])  # Пилообразный узор
	print(bobr99.hex())
	
	bobr10 = bytes(([random.randint(1, 255)] * 2 + [random.randint(0, 255)] * 2) * 8)  # Случайные пары байтов
	print(bobr10.hex())
	bobr100 = bytes(([random.randint(1, 255)] * 2 + [random.randint(0, 255)] * 2) * 4)  # Случайные пары байтов
	print(bobr100.hex())
	
	bobr11 = bytes([0xDE, 0xAD, 0xBE, 0xEF] * 8)  # "Магические" числа
	print(bobr11.hex())
	bobr12 = b'\x42\x42\x42\x42' + os.urandom(28)  # Фиксированный префикс + случайные
	print(bobr12.hex())

```

```
import hashlib
import string

with open("file.txt", "r", encoding='utf_8_sig', errors='ignore') as f:
       while True:
           line = f.readline()
           if not line:
               break

           keypair = hashlib.sha256(line.encode()).hexdigest()
           print(keypair)
           for i in range(6):
           	   if i == 1:
           	   	keypair1 = keypair[:32]
           	   	print(keypair1)
           	   
           	   if i == 2:
           	   	keypair2 = keypair[32:]
           	   	print(keypair2)
           	   
           	   if i == 3:
           	   	keypair3 = hashlib.md5(line.encode()).hexdigest()
           	   	print(keypair3)
           	   
           	   if i == 4:
           	   	keypair4 = hashlib.sha3_256(line.encode()).hexdigest()
           	   	print(keypair4)
           	   
           	   if i == 5:
           	   	keypair5 = hashlib.shake_128(line.encode()).hexdigest(16)
           	   	print(keypair5)
           	   
           	   if i == 6:
           	   	keypair6 = hashlib.shake_256(line.encode()).hexdigest(32)
           	   	print(keypair6)
```
