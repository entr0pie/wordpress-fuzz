#!/bin/python3

import requests
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--host", type=str, required=True)
parser.add_argument("--wordlist", type=str, required=False)

args = parser.parse_args()

print("")

if not args.wordlist:
    print("* Using default wordlist (https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/CMS/wordpress.fuzz.txt)")
    WORDLIST = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/CMS/wordpress.fuzz.txt").text
    content = WORDLIST.split('\n')

else:
    content = open(args.wordlist, 'r').read()


HOST = args.host

output = open("out.txt", "w")

print("* Starting Wordpress-Fuzz, saving on out.txt ...\n")

for page in content:
    try:
        page = page.strip()
    
        text = page

        response = requests.get(HOST + page)
        print(page, end=' ')

        if response.status_code == 200:
            print("[\u001b[32mok\u001b[0m]")
            output.write(page + " " + "[ok]\n")

        elif response.status_code == 404:
            print("[\u001b[31m404\u001b[0m]")

        else:
            print(f"[\u001b[33m{response.status_code}\u001b[0m]")
            output.write(page + " " + f"[{response.status_code}]\n")
    
    except KeyboardInterrupt:
        print("\nSaved on out.txt, Bye!")
        exit(0)

print("\nSaved on out.txt, Bye!")
output.close()
