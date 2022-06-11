import os

data = os.popen('tshark -r capture-reseau.pcapng -Y "ip.src == 192.168.122.1" -T fields -e dns.qry.name | grep hallebarde').read().split('\n')

files = {}
bool_name = False
bool_file = False
file_data = b''
curr_name = b''
for query in data:
    query = query.split('.')[0]
    if query == "never-gonna-give-you-up":
        bool_name = True
        continue
    elif query == "626567696E":
        bool_name = False
        bool_file = True
        continue
    elif query == "656E64":
        bool_file = False
        files[curr_name.decode()] = file_data
        curr_name = b''
        file_data = b''
        continue
    if bool_name:
        curr_name += bytearray.fromhex(query)
    elif bool_file:
        file_data += bytearray.fromhex(query)
    

for name in files.keys():
    open(name,'wb').write(files[name])
