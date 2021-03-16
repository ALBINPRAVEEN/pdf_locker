# pdflocker

## About lockpdf
lockpdf is a single-purpose tool that wraps PyPDF2 to encrypt pdfs quickly. It will also create moderately safe passwords for said files, so you don't have to.

## Disclaimer
Encrypting PDFs is, at best, protection against the prying eyes of an opportunistic attacker. Do not rely on lockpdf or password-protected PDFs in general for critical information.

### Installation
```
git clone https://github.com/keralahacker/pdflocker.git
```
### Dependencies
lockpdf uses the PyPDF2 module.

The specific versions can be found in the requirements file. The modules can be installed manually or using said file:

### Linux/OSX:
```
sudo pip3 install -r requirements.txt
```
### Windows:
```
python.exe -m pip install -r requirements.txt
```

#### Usage
Usage is generally explained through the --help output.
```
usage: lockpdf.py [-h] -i SRC_PDF [-o DST_PDF] [-p PASSWORD] [--version]
```
Pdflocker 

optional arguments:
```
  -h, --help   show this help message and exit
  -i SRC_PDF   Input file
  -o DST_PDF   Output file (default: [Original]_encrypted.pdf)
  -p PASSWORD  Specify a custom password (default: random alphanum, l=32)
  --version    show program's version number and exit
```
