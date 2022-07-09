#!/usr/bin/python3

import email
import argparse

parser = argparse.ArgumentParser("mime_to_html")
parser.add_argument("txt", help="Txt file with mime content", type=str)
args = parser.parse_args()
assert(args.txt.endswith(".txt"))
out_html_file = args.txt[:-4] + ".html"

f = open(args.txt).read()

def get_html_part(msg):
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            bytes = part.get_payload(decode=True)
            charset = part.get_content_charset('iso-8859-1')
            chars = bytes.decode(charset, 'replace')
            return chars

msg=email.message_from_string(f)
html=get_html_part(msg)

print(out_html_file)
out_file = open(out_html_file, "w+")
out_file.write(html)
out_file.close()
