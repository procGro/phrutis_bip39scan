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
To purchase, write to telegram ```@phrutis``` or buy from a bot in a group https://t.me/cuda8

# Modes:
## Sequential search words
```
bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 uncover figure script * obscure waste metal quit depend bachelor trust erupt * impose brave leave number rapid oak wealth reopen * noodle tragic
```
In the phrase, 3 missing words in different positions are replaced by * (test address 14aZB9i8NFiXpeGbS3g7vLArhL7EbNBSWS)

[![Image](https://github.com/user-attachments/assets/0a4e85ae-166f-41ae-b406-16c736e38d17)](https://github.com/user-attachments/assets/e8d4535c-ea78-410f-8ec9-2608847ce975)

```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M -e stdin --save Found.txt -p m/44'/0'/0'/0/0-9 cause ensure shield option monkey infant tray okay remember * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M -e stdin --save Found.txt -p m/49'/0'/0'/0/0-9 carpet * recycle force since * update glare seminar * worth answer
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M -e stdin --save Found.txt -p m/84'/0'/0'/0/0-9 * ostrich * kitten * unit glow tortoise world crop kit curve
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M -e stdin --save Found.txt -p m/44'/60'/0'/0/0-9 right elevator dust radio please prison cup omit require also decorate sock
```
You can use your own list of words from a text file for searching.<br>
Only words from the [2048 mnemonic words](https://github.com/phrutis/bip39scan/blob/main/bip39.txt) are supported.<br>
Words in the file must be on a new line.<br>
To add a specified list, use ```-w words.txt```<br>
Replace unknown words with *<br>

## Random mode:
```
bip39scan.exe --save Found.txt -a btc1.txt -t P2PKH -p m/44'/0'/0'/0/0-9 -w mywordlist.txt -r uncover figure script * obscure waste * quit depend bachelor trust erupt * impose brave leave number rapid oak * reopen * noodle tragic
```
https://github.com/user-attachments/assets/2d9d24c7-8844-4de4-9e5d-7eba976d021e

**Replace unknown words with** **\***<br>
**Standard random 2048 words in positions with** **\***<br>
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M -e stdin --save Found.txt -p m/44'/0'/0'/0/0-9 -r cause * shield option monkey infant tray okay remember * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M -e stdin --save Found.txt -p m/49'/0'/0'/0/0-9 -r carpet * recycle * since * update glare seminar * worth answer
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M -e stdin --save Found.txt -p m/84'/0'/0'/0/0-9 -r * ostrich * * * unit glow tortoise world crop kit curve
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M -e stdin --save Found.txt -p m/44'/60'/0'/0/0-9 -r * * * * * prison cup omit require also decorate sock
```


**Random using your list of mnemonic words from the file words.txt**<br>
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M -e stdin --save Found.txt -p m/44'/0'/0'/0/0-9 -w words.txt -r cause * shield option monkey infant tray okay remember * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M -e stdin --save Found.txt -p m/49'/0'/0'/0/0-9 -w words.txt -r carpet * recycle * since * update glare seminar * worth answer
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M -e stdin --save Found.txt -p m/84'/0'/0'/0/0-9 -w words.txt -r * ostrich * * * unit glow tortoise world crop kit curve
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M -e stdin --save Found.txt -p m/44'/60'/0'/0/0-9 -w words.txt -r * * * * * prison cup omit require also decorate sock
```

**For full random, add only stars**<br>
```
bip39scan.exe -a allbtc1.bin -t P2PKH --bloom 2048M -e stdin --save Found.txt -p m/44'/0'/0'/0/0-9 -r * * * * * * * * * * * *
```
```
bip39scan.exe -a allbtc3.bin -t P2SH --bloom 2048M -e stdin --save Found.txt -p m/49'/0'/0'/0/0-9 -r * * * * * * * * * * * *
```
```
bip39scan.exe -a allbc.bin -t bech32 --bloom 2048M -e stdin --save Found.txt -p m/84'/0'/0'/0/0-9 -r * * * * * * * * * * * *
```
```
bip39scan.exe -a alleth.bin -t ethereum --bloom 4096M -e stdin --save Found.txt -p m/44'/60'/0'/0/0-9 -r * * * * * * * * * * * *
```







## Linux (Ubuntu, hiveos)
The commands are the same as for Windows.<br>
You need to add in patch \ before '

```
chmod +x bip39scan
```
```./bip39scan -a eth.bin -t ethereum --bloom 2048M --save Found.txt -p m/44\'/60\'/0\'/0/0-9 ...```

