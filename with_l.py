with open('hello.txt', 'w') as f:
    f.write('привет, мир!')
    f = open('hello.txt', 'w')
    try:
        f.write('привет, мир!')
    finally:
        f.close()

