import argparse
import PyPDF2
import secrets
import string

def parse_args():
    parser = argparse.ArgumentParser(
        description='lockpdf',
        epilog='Ping me on Twitter @stfn42 if you get stuck.')

    parser.add_argument('-i', required = True,
                        help='Input file',
                        action="store", dest="src_pdf")

    parser.add_argument('-o',
                        help='Output file (default: [Original]_encrypted.pdf)',
                        action="store", dest="dst_pdf")

    parser.add_argument('-p',
                    help='Specify a custom password (default: random alphanum, l=32)',
                    action="store", dest="password")

    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()

def create_password(len):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(len))


def main():
    args = parse_args()
    if not args.password:
        args.password = create_password(32)

    if not args.dst_pdf:
        args.dst_pdf = args.src_pdf.split(".pdf")[0]+"_encrypted.pdf"

    pdf_w = PyPDF2.PdfFileWriter()
    with open(args.src_pdf, "rb") as infile:
        pdf_r = PyPDF2.PdfFileReader(infile)
        for i in range(pdf_r.numPages):
            pdf_w.addPage(pdf_r.getPage(i))
        pdf_w.encrypt(args.password, use_128bit=True)
        with open(args.dst_pdf, "wb") as outfile:
            pdf_w.write(outfile)

    print("Encypted %s with password: %s" % (args.dst_pdf, args.password))

main()
