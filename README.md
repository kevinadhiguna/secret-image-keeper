# Secret Image Keeper

Secret Image Keeper is an image encryptor/decryptor written in Python which will help you to secure your images.

## Demo
Here are how this app looks : <br><br>
<img src="https://raw.githubusercontent.com/kevinadhiguna/secret-image-keeper/master/demo/1.GUI.png" width="30%"></img> <br><br>
Input key that will be used to encrypt and decrypt an image :<br><br>
<img src="https://raw.githubusercontent.com/kevinadhiguna/secret-image-keeper/master/demo/2.input-Key.png" width="30%"></img> <br><br>
Choose an image :<br><br>
<img src="https://raw.githubusercontent.com/kevinadhiguna/secret-image-keeper/master/demo/3.open-file.png" width="60%"></img> <br><br>
This is how an encrypted image looks : <br><br>
<img src="https://raw.githubusercontent.com/kevinadhiguna/secret-image-keeper/master/demo/4.encrypted.png" width="80%"></img> <br><br>
To decrypt, input key that was used to encrypt the image :<br><br>
<img src="https://raw.githubusercontent.com/kevinadhiguna/secret-image-keeper/master/demo/2.input-Key.png" width="30%"></img> <br><br>
Voila! The image is now visible! <br><br>
<img src="https://raw.githubusercontent.com/kevinadhiguna/secret-image-keeper/master/demo/5.decrypted.png" width="80%"></img>

## Supported Image Extensions
Images with : <br />
1.`.png` <br />
2.`.jpg` <br />
3.`.jpeg` <br />
extensions can be encrypted and decrypted.

## How to Run :

1. Install dependencies : <br />
`pip install -r requirements.txt` (python2) <br />
`pip3 install -r requirements.txt` (python3) 
2. Run this program : <br />
`python keeper.py` (python2) <br />
`python3 keeper.py` (python3)
3. Enter your key to encrypt or decrypt.
4. Click `encrypt / decrypt` button, then choose an image to encrypt or decrypt.
5. Close the program and click the image you chose. Voila! The image is either encrypted or decrypted!
