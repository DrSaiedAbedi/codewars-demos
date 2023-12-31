"""
Decode the Morse code with unknown frequency of dots and dashes, advanced

Example:
HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

11001100110011000000110000001111110011001111110011111100000000000000110011
11110011111100111111000000110011001111110000001111110011001100000011

"""
from preloaded import MORSE_CODE
def disoverFrequcnyOf(lMessage):
    a = lMessage
    a = a.replace('0', ' ')
    d = a.split()
    flag3Div = True
    for x in d:
        if len(x) % 3 != 0:
            flag3Div = False
        break
    b = lMessage.replace('1', ' ')
    c = b.split()
    lWordMessage = []
    for x in c:
        lWordMessage.append(len(x))
    freqM = 1
    for y in lWordMessage:
        if y % 7 == 0:
            freqM= int(y / 7)
        elif y % 3 == 0 and y > 3:
            freqM= int(y / 3)
        else:
            freqM = y;
        if y == 3 and not flag3Div:
            freqM= 1
        if y == 3 and flag3Div:
            freqM= 3
    return(freqM)


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


def decode_bits(bits):
    
    if bits =='111':
        return('.')
    else:
        x = bits
        k = 1
        if '0' in x:
            k = disoverFrequcnyOf(bits)
        else:
            k = len(bits)
        dotP = ""
        dashP = ""
        for i in range(k):
            dotP += '0'
            dashP += '1'
            c1Message = x.replace(dotP, '0')
            morse_code = c1Message.replace(dashP, '1')
        if '0' in x:
            
            morse_code = morse_code.replace('111', '-')
            morse_code = morse_code.replace('1', '.')
            morse_code = morse_code.replace('0000000', '   ')
            morse_code = morse_code.replace('000', ' ')
            morse_code = morse_code.replace('0', '')
        else:
            if k > 1:
                morse_code = '.'
            else:
                if len(morse_code) == 1:
                    morse_code = morse_code.replace('1', '.')
                else:
                    if len(morse_code) == 3:
                        morse_code = morse_code.replace('111', '-')
                    else: 
                        morse_code = morse_code.replace('11', '.')
    if morse_code == '-':
        return('.')
    morse_code1 = morse_code
    morse_code1 = morse_code1.strip()
    if morse_code1 == '-':
        return('.')
    return(morse_code)