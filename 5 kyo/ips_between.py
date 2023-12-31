"""
Implement a function that receives two IPv4 addresses, and returns the number of 
addresses between them (including the first one, excluding the last one).


Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246

"""

def ips_between(start, end):
    startArr = start.split(".")
    endArr = end.split(".")
    startBin = ""
    endBin = ""
    # Convert IP address into a 32-bit binary number
    for i in range(len(startArr)):
        startBin = startBin + format(int(startArr[i]), '08b')
        endBin = endBin + format(int(endArr[i]), '08b')
    startBin = "0b" + startBin
    endBin = "0b" + endBin
    return(int(endBin , 2)-int(startBin , 2))