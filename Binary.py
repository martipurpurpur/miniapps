def bin_in_int(bin):
    result = []
    print(bin)
    for i in range(len(bin)):
        decimal = 0
        for digit in bin[i]:
            decimal = decimal * 2 + int(digit)
        result.append(decimal)
    return result

def div_7(bin):
    int = bin_in_int(bin)
    bool = {}
    for i in range(len(int)):
        bool[int[i]] = int[i]%7 == 0
    return bool

bin = ['0011', '001011', '001', '0', '00111', '01011', '11001']
print(div_7(bin))