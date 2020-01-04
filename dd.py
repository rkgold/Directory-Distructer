if __name__ == "__main__":
    # Executed when in CL mode
    import os
    from sys import argv

    if len(argv) != 2: # Raises Error when file name missing as argv[1]
        print('Error') 
        raise AttributeError('Missing Parameter')

    orign = argv[1] # Assign root file name

    e = os.walk(orign)
    i = []

    for x in e:
        i.append(x)

    for x in i:
        ptr = x[0]+'\\' if not x[0].endswith('\\') else x[0] # Adds back slashes if not present
        for m in x[2]:
            print(f'Deleting file: {ptr+m}') # Debugging
            os.remove(ptr+m) # Removing contents to Delete folder because os.rmdir requires empty folders

     for x in i[::-1]: # used [::-1] to reverse folder order because we delete the root folder if it has empty folders in it...
        ptr = x[0]
        print(f"Deleting folder: {ptr}") # Debugging
        os.rmdir(ptr) 

else:
    # Module Version
    def DelDir(folder,clean:bool): # clean == true then leave the root folder else You Know What
        import os

        orign = folder

        e = os.walk(orign)
        i = []

        for x in e:
            i.append(x)
        i = i[1:] if clean else i #                               /\
        for x in i:
            ptr = x[0]+'\\' if not x[0].endswith('\\') else x[0]
            for m in x[2]:
                print(f'Deleting file: {ptr+m}')
                os.remove(ptr+m)

        for x in i[::-1]:
            ptr = x[0]
            print(f"Deleting folder: {ptr}")
            os.rmdir(ptr)
