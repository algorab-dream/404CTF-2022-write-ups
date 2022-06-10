data = open('Cable.txt','r').read().split(' ')

print(''.join([bytes([int(byte,2)]).decode() for byte in [''.join([str(int(data[i] != data[i+1])) for i in range(len(data) - 1)])[i:i+8] for i in range(0, len(''.join([str(int(data[i] != data[i+1])) for i in range(len(data) - 1)])), 8)]]))