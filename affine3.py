# Affine Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import affineCipher, detectEnglish, cryptomath, sys

def breakAffine(cipher):
    print('\nCipher:')
    yp_file = open(cipher)
    i = 0
    for yp_line in yp_file:
        inp = yp_line.rstrip()
        print(inp)
        Affine(inp)
        i += 1
    yp_file.close()

def Affine(cipher):
    hackedMessage = hackAffine(cipher)
    if hackedMessage != None:
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
        print('\nPlaintext:')
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackAffine(message):
    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    # brute-force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print('\nKey: %s' % (key))
            response = 'D'

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# If affineHacker.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    print('\nCipher:')
    yp_file = open(sys.argv[1])
    i = 0
    for yp_line in yp_file:
        inp = yp_line.rstrip()
        print(inp)
        Affine(inp)
        i += 1
    yp_file.close()
