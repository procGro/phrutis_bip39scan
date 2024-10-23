# Bip39scan - $500
Multigpu program brute force mnemonic phrases<br>
Supports all patches, BTC, DOGE, LITE, dash, BTC Cash, addresses and ETH tokens.<br>
Automatically detects the coin type based on the given patch. You can specify the type manually.<br> 
RTX speed 4090 = 11,000,000 phrases per sec.<br>
By default, all CUDA cards work. You can specify the necessary -d 0,1,2,3,5<br>
The program was extracted from the docker by the miner from whom the installation was rented.<br>
The source code is missing, prohibit the program from accessing the Internet.<br>
If you do not know how to do this, simply disconnect the Internet.<br>
Buy the program https://t.me/cuda8<br>

### Sequential search<br>
Replace unknown words with *<br>
```bip39scan.exe --save Found.txt -a eth0x.txt -p m/44'/60'/0'/0/0-3 cement income * bounce suspect * * jungle cheese ranch neutral *```<br><br>
![1](https://github.com/user-attachments/assets/a448a078-7340-4b86-af06-766db9897238)

### Random mode:<br>
Replace unknown words with *<br>
```bip39scan.exe --save Found.txt -a eth0x.txt -p m/44'/60'/0'/0/0-3 -r * * * * * * * * * * * *```<br><br>
![random](https://github.com/user-attachments/assets/f9611d71-33fe-4abc-87a8-e52b83102147)

For linux (ubuntu) it is important to put \ before ' in the patch!!!<br>
Ex. ```./bip39scan --save Found.txt -a eth0x.txt -p m/44\'/60\'/0\'/0/0-3 -r * * * * * * * * * * * *```<br>

If you have address bases of 1-12 GB, it is better to convert them to binary format.<br>
Launch with a text address base of 10 GB = 10 minutes, with a binary base 3-5 seconds.<br>
We create binary databases, example below<br>

BTC<br>
```./bip39scan --save Found.txt -a btc1.txt --save-bin btc1.bin -p m/44\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan --save Found.txt -a btc3.txt --save-bin btc3.bin -p m/49\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan --save Found.txt -a btc-bc.txt --save-bin btc-bc.bin-p m/84\'/0\'/0\'/0-1/0-10```<br>

ETH and tokens<br>
```./bip39scan --save Found.txt -a eth_addresses.txt --save-bin eth.bin -t ethereum -p m/44\'/60\'/0\'/0-1/0-5  -r * * * * * *```

Quick start with binary base:<br>
```./bip39scan --save Found.txt -a btc1.bin -t P2PKH -p m/0-1/0-10 -r * * * * * *```<br>
```./bip39scan --save Found.txt -a btc1.bin -t P2PKH -p m/44\'/0\'/0\'/0-1/0-9  -r * * * * * *```<br>
```./bip39scan --save Found.txt -a btc3.bin -t P2SH -p m/49\'/0\'/0\'/0-1/0-9  -r * * * * * *```<br>
```./bip39scan --save Found.txt -a btc-bc.bin -t Bech32 -p m/84\'/0\'/0\'/0-1/0-9  -r * * * * * *```<br>
```./bip39scan --save FoundETH.txt -a eth.bin -t ethereum -p m/44\'/60\'/0\'/0/0-9  -r * * * * * *```<br>


It is better to be on the safe side, use the instructions below or turn off the Internet during the search.

1. Press the key combination "Win+R" and enter the command "firewall.cpl".
2. Go to the "Advanced settings" section and select "Outgoing connection rules".
3. Click on the "Create rule" button, select the "For program" option and specify its path.
4. Select the checkbox next to "Block connection".
5. Click "Next", specify "Name" and click "Done".


