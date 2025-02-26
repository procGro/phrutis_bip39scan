# bip39scan - CUDA only
Multigpu program brute force mnemonic phrases <br>
Supports all patches, BTC, DOGE, LITE, dash, BTC Cash, addresses and ETH tokens.<br>
Automatically detects the coin type based on the given patch. You can specify the type manually.<br> 
RTX speed 4090 = 160,000,000 phrases per sec (24 words)<br>
RTX speed 4090 = 11,000,000 phrases per sec. (12 words)<br>
By default, all CUDA cards work. You can specify the necessary -d 0,1,2,3,5<br>
You can use your own list of words from a text file for searching.<br>
Only words from the 2048 mnemonic words are supported.<br>
Words in the file must be on a new line.<br>
To add a specified list, use ```-w words.txt```<br>
[Brute force program (win + linux)](https://github.com/phrutis/bip39scan#bip39scanexe---windows-cuda-only) + [program for reading mnemonics from a file (win + linux)](https://github.com/phrutis/bip39scan#bip39scan-linux-only) +<br>[source code bip39scan client](https://github.com/phrutis/bip39scan#source-code-of-bip39scan) + [Bonus](https://github.com/phrutis/bip39scan#bonus-only-for-linux) = $500<br><br>
Buy the programs https://t.me/cuda8<br>
If you have any questions, please write @phrutis

For the test, you can generate a phrase on the website https://iancoleman.io/bip39/<br>
Add the address to the address database. Using the same patch you will find

## Modes:
### Sequential search Windows<br>
Replace unknown words with *<br>
```bip39scan.exe --save Found.txt -a eth0x.txt -p m/44'/60'/0'/0/0-3 cement income * bounce suspect * * jungle cheese ranch neutral *```<br><br>
![1](https://github.com/user-attachments/assets/a448a078-7340-4b86-af06-766db9897238)

### Random mode:<br>
Replace unknown words with *<br>
```bip39scan.exe --save Found.txt -a eth0x.txt -p m/44'/60'/0'/0/0-3 -r * * * * * * * * * * * *```<br><br>
![random](https://github.com/user-attachments/assets/f9611d71-33fe-4abc-87a8-e52b83102147)


If you have address bases of 1-12 GB, it is better to convert them to binary format.<br>
Launch with a text address base of 10 GB = 10 minutes, with a binary base 3-5 seconds.<br>
We create binary databases, example below<br>

BTC<br>
```bip39scan.exe --save Found.txt -a btc1.txt --save-bin btc1.bin -p m/44'/0'/0'/0/0-5```<br>
```bip39scan.exe --save Found.txt -a btc3.txt --save-bin btc3.bin -p m/49'/0'/0'/0/0-5```<br>
```bip39scan.exe --save Found.txt -a btc-bc.txt --save-bin btc-bc.bin-p m/84'/0'/0'/0/0-5```<br>

ETH and tokens<br>
```bip39scan.exe --save Found.txt -a eth_addresses.txt --save-bin eth.bin -t ethereum -p m/44'/60'/0'/0/0-5  -r * * * * * *```

Quick start with binary base:<br>
```bip39scan.exe --save Found.txt -a btc1.bin -t P2PKH -p m/0/0-10 -r * * * * * *```<br>
```bip39scan.exe --save Found.txt -a btc1.bin -t P2PKH -p m/44'/0'/0'/0/0-9  -r * * * * * *```<br>
```bip39scan.exe --save Found.txt -a btc3.bin -t P2SH -p m/49'/0'/0'/0-1/0-9  -r * * * * * *```<br>
```bip39scan.exe --save Found.txt -a btc-bc.bin -t Bech32 -p m/84'/0'/0'/0-1/0-9  -r * * * * * *```<br>
```bip39scan.exe --save FoundETH.txt -a eth.bin -t ethereum -p m/44'/60'/0'/0/0-9  -r * * * * * *```<br>


It is better to be on the safe side, use the instructions below or turn off the Internet during the search.

1. Press the key combination "Win+R" and enter the command "firewall.cpl".
2. Go to the "Advanced settings" section and select "Outgoing connection rules".
3. Click on the "Create rule" button, select the "For program" option and specify its path.
4. Select the checkbox next to "Block connection".
5. Click "Next", specify "Name" and click "Done".

precomp.bin - this is the acceleration table<br>

![Image](https://github.com/user-attachments/assets/ee6c4bac-2fc2-452e-b9ab-b85cdfe64701)

### Sequential search linux
Works on RTX 3070, other cards may have problems.<br>
Try installing nvidia/cuda:12.1.0-devel-ubuntu20.04<br>
```--dict words.txt``` - Specify the desired mnemonic list of words on a new line.<br>

```chmod +x bip39scan```<br>

```./bip39scan --dict 'words.txt' -a btc1.txt -p m/44\'/0\'/0\'/0/0-5 --save Found.txt \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt*```<br>

If you know part of the phrase, please indicate it like this<br>
```./bip39scan --dict 'words.txt' -a btc1.txt -p m/44\'/0\'/0\'/0/0-5 --save Found.txt chat summer \*words.txt* gap injury \*words.txt* snap note \*words.txt* \*words.txt* \*words.txt*```<br>
![bip39](https://github.com/user-attachments/assets/9e0437f6-82ac-474b-afd1-5dd7b744b6c6)<br>

### Random search linux

```./bip39scan --dict 'words.txt' -a btc1.txt -p m/44\'/0\'/0\'/0/0-5 --save Found.txt \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* \*words.txt* -r```

If you know part of the phrase, please indicate it like this<br>

```./bip39scan --dict 'words.txt' -a btc1.txt -p m/44\'/0\'/0\'/0/0-5 --save Found.txt chat summer denial gap injury equip snap note \*words.txt* \*words.txt* \*words.txt* \*words.txt* -r```<br>
![Image](https://github.com/user-attachments/assets/f11bd02a-cace-43cf-b992-f94d0ae6bbe1)


### Speed ​​example RTX 3070 Ti (24 words) - 43 million phrases per second<br>
![Image](https://github.com/user-attachments/assets/212ae251-7cf6-4e20-a057-c5fc6c22ac3c)

<hr>

# bip39scan2 linux (ubuntu)
The program reads mnemonic phrases from a text file on the GPU (Only CUDA )<br>
The program also reads all: PASSWORDS, numbers, words from a file. There are many finds on them.<br>
Supports all patches, addresses from different coins and tokens.<br>
Automatically detects the coin type based on the given patch. You can specify the type manually.<br>
Multi GPU program. RTX speed 4090 = 500k phrases per sec.<br>
By default, all CUDA cards work. You can specify the necessary -d 0,1,2,3,5<br>
Supports phrase dictionaries up to 32 TB.<br>
Buy the programs https://t.me/cuda8

<b>Launch examples:</b>
<br>
```chmod +x bip39scan2```<br><br>
<b>BTC:</b><br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc1.txt -p m/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc1.txt -p m/44\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc3.txt -p m/49\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc-bc.txt -p m/84\'/0\'/0\'/0-1/0-10```<br><br>
<b>ETH:</b><br>
```./bip39scan -m seeds.txt --save Found.txt -a eth_addresses.txt -p m/44\'/60\'/0\'/0-1/0-20```<br><br>
<b>Others coins:</b><br>
```./bip39scan2 -m seeds.txt --save FoundB-cash.txt -a btc-cash.txt -p m/44\'/145\'/0\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save FoundB-cash.txt -a btc-cash.txt -p m/44\'/0\'/0\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save FoundDash.txt -a dash.txt -p m/44\'/5\'/0\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save FoundDoge.txt -a doge.txt -p m/44\'/3\'/0\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save FoundLITE.txt -a lite-L.txt -p m/44\'/2\'/0\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save FoundLITE.txt -a lite-M.txt -p m/49\'/2\'/0\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save FoundLITE.txt -a lie-ltc1.txt -p m/84\'/2\'/0\'/0-1/0-20```<br><br>
<b>ETH Tokens:</b>  ARB, AVAX, BASE, BNB, CRO, ETC, ETH, FTM, GETH, GNO, MATIC, OP, opBNB, zkEVM<br>
```./bip39scan2 -m seeds.txt --save TFoundETH.txt -a BAZA/t6.bin -t ethereum -p m/44\'/60\'/160720\'/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETH.txt -a BAZA/t6.bin -t ethereum -p m/44\'/137\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHNIM-Nimiq.txt -a BAZA/t6.bin -t ethereum -p m/44\'/242\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHAION.txt -a BAZA/t6.bin -t ethereum -p m/44\'/425\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHTHETA.txt -a BAZA/t6.bin -t ethereum -p m/44\'/500\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHSmartCL.txt -a BAZA/t6.bin -t ethereum -p m/44\'/714\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHVET.txt -a BAZA/t6.bin -t ethereum -p m/44\'/818\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHCLO.txt -a BAZA/t6.bin -t ethereum -p m/44\'/820\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHTOMO.txt -a BAZA/t6.bin -t ethereum -p m/44\'/889\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHTT.txt -a BAZA/t6.bin -t ethereum -p m/44\'/1001\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHWAN.txt -a BAZA/t6.bin -t ethereum -p m/44\'/5718350\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHPOA.txt -a BAZA/t6.bin -t ethereum -p m/44\'/178\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHGO.txt -a BAZA/t6.bin -t ethereum -p m/44\'/6060\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHCELO.txt -a BAZA/t6.bin -t ethereum -p m/44\'/52752\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHPOLYGON.txt -a BAZA/t6.bin -t ethereum -p m/44\'/966\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHHARMONY.txt -a BAZA/t6.bin -t ethereum -p m/44\'/1023\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHKLAY.txt -a BAZA/t6.bin -t ethereum -p m/44\'/8217\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHTRON.txt -a BAZA/t6.bin -t ethereum -p m/44\'/195\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHEGLD.txt -a BAZA/t6.bin -t ethereum -p m/44\'/508\'/0\'/0\'/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHADA.txt -a BAZA/t6.bin -t ethereum -p m/1852\'/1815\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHFLOW.txt -a BAZA/t6.bin -t ethereum -p m/44\'/539\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHNEO.txt -a BAZA/t6.bin -t ethereum -p m/44\'/888\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHSOL.txt -a BAZA/t6.bin -t ethereum -p m/44\'/501'/0\'/0\'/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHXDC.txt -a BAZA/t6.bin -t ethereum -p m/44\'/550\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHXLM.txt -a BAZA/t6.bin -t ethereum -p m/44\'/148\'/0\'/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHXRP.txt -a BAZA/t6.bin -t ethereum -p m/44\'/144\'/0\'/0/0-20```<br>
```./bip39scan2 -m seeds.txt --save TFoundETHBNB.txt -a BAZA/t6.bin -t ethereum -p m/44\'/714\'/0\'/0/0-20```<br>

<b>It is important to put \ before ' in the patch!!!</b><br>
If you have address bases of 1-12 GB, it is better to convert them to binary format.<br>
Launch with a text address base of 10 GB = 10 minutes, with a binary base 3-5 seconds.<br>
We create binary databases, example below<br>

BTC<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc1.txt --save-bin btc1.bin -p m/44\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc3.txt --save-bin btc3.bin -p m/49\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc-bc.txt --save-bin btc-bc.bin-p m/84\'/0\'/0\'/0-1/0-10```<br><br>
ETH and tokens<br>
```./bip39scan -m seeds.txt --save Found.txt -a eth_addresses.txt --save-bin eth.bin -t ethereum -p m/44\'/60\'/0\'/0-1/0-20```<br><br>

Quick start with binary base:<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a btc1.bin -t P2PKH -p m/0-1/0-20```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a BAZA/btc1.bin -t P2PKH -p m/44\'/0\'/0\'/0-1/0-10<br>```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a BAZA/btc3.bin -t P2SH -p m/49\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan2 -m seeds.txt --save Found.txt -a BAZA/btc-bc.bin -t Bech32 -p m/84\'/0\'/0\'/0-1/0-10```<br>
```./bip39scan2 -m seeds.txt --save FoundETH.txt -a eth.bin -t ethereum -p m/44\'/60\'/0\'/0-20```<br>


The program works very fast, it takes a lot of time to launch each command.<br>
I recommend first creating binary databases, then making a list of launch commands in a file.<br>
This will be faster and more convenient.<br>
Place the file next to the program.<br>
```chmod +x START.sh```<br>
See the example in the file START.sh<br>
```./START.sh```

### bip39scan2.exe Windows
```bip39scan2.exe -m seeds.txt --save Found.txt -a btc1.txt -p m/0-1/0-20```<br>
Launch arguments as for Linux above. Launch arguments as for Linux above. Get help ```bip39scan2.exe -h```<br>
Works on RTX 20xx, 30xx series cards.<br>
On RTX 4090, 5090 cards it does not work for everyone!
<hr>

# BONUS only for Linux (ubuntu)
Attack on vulnerable random number generator (RNG)
Program only for win bip39scan-rng.exe
Ex. ```bip39scan-rng.exe --rng --save Found.txt -p m/44'/0'/0'/0/0-9 -a btc1.txt```

Vulnerablity in libbitcoin explorer library - generator phrases and entropy<br>
The developers have removed the utility everywhere, it is impossible to compile from the source code.<br>
It is very difficult to find a vulnerable version 3.2.<br>
32-bit vulnerability is 4294967295 mnemonic phrases.<br>
9 languages, 12, 15, 18, 21, 24 words. 193,273,528,275 is tens of TB.<br>
The vulnerability affected not only BTC, ETH, but also tokens, other coins.<br>
Many still don't know and use the old library to generate phrases and keys<br>

Launch example.<br>
```./bx-linux-x64-qrcode_3_2 seed -b 256 | ./bx-linux-x64-qrcode_3_2 mnemonic-new```

```./bx-linux-x64-qrcode_3_2 seed -b 256 | ./bx-linux-x64-qrcode_3_2 mnemonic-new -l es```

```./bx-linux-x64-qrcode_3_2 seed -b 128 | ./bx-linux-x64-qrcode_3_2 mnemonic-new -l ja```

Languages<br>
--language<br>
en (default)<br>
-l es<br>
-l fr<br>
-l it<br>
-l ja<br>
-l cs<br>
-l ru<br>
-l uk<br>
-l zh_Hans<br>
-l zh_Hant<br>

(Phrase length 12, 15, 18, 21, 24)<br>
-b 128<br>
-b 160<br>
-b 192<br>
-b 224<br>
-b 256<br>

A multi-cpu script is sent to the explorer that generates a stream of phrases into a text file.<br>
It is also possible to generate vulnerable private keys from BTC, ETH and other coins.<br>
```./bx-linux-x64-qrcode_3_2 seed -b 256 >> Out.txt```
<hr>

# Source code of bip39scan

Source code of the program bip39scan<br>
For compilation you need knowledge of C++, CUDA!<br>
It is necessary to remove the client-server link and other.<br>
How to build:<br>

## Building on Ubuntu:

Below is detailed instruction with bash commands required to build bip39scan. <br>
The symbol '$' denotes command prompt.<br> 
If your prompt is shown as '#' on your terminal, skip 'sudo'. <br>
For example, instead of

 $ sudo sh cuda_12.0.1_525.85.12_linux.run
 
you should run

 ```# sh cuda_12.0.1_525.85.12_linux.run```

Let's start.

1. install CUDA. Download the linux version from the NVIDIA website and run. <br>Open https://developer.nvidia.com/cuda-12-0-1-download-archive?target_os=Linux<br>
in your browser and choose your system. The following is valid for Ubuntu 18.04.

 $ wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda_12.0.1_525.85.12_linux.run<br>
 $ sudo sh cuda_12.0.1_525.85.12_linux.run
 
Skip the driver installation (deselect the 'driver' checkbox) if you already have it.

To ensure the cuda is installed, run:<br>
 $ nvcc --version<br>
It should print information and version of CUDA.<br>
If no nvcc is found, try adding the CUDA bin path to the PATH variable:<br>
 $ export PATH=/usr/local/cuda/bin:$PATH<br>
2. install  build-essential:<br>
 $ sudo apt-get install build-essential<br>
 
 Check the gcc version:<br>
 $ gcc --version
 
 if the version is less than 9, install gcc 9:
 
 $ sudo apt-get install software-properties-common<br>
 $ sudo add-apt-repository ppa:jonathonf/gcc<br>
 $ sudo apt-get update<br>
 $ sudo apt-get install gcc-9<br>
 $ sudo apt-get install g++-9<br>
 $ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 10<br>
 $ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 10<br>

3. install libssl: <br>
 $ sudo apt-get install libssl-dev<br>
4. for the client-server version, install boost:<br>
 $ sudo apt-get install libboost-all-dev<br>
 
You will need Boost version at least 1.71. If apt-get does not intall at least 1.71, build Boost from source:

 $ wget https://boostorg.jfrog.io/artifactory/main/release/1.71.0/source/boost_1_71_0.tar.gz<br>
 $ tar -xzvf boost_1_71_0.tar.gz<br>
 $ cd boost_1_71_0<br>
 $ ./bootstrap.sh --prefix=/usr && ./b2 stage threading=multi link=static<br>
 $ sudo ./b2 install threading=multi link=static<br>
 $ sudo ln -svf detail/sha1.hpp /usr/include/boost/uuid/sha1.hpp<br>

5. install cmake from here: https://cmake.org/download/ choose Binary distributions, if that does not work - build from source<br>
 $ wget https://github.com/Kitware/CMake/releases/download/v3.28.0/cmake-3.28.0-linux-x86_64.tar.gz<br>
 $ tar -xzvf cmake-3.28.0-linux-x86_64.tar.gz<br>
6. unpack the bip39scan source, let's say bip39scan/<br>
7. make an empty build directory, and run cmake in it e.g.<br>
 $ mkdir bip39scan-build<br>
 $ cd bip39scan-build<br>
 
On first make, it will generate precomp.bin file, which may take quite some time. If you 
already have the precomp.bin, copy it to the build directory and comment this line in the 
../bip39scan/CMakeLists.txt: add_dependencies(bip39scan precomp-bin) like this:<br>

#add_dependencies(bip39scan precomp-bin)

Save CMakeLists.txt and run cmake:

 $ ../cmake-3.28.0-linux-x86_64/bin/cmake ../bip39scan<br>
where ../bip39scan is the source code directory<br>
8. make the project<br>
 $ make bip39scan


