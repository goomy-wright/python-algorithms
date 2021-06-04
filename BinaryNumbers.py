def binaryToDecimal(binary: str):
    return int(binary,2)

def decimalToBinary(n):
    return bin(n).replace("0b", "")
