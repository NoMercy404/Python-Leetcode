def IsAvailable(ransomeNote,magazine):
    tab1 = []
    if(len(ransomeNote)>len(magazine)):
        return False
    else:
        for i in ransomeNote:
            tab1.append(i)
        for j in magazine:
            if(j in tab1):
                tab1.remove(j)
        if(len(tab1)==0):
            return True
        else:
            return False
ransomeNote = "adb"
magazine = "abcd"
print(IsAvailable(ransomeNote,magazine))