# Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

from transpositionDecrypt import *
from detectEnglish import *

import sys
def breakTranspose(cipher):
    yp_file = open(cipher)
    i = 0
    for yp_line in yp_file:
        inp = yp_line.rstrip()
        print('Ciphertext: ')
        print(inp)
        hackedMessage = hackTransposition(inp)
        i += 1
    yp_file.close()

def hackTransposition(message):
    # brute-force by looping through every possible key
    for key in range(1, len(message)):
        #print('X')
        decryptedText = decryptMessage(key, message)
        if isEnglish(decryptedText):
            # Check with user to see if the decrypted key has been found.
            print('\nKey:', key)
            print('\nPlaintext: ')
            response = 'Q'

            if response.strip().upper().startswith('Q'):
                print(decryptedText)
                break
    return None

if __name__ == '__main__':
    cipher2 = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
    yp_file = open(sys.argv[1])
    i = 0
    for yp_line in yp_file:
        inp = yp_line.rstrip()
        print(inp)
        print(len(inp))
        breakTranspose(inp)
        print(i)
        i += 1
    yp_file.close()
    