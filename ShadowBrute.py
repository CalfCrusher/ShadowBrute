# A simple bruteforce cracker for UNIX passwords
# calfcrusher@inventati.org
#
# Usage: python ShadowBrute.py HASHFILE WORDLIST
# python ShadowBrute.py hashes.txt wordlist.txt

import crypt
import sys
import os


def crackpass(cryptPass):
    salt = cryptPass[0:2]

    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: " + word + "\n"
            return
    print "[-] Password Not Found.\n"
    return

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print "Usage: python ShadowBrute.py hashes.txt wordlist.txt"
        exit(0)
    else:
        filehash = sys.argv[1]
        wordlist = sys.argv[2]
        try:
            fhash = open(filehash, 'r')
            wlist = open(wordlist, 'r')
        except:
            print "Error: File does not appear to exist"
            exit(0)

    for line in fhash.readlines():
        print line
        #user = line.split(':')[0]
        #cryptPass = line.split(':')[1].strip(' ')
        #print "[*] Cracking Password For: " + user
        #testPass(crackpass())


if __name__ == "__main__":
    main()
