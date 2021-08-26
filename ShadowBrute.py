# A simple bruteforce tool to crack UNIX passwords using wordlists
# calfcrusher@inventati.org
# Usage: ./ShadowBrute.py HASHFILE WORDLIST
# insert many hash as you want in HASHFILE once one per line, same in wordlist file

import crypt
import sys
import time
import pyfiglet


def crackpass(list, hashstring, salted):
    """Bruteforce function"""

    try:
        wlist = open(list, 'r')
    except:
        print("Error: Unable to access wordlist file")
        exit(0)

    # Check if salt is present
    if salted:
        for word in wlist:
            word = word.strip('\n')
            original_hash = str(salted + "$" + hashstring).strip('\n')
            crypted_word = crypt.crypt(word, salt=salted)
            if original_hash == crypted_word.strip('\n'):
                print("[+] HASH: " + salted + hashstring)
                print("[+] CRACKED: " + word + "\n")
                break
    else:
        for word in wlist:
            word = word.strip('\n')
            crypted_word = crypt.crypt(word)
            if hashstring == crypted_word.strip('\n'):
                print("[+] HASH: " + hashstring)
                print("[+] CRACKED: " + word + "\n")
                break

    wlist.close()


def main():
    """Main function of tool"""

    ascii_banner = pyfiglet.figlet_format("ShadowBrute")
    print(ascii_banner)
    print("calfcrusher@inventati.org | For educational use only.")
    print("*****************************************************\n")

    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Usage: ./ShadowBrute.py hashes.txt wordlist.txt")
        exit(0)
    else:
        filehash = sys.argv[1]
        wordlist = sys.argv[2]
        try:
            fhash = open(filehash, 'r')
        except:
            print("Error: Unable to access hash file")
            exit(0)


    # Reading lines from hash file
    for line in fhash.readlines():
        # Check if our hash contains salt or not
        if str(line).count('$') == 3:
            hash_identifier = str(line.split('$')[1])
            # We construct the salt in this way: $1$saltstring
            salt = str("$" + hash_identifier + "$" + (line.split('$')[2]))
            hash = str(line.split ('$')[3])
        elif str(fhash).count('$') == 2:
            hash = line.split('$')[2]
            salt = 0
        else:
            print("Error: Unrecognized hash in " + filehash)
            exit(0)

        crackpass(wordlist, hash, salt)

    fhash.close()


if __name__ == "__main__":
    start = time.time()
    main()
    print('It took {0:0.1f} seconds'.format(time.time() - start))
