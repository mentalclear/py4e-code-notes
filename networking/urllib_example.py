import urllib.request

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())
    # print(line.strip()) # shows b'string' - suggesting the string is in bytes

# It's important to decode the line since it's coming in bytes.
