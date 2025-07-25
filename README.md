# bip39scan - New reliase v 4.0.1 (22/07/2025) - $500

**MultiGPU program brute force mnemonic phrases**<br>
Supports all patches, ETH, BTC, DOGE, LITE, dash, BTC Cash, addresses and ETH tokens.<br>
Automatically detects the coin type based on the given patch. You can specify the type manually.<br> 
Supports brute force 6, 9, 12, 15, 18, 21, 24 words<br> 

| GPU card | 24 words speed | 18 words speed | 12 words speed | Stream, reading from file, other brute |
|----------|---------------|----------------|----------------|----------------------------------------|
| **RTX 5090** | **250M** mnemo/s	| **63M** mnemo/s	| **17M** mnemo/s | 800k phrases/s - 500k entropy/s |
| **RTX 4090** | **160M** mnemo/s | **38M** mnemo/s	| **11M** mnemo/s | 530k phrases/s - 300k entropy/s | 
* The speed is indicated when checking 10 addresses in each phrase.
* If you reduce the number of addresses checked, the speed will be higher.
* The size of the address base does not affect the speed +-5%

The program is sold with the source code! cmake VS2022<br>
The kit includes ready-made programs for Windows x64 and Linux (Ubuntu and hiveos)<br>
To purchase, write to telegram ```@phrutis``` or buy from a bot in a group https://t.me/cuda8

## Linux (Ubuntu, hiveos)
The commands are the same as for Windows.<br>
You need to add in patch \ before '

```chmod +x bip39scan```<br>
```./bip39scan -a eth.bin -t ethereum --bloom 2048M --save Found.txt -p m/44\'/60\'/0\'/0/0-9 ...```

# Modes:
## 1. Sequential search words:
```
bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 uncover figure script * obscure waste metal quit depend bachelor trust erupt * impose brave leave number rapid oak wealth reopen * noodle tragic
```
In the phrase, 3 missing words in different positions are replaced by * (test address 14aZB9i8NFiXpeGbS3g7vLArhL7EbNBSWS)

[![Image](https://github.com/user-attachments/assets/0a4e85ae-166f-41ae-b406-16c736e38d17)](https://github.com/user-attachments/assets/e8d4535c-ea78-410f-8ec9-2608847ce975)

```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 cause ensure shield option monkey infant tray okay remember * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 carpet * recycle force since * update glare seminar * worth answer
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 * ostrich * kitten * unit glow tortoise world crop kit curve
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 right elevator dust radio please prison cup omit require also decorate sock
```
You can use your own list of words from a text file for searching. Only words from the [2048 mnemonic words](https://github.com/phrutis/bip39scan/blob/main/bip39.txt) are supported.<br>
Words in the file must be on a new line. To add a specified list, use ```-w words.txt``` Replace unknown words with *<br>

## 2. Random words:
```
bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 -w mywordlist.txt -r uncover figure script * obscure waste * quit depend bachelor trust erupt * impose brave leave number rapid oak * reopen * noodle tragic
```
https://github.com/user-attachments/assets/2d9d24c7-8844-4de4-9e5d-7eba976d021e

**Replace unknown words with** **\***<br>
**Standard random 2048 words in positions with** **\***<br>
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 -r cause * shield option monkey infant tray okay remember * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 -r carpet * recycle * since * update glare seminar * worth answer
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 -r * ostrich * * * unit glow tortoise world crop kit curve
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 -r * * * * * prison cup omit require also decorate sock
```


**Random using your list of mnemonic words from the file words.txt**<br>
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 -w words.txt -r cause * shield option monkey infant tray okay remember * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 -w words.txt -r carpet * recycle * since * update glare seminar * worth answer
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 -w words.txt -r * ostrich * * * unit glow tortoise world crop kit curve
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 -w words.txt -r * * * * * prison cup omit require also decorate sock
```

**For full random, add only stars**<br>
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 -r * * * * * * * * * * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 -r * * * * * * * * * * * *
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 -r * * * * * * * * * * * *
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 -r * * * * * * * * * * * *
```

## 3. Reading phrases and passwords from a text file:
**The program reads everything from the file: phrases, passwords, passphrases, words, numbers...**<br>
There are many finds on them. Supports dictionaries up to 64 TB.

https://github.com/user-attachments/assets/b981b17f-db42-41a7-adb8-3b6dc7d73803

```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 -m dict.txt
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 -m dict.txt
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 -m dict.txt
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 -m dict.txt
```

## 4. Reading phrases and passwords as a stream from an external generator
Use ```-m stdin```<br>
Use your own masks, dictionaries, rules, or other generators<br>

https://github.com/user-attachments/assets/5d930d3d-4224-4316-8f8f-87a721e21ec8

```
hashcat.exe --stdout -a 3 -1 ?u?l ?1?l?l?l?d?d?d?d | bip39scan.exe -m stdin -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9
```
```
hashcat.exe --stdout -a 3 -1 ?u?l ?1?l?l?l?d?d?d?d | bip39scan.exe -m stdin -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9
```
```
hashcat.exe --stdout -a 3 -1 ?u?l ?1?l?l?l?d?d?d?d | bip39scan.exe -m stdin -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9
```
```
hashcat.exe --stdout -a 3 -1 ?u?l ?1?l?l?l?d?d?d?d | bip39scan.exe -m stdin -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9
```

## 5. Reading entropy from file
Entropy must be in hex format with a new line.<br>
Depending on the length of the hash, a phrase is created.
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 -e entropy.txt
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 -e entropy.txt
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 -e entropy.txt
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 -e entropy.txt
```

## 6. Reading entropy stream from external generator
Now you don't need to modify the program for the next vulnerability.<br>
Create your own generators based on Python or C++ code.<br>
There are many vulnerable random generators on the Internet (github).<br>
Print the entropy in hex format, done.<br>
The program will determine the length of the hex and create a phrase of the required length itself.

https://github.com/user-attachments/assets/df8a0774-307a-46e0-ac01-b9123aad5c50

```
py 128bit.py | bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 -e stdin
```
```
py entropy.py | bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 -e stdin
```
```
py md5.py | bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 -e stdin
```
```
py 256.py | bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 -e stdin
```


## 7. Use the built-in generator passwords
In 2015-2016, there was an online service live.ether where everyone could generate addresses using passwords.<br>
At first https://live.ether.camp they generated from camp 2031 iteration of SHA-3 (Keccak)<br>
then switched to a more secure generation of pbkdf2_hmac_sha512 2048 iterations.<br>
The service worked for about a year and closed, the wallets remained.<br>
![live.ether](https://github.com/user-attachments/assets/7cba4517-5f2e-4b3a-986a-4cace21cc5fa)<br>
Many finds by generator and passwords from file<br>
You can see the [list of found passwords 7165 pcs.](https://github.com/phrutis/bip39scan/blob/main/Founds.md)<br>
In the alpha.txt file, specify your alphabet, numbers, symbols in a line.<br>
The generator works with an increment increasing the password length.

https://github.com/user-attachments/assets/d0fc2faa-b0bb-4f7b-8c4e-575972a0cb26

```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 --alphabet alpha.txt --start a
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 --alphabet alpha.txt --start a
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 --alphabet alpha.txt --start a
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 --alphabet alpha.txt --start a
```
Every 5 minutes the progress status is written to the file status.txt<br>
To continue, copy the position from status.txt and run --start FromHire1<br>
If there is a space in the start word, run it like this --start "From Hire 1"<br>

https://github.com/user-attachments/assets/313156e0-d82e-499d-a5c0-644e067d76cd

Important! The symbols from the starting position must be present in the alphabet.<br>


## 8. Vulnerable generator libbitcoin explorer v3.2
More about the vulnerability Milk Sad:<br>
RU https://habr.com/ru/articles/771980/<br>
EN https://milksad.info<br>
EN https://milksad.info/disclosure.html#codename-milk-sad<br>
 
bip39scan generates all possible mnemonics across the entire 32-bit<br>
Not everyone knows about this vulnerability. Some sites and applications still use this vulnerable library.<br>
Therefore, the chance to find a fresh coin is very high. Update your address databases.<br>
The main advantage of bip39scan v3 is its high speed!

### The program's operating principle:<br>
When first launched, the program checks all 4294967296 phrases in vulnerable 32 bits of entropy.<br>
At a speed of 550k phrases per second - this is only 2 hours of brute force.<br>
Perhaps with a fresh address base there is a chance to find a fresh coin.<br> 
There is also a chance to find by a non-standard patch or a rare coin, token.<br>
After that, the program again goes through 32 bits of entropy but with greater depth, as if the entropy was generated a second time.<br>
Then, the third, fourth ... the program searches indefinitely.<br>
No one has used this method! There are finds with a positive balance for it.

https://github.com/user-attachments/assets/8c33254d-46a7-4570-a9e4-3d6d39d87693

Vulnerability 32 bits in each phrase length, in each language from the list. <br>
Also several patches + different coins. This is for years of searching. <br>
There are finds with a positive balance - this indicates that not everything was cleaned. <br>
Perhaps they did not have such a fast GPUs program as bip39scan.

[**View 27 finds BTC with positive balance**](https://github.com/phrutis/bip39scan/blob/main/Founds.md)<br>

[**Download all empty finds CSV FOUNDS.txt (219к phrases)**](https://github.com/phrutis/bip39scan/releases/download/4.0.1/FOUNDS.txt)<br>

Important! There is no continuation of the search.<br> 
If you stop brute force, start the program from the beginning, it will start searching all over again.<br> 
You will find what you found before until you reach the place where you stopped.

Unix timestamp range (from January 1, 1970, to January 19, 2038).<br>
date/time: 1970-01-01 00:00:00 for first timestamp. If chosen english ETH addresses pach ```m/44'/60'/0'/0/0-9```<br>
it will generate "milk sad ..." mnemonic<br>
<img width="977" height="511" alt="Image" src="https://github.com/user-attachments/assets/c38e79c6-08de-4b5c-8d85-f01f06bf7bba" /><br>

### Length of phrases
```--bits 64``` (random phrase 6 words)<br>
```--bits 96``` (random phrase 9 words)<br>
```--bits 128``` (random phrase 12 words)<br>
```--bits 160``` (random phrase 15 words)<br>
```--bits 192``` (random phrase 18 words)<br>
```--bits 224``` (random phrase 21 words)<br>
```--bits 256``` (random phrase 24 words)<br>

```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 --bits 192
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 --bits 256
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 --bits 224
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 --bits 128
```
### Phrase Languages
If not specified, the default will be en<br>
```-l en``` English phrases<br>
```-l es``` Spanish phrases<br>
```-l fr``` French phrases<br>
```-l it``` Italian phrases<br>
```-l ja``` Japanese phrases<br>
```-l cs``` Czech phrases<br>
```-l ru``` Russian phrases<br>
```-l uk``` Ukrainian phrases<br>
```-l zh_Hans``` Chinese (Simplified)<br>
```-l zh_Hant``` Chinese (Traditional)<br>
```-l ko``` Korean phrases<br>
```-l po``` Portuguese phrases<br>
```-l tu``` Turkish phrases<br>
<img width="978" height="325" alt="Image" src="https://github.com/user-attachments/assets/c3afa204-81df-49a4-9f7f-8b5e17bbdbad" /><br>

<img width="976" height="370" alt="Image" src="https://github.com/user-attachments/assets/e787746a-1646-428c-9865-d62ff85baf66" />

```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M --save Found.txt -p m/44'/0'/0'/0/0-9 --bits 192 -l tu
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M --save Found.txt -p m/49'/0'/0'/0/0-9 --bits 256 -l it
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M --save Found.txt -p m/84'/0'/0'/0/0-9 --bits 224 -l zh_Hans
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M --save Found.txt -p m/44'/60'/0'/0/0-9 --bits 128 -l fr
```

# Download ready-made address databases for bip39scan

**ALL ETH 1458757703 addresses with balance 09/07/2025** + empty + ALL ETH TOKENS with balance 09/07/2025 + empty history:<br>
ARBITRUM, AVALANCHE, BASE, BNB, BSC, BTT, CRONOS, CELO, ETC, Ethereumnie, ERA, ERC20, ETH, Ethered, FANTOM, <br>
GETH (Goerli), GNOSIS, IOTX, LINEA, MOONBEAM, MOONRIVER, OPBNB, OPTIMISM, POLYGON, VET, ZKEVM-POLYGON...<br>
**Doesn't start on 8 GB cards! The database fits on a 12 GB card or more.** <br>
**To run you need 32 GB of RAM (if you don't have that much, you can use the swap file)** <br>
Add these arguments to run ```--bloom 4096M -t ethereum```<br>
Download http://89.23.98.83/up/alleth.bin  **29 GB**

**ALL BTC addresses 1...** P2PKH with balance + empty (history)<br>
Add these arguments to run ```--bloom 2048M -t P2PKH```<br>
Download http://89.23.98.83/up/allbtc1.bin  **11.9 GB**

**ALL BTC addresses 3...** P2SH with balance + empty (history)<br>
Add these arguments to run ```--bloom 2048M -t P2SH```<br>
Download http://89.23.98.83/up/allbtc3.bin  **7.6 GB**

**ALL BTC addresses bc1q...** bech32 with balance + empty (history)<br>
Add these arguments to run ```--bloom 2048M -t bech32```<br>
Download http://89.23.98.83/up/allbc.bin  **6.5 GB**

**List OTHESR Databases .bin**<br>
see http://89.23.98.83/up/

## Addresses only with positive balance

Download ETH addresses 0x + tokens 02/07/2025<br>
```-t ethereum --bloom 2048M```<br>
http://89.23.98.83/up/eth.bin  **6.9 GB**

Download BTC addresses 1... 30/06/2025<br>
http://89.23.98.83/up/btc1.txt  **787 MB**

Download BTC addresses 3... 30/06/2025<br>
http://89.23.98.83/up/btc3.txt **240 MB**

Download BTC addresses bc... 30/06/2025<br>
http://89.23.98.83/up/bc.txt **842 MB**

Purchased ETH bases and tokens.<br>
The base was provided by the hunter.<br>
```-t ethereum --bloom 2048M```<br>
http://89.23.98.83/up/eth_parse.bin  **10.1 GB**

I recommend using large address bases.<br>
For example, BCH may remain on the historical address 1... (P2PKH)

Launching the program with a text database of addresses.<br>
Each address must be on a new line!<br>
The text address base is well suited for quick tests

```bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a btc3.txt -t P2SH -p m/49'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a btc-bc.txt -t bech32 -p m/84'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a eth_addresses.txt-t ethereum -p m/44'/60'/0'/0/0-9 --bits 256```

## Create your own .bin database from addresses

To avoid waiting for a long time for the addresses to be loaded into the program.<br>
Create and use binary databases.<br>
The program will start in seconds<br>
Create databases:<br>
BTC<br>
```bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH --save-bin btc1.bin -p m/44'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a btc3.txt -t P2SH --save-bin btc3.bin -p m/49'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a btc-bc.txt -t bech32 --save-bin bc.bin -p m/84'/0'/0'/0/0-9 --bits 256```

ETH and tokens<br>
```bip39scan.exe --save Found.txt -a eth_addresses.txt --save-bin eth.bin -t ethereum -p m/44'/60'/0'/0/0-9 --bits 256```

**Next launches run like this!** <br>
```bip39scan.exe --save Found.txt -a btc1.bin -t P2PKH -p m/44'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a btc3.bin -t P2SH -p m/49'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a bc.bin -t bech32 -p m/84'/0'/0'/0/0-9 --bits 256```<br>
```bip39scan.exe --save Found.txt -a alleth.bin --bloom 4096M -t ethereum -p m/44'/60'/0'/0/0-9 --bits 256```


Where can I download a fresh database of addresses?<br>
BTC and other coins https://blockchair.com/dumps<br>
Fresh ETH addresses + ETH Tokens taken from node dumps<br>
https://routescan.io/dumps?page=2&nexttoken=undefined<br>
Each address must be on a new line.<br>
Ethereum addresses must be 0x...<br>
Bitcoin addresses 1.., 3.., bc.. (New long addresses bc.. does not accept)

# FAQ

**The program did not find my test password from the file.**

Do not use small dictionaries for the test.<br>
The program starts in 3-5 seconds, at a speed of 500k, it can go through your dictionary of 25 phrases in 0.001 sec and finish the work without having time to give the result.<br>
I recommend using dictionaries from 5 million lines and more.<br>
The program has 65536 threads, while 50 threads processed your list, other threads (65511 empty) without load finished the program earlier.<hr>

**How to change the derivation in a patch?**

You can set a non-standard patch derivation at your discretion:<br>
m/0-9<br>
m/0/0-9<br>
m/0/0/0-9<br>
m/0-99/0-99/0-99<br>
m/44'/0-99'/0'/0/0-9<br>
m/0-99'/0-99'/0'/0-5/0-999<br>
max value: **2147483647**<br>
m/44'/0-2147483647'/0-2147483647'/0-2147483647/0-2147483647<hr>

**My program won't start - bloom memory error...?**

Take a screenshot of the program window and send it to me.

99% you made a mistake in the launch command.<br>
Most likely you did not specify the memory size for the filter.<br>
Base.bin 7 GB+ specify --bloom 2048M<br>
Base.bin 20 GB+ specify --bloom 4096M<br>
Base.bin 50 GB+ specify --bloom 8192M<hr>

**Where can I make a mnemonic from a password?**

Online generator http://89.23.98.83<br>
Bookmark this<hr>

**What is precomp.bin**?

This is a table of acceleration, pre-calculated points of the curve<hr>

**Words and letters from the previous generation remain (stick) in my window, how can I fix it?**

Languages or some characters may also be displayed incorrectly. <br>
These are properties of the correction and different language encodings.<br>
This does not affect the brute force process itself.<hr>

**What mode is better to search in? Where are there more prospects? Where and how much did you find?**

Try different modes and directions.<br>
Search in the one in which you think you have the best chance of finding.<br>
Finds are found, they are not asked about, and they are not told. When you find one, will you tell everyone?<hr>

**How can I search for other coins like Salona?**

Create several test addresses.<br>
Convert addresses to ripemd160 hashes.<br>
Be sure to sort 00...ff<br>
Run the program, specify the type, for example for BTC ```-t P2PKH```<br>
The program will find an empty address BTC 1.... you don't need it.<br>
Take the phrase, or private key, generate the address of the desired coin<br>
If you do everything correctly, you will find test addresses<hr>

**Why specify -t typecoin ?**

When you search with binary database the program does not know what coin you are looking for.<br>
BE SURE TO SPECIFY - t typecoin
<hr>

## bip39scan.exe -h
```
C:\Users\User\Downloads\bip39scan-win64>bip39scan -h
bip39scan v 4.0.1 (phrutis modification 22/07/2025)
Bruteforce bip39 mnemonics
Syntax: bip39scan [OPTIONS] [MNEMO]
OPTIONS:
    -h, --help            Print this message.
    -a, --addresses STR   The name of the address list, each address of a separate line, or a binary
                          file previosly created with --save-bin. Binary files are faster to read.
        --save-bin STR    The name of the binary file to write, 20 bytes per address. This is in order
                          to accelerate loading of addresses.
    -p, --path STR        Use this derivation path template, e.g. m/44'/60'/0-99'/0/0-99
                          The default is m/44'/0'/0-9'/0-1/0-9 for p2pkh addresses and ethereum,
                          m/49'/0'/0-9'/0-1/0-9 for p2sh addresses,
                          m/84'/0'/0-9'/0-1/0-9 for bech32 addresses.
    -v, --verbose         Print debug messages.
    -t, --type STR        Address type, one of P2SH, P2PKH_UNCOMPRESSED, P2PKH, bech32, ethereum
                          By default, address type is detected from the address file, if it's text.
                          This options is required when using binary data.
    -S, --save FILE       Save found results to the file.
    -m, --mnemo FILE      Read mnemonics from the file, one per line. -m stdin to read from the input pipe.
        --alphabet FILE   Generate mnemonics as passwords from the characters of the given file.
                          Not compatible with --mnemo option.
        --bits INT        Generate mnemonics using RNG of the libbitcoin explorer 3.2.0. The integer number is the entropy length:
                          64 - 6 words, 96 - 9 words, 128 - 12 words, 160 - 15 words, 192 - 18 words, 224 - 21 words
                          256 - 24 words.
    -e, --entropy FILE    Read entropy from the file in hex, one per line. If FILE is 'stdin', read from input pipe.
    -l, --lang STR        Language of the mnemonics generated with --bits, one of en, es, es-nfkd, ja, ja-nfkd, it, fr, cs, ru, uk, zh_Hans, zh_Hant, po, ko, tu.
                          Default is English.
        --start STR       For generated mnemonics, start from this mnemonic.
    -d, --devices STR     Comma-separated list of device indexes (indeces start with 0). By default,
                          run on all devices.
        --bloom NUM       Bloom filter size in GPU, in bytes. Can use K, M, and G suffixes. Default
                          is 1024M.
        --kernel NUL      GPU memory reserved for kernel execution, in bytes. Can use K, M, and G suffixes.
                          Default depends on the device.
        --ec-threads NUM  Number of threads for elliptic curve computations. Default is 128. Should be a multiplier of 32.
                          Set to 64 if you are experiencing out of memory errors.
    -w, --words FILE      Use custom dictionary for '*' placeholders in the mnemo template; each word in a separate text line.
                          Each word should be a valid BIP39 word in the specified language (--lang).
        --dump            Dumps valid mnemonics.
    -r, --random          Randomize the mnemonics generated with MNEMO templates (see below).
    MNEMO                 Mnemonic template, up to 24 words. Can contain placeholders '*'. If less than
                          12 words, the rest are placeholders. Each '*' is replaced with one of 2048 words (or one of the words
                          from the dictionary specified with --words option).

Example:
   > bip39scan -a addresses.txt -p m/0'/0-1 -m mnemo.txt
   > bip39scan -a addresses.txt -p m/0'/0-1 --alphabet characters.txt --start kaaaaaaa
```

## Building on Windows VS-2022

Install cmake 3.30+ from this link: https://github.com/Kitware/CMake/releases/download/v3.31.8/cmake-3.31.8-windows-x86_64.msi<br>
Or find another version on this page: https://cmake.org/download/<br>

Install Visual Studio 2022 community: https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2022<br>
click the big Download button
 
Install Nvidia CUDA 12.9: https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local<br>
choose Windows version
 
Install OpenSSL from https://slproweb.com/download/Win64OpenSSL-3_0_16.msi

Go to the "Sources" folder<br>
In cmd run: 

```cmake bip39scan```

The project files will appear in the folder:<br>
bip39scan.sln (run this file the project will open)<br>
bip39scan.vcxproj<br>
bip39scan.vcxproj.filters<br>
..

![brute bip39 phrases](https://github.com/user-attachments/assets/16e2197f-a01e-43ee-a02e-5b6f9e515e15)

OpenSSL should be found. If now, rename c:\program files\OpenSSL-Win64 to OpenSSL and re-run. Note that the libcrypto dll should<br>
be in PATH or in the current directory when running bip39scan.

 
Visual Studio 2022 opens. In the top toolbar choose: Release/x64.<br>
In the "Solution explorer" to the right, right-click bip39scan, choose "build".<br>
The executable builds in the your-build-directory\Release
 
![gpu brute bip39 mnemonic](https://github.com/user-attachments/assets/34d6574c-20a3-462c-a857-117ae9ae664f)

If necessary run precomp.exe file precomp.bin will be generated

## Building on Ubuntu:

Below is detailed instruction with bash commands required to build bip39scan.<br>
The symbol '$' denotes command prompt.<br>
If your prompt is shown as '#' on your terminal, skip 'sudo'.<br>
For example, instead of

$ sudo sh cuda_12.0.1_525.85.12_linux.run

you should run

sh cuda_12.0.1_525.85.12_linux.run

Let's start.

install CUDA. Download the linux version from the NVIDIA website and run.<br>
Open https://developer.nvidia.com/cuda-12-0-1-download-archive?target_os=Linux<br>
in your browser and choose your system. The following is valid for Ubuntu 18.04.

$ wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda_12.0.1_525.85.12_linux.run<br>
$ sudo sh cuda_12.0.1_525.85.12_linux.run

Skip the driver installation (deselect the 'driver' checkbox) if you already have it.

To ensure the cuda is installed, run:<br>
$ nvcc --version<br>

It should print information and version of CUDA.<br>
If no nvcc is found, try adding the CUDA bin path to the PATH variable:<br>
$ export PATH=/usr/local/cuda/bin:$PATH

install build-essential:<br>
$ sudo apt-get install build-essential

Check the gcc version:<br>
$ gcc --version

if the version is less than 9, install gcc 9:

$ sudo apt-get install software-properties-common<br>
$ sudo add-apt-repository ppa:jonathonf/gcc<br>
$ sudo apt-get update<br>
$ sudo apt-get install gcc-9<br>
$ sudo apt-get install g++-9<br>
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 10<br>
$ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 10

install libssl:<br>
$ sudo apt-get install libssl-dev<br>
for the client-server version, install boost:<br>
$ sudo apt-get install libboost-all-dev

You will need Boost version at least 1.71. If apt-get does not intall at least 1.71, build Boost from source:
$ wget https://archives.boost.io/release/1.71.0/source/boost_1_71_0.tar.gz<br>
$ tar -xzvf boost_1_71_0.tar.gz<br>
$ cd boost_1_71_0<br>
$ ./bootstrap.sh --prefix=/usr && ./b2 stage threading=multi link=static<br>
$ sudo ./b2 install threading=multi link=static<br>
$ sudo ln -svf detail/sha1.hpp /usr/include/boost/uuid/sha1.hpp

install cmake from here: https://cmake.org/download/ choose Binary distributions, if that does not work - build from source<br>
$ wget https://github.com/Kitware/CMake/releases/download/v3.28.0/cmake-3.28.0-linux-x86_64.tar.gz<br>
$ tar -xzvf cmake-3.28.0-linux-x86_64.tar.gz

unpack the bip39scan source, let's say bip39scan/<br>
make an empty build directory, and run cmake in it e.g.<br>
$ mkdir bip39scan-build<br>
$ cd bip39scan-build

On first make, it will generate precomp.bin file, which may take quite some time. <br>
If you already have the precomp.bin, copy it to the build directory and comment this line in the ../bip39scan/CMakeLists.txt: add_dependencies(bip39scan precomp-bin) like this:<br>
#add_dependencies(bip39scan precomp-bin)

Save CMakeLists.txt and run cmake:
$ ../cmake-3.28.0-linux-x86_64/bin/cmake ../bip39scan<br>

where ../bip39scan is the source code directory<br>
make the project<br>
$ make bip39scan
