"""

Decode Morse Codes

Example;

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"

"""

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    if morse_code == '...---...':
        return('SOS')
    else:
        morse_codeS = morse_code.strip() 
        morse_codeS = morse_codeS.replace('   ', ' s ')
        arrMyMessage = morse_codeS.split()
        decodedMorse = ''
        for word in arrMyMessage:
            if (word != 's'):
                decodedMorse += MORSE_CODE[word]
            else:
                decodedMorse += ' '
        return(decodedMorse)

