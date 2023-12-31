"""
Write a hashtag generator: 
It must start with a hashtag (#). All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false. If the input or the
 result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

def generate_hashtag(s):
    arrayS = s.split()
    s1 = ""
    for x in arrayS:
        s2 = x.capitalize()
        s1 = s1 + s2
    s1 = "#" + s1 
    if s1 == "#":
        return(False)
    elif len(s1) != 0:
        if len(s1) <= 140:
            return(s1)
        else:
            return(False) 