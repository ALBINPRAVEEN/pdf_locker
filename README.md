# pdflocker

## About lockpdf
lockpdf is a single-purpose tool that wraps PyPDF2 to encrypt pdfs quickly. It will also create moderately safe passwords for said files, so you don't have to.

## Disclaimer
Encrypting PDFs is, at best, protection against the prying eyes of an opportunistic attacker. Do not rely on lockpdf or password-protected PDFs in general for critical information.

### Installation
```
git clone https://github.com/ALBINPRAVEEN/pdf_locker.git
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

## CONTACT ME:
<p align="center">
<a href="https://www.instagram.com/i_am_albin_praveen/"><img title="Instagram" src="https://img.shields.io/badge/i_am_albin_praveen-black?style=for-the-badge&logo=instagram"></a>
<a href="mailto:albinpraveen135790@gmail.com"><img title="MAIL" src="https://img.shields.io/badge/ALBY-black?style=for-the-badge&logo=Gmail"></a>
</p>
<p align="center">
<a href="https://t.me/i_am_albin_praveen"><img title="Telegram" src="https://img.shields.io/badge/i_am_albin_praveen-black?style=for-the-badge&logo=telegram"></a>
<a href="https://wa.me/+917025743032"><img title="ALBY" src="https://img.shields.io/badge/ALBY-black?style=for-the-badge&logo=Whatsapp"></a>
</p>
<p align="center">
<a href="https://github.com/ALBINPRAVEEN"><img title="Github" src="https://img.shields.io/badge/ALBIN PRAVEEN-black?style=for-the-badge&logo=github"></a>
 </p>
