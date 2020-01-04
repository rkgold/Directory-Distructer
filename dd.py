if __name__ == "__main__":
    import os
    from sys import argv

    if len(argv) != 2:
        print('Error')
        raise AttributeError('Missing Parameter')

    orign = argv[1]

    e = os.walk(orign)
    i = []

    for x in e:
        i.append(x)

    for x in i:
        ptr = x[0]+'\\' if not x[0].endswith('\\') else x[0]
        for m in x[2]:
            print(f'Deleting file: {ptr+m}')
            os.remove(ptr+m)

    for x in i[::-1]:
        ptr = x[0]
        print(f"Deleting folder: {ptr}")
        os.rmdir(ptr)

else:
    def DelDir(folder,clean:bool):
        import os

        orign = folder

        e = os.walk(orign)
        i = []

        for x in e:
            i.append(x)
        i = i[1:] if clean else i
        for x in i:
            ptr = x[0]+'\\' if not x[0].endswith('\\') else x[0]
            for m in x[2]:
                print(f'Deleting file: {ptr+m}')
                os.remove(ptr+m)

        for x in i[::-1]:
            ptr = x[0]
            print(f"Deleting folder: {ptr}")
            os.rmdir(ptr)