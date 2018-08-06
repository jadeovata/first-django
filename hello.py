##hello someone

def hello(name):
    if name == 'Sonja':
        print("hello Sonja")
    elif name == 'Soa':
        print("hello Soa")
    else:
        print("hello {}".format(name))

##hello("Sonja")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for  name in girls:
    hello(name)

for i in range(1,100):
    hello("abc")
