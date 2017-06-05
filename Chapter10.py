reply=""
while reply.lower() != 'stop':
    reply=input("Enter Words('stop' to terminate):")
    print(reply.upper())
print("Goodbye")

while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')

while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except Exception as ex :
        print('Bad!' * 8,ex)
    else:
        print(num ** 2)
print('Bye')