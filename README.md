# bip39scan - New reliase v4.0.1 (22/07/2025) - $300

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

The program is sold with the source code!<br>
The kit includes ready-made programs for Windows x64 and Linux (Ubuntu and hiveos)<br>
To purchase, write to telegram ```@phrutis``` or buy from a bot in a group t.me/cuda8

# Modes:
## Sequential search words
```bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 uncover figure script * obscure waste metal quit depend bachelor trust erupt * impose brave leave number rapid oak wealth reopen * noodle tragic```<br>
In the phrase, 3 missing words in different positions are replaced by * (test address 14aZB9i8NFiXpeGbS3g7vLArhL7EbNBSWS)

[![Image](https://github.com/user-attachments/assets/0a4e85ae-166f-41ae-b406-16c736e38d17)](https://github.com/user-attachments/assets/e8d4535c-ea78-410f-8ec9-2608847ce975)


You can use your own list of words from a text file for searching.<br>
Only words from the [2048 mnemonic words](https://github.com/phrutis/bip39scan/blob/main/bip39.txt) are supported.<br>
Words in the file must be on a new line.<br>
To add a specified list, use ```-w words.txt```<br>
Replace unknown words with *<br>

## Random mode:
```bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 -w mywordlist.txt -r uncover figure script * obscure waste * quit depend bachelor trust erupt * impose brave leave number rapid oak * reopen * noodle tragic```

https://github.com/user-attachments/assets/2d9d24c7-8844-4de4-9e5d-7eba976d021e

Replace unknown words with *<br>
For full random, add only stars<br>



## Linux (Ubuntu, hiveos)
The commands are the same as for Windows.<br>
You need to add in patch \ before '

```chmod +x bip39scan```<br>
ex. ``` ./bip39scan -a eth.bin -t ethereum --bloom 2048M --save Found.txt -p m/44\'/60\'/0\'/0/0-9 ...```

