
file = open ("../chat.txt")
# try:
#     for line in file:
#         print(line)
# finally:
#     file.close()
lines = file.read().splitlines()
for line in lines:
    print(line)
