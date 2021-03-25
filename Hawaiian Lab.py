vowels ={"a":"ah","e":"eh","i":"ee","o":"oh","u":"oo"}
catch={"ae":"eye","ai":"eye","ao":"ow","au":"ow","ei":"ay","eu":"eh-oo","iw":"v","ew":"v","uw":"w","ow":"w","iu":"ew","oi":"oyo","ou":"ow","ui":"ooey","ew": "v","uw": "w","ow": "w","aw": "w"}
chars =  ("aeioupkhlmnw")
chars2 =  ['a','e','i','o','u','p','k','h','l','m','n','w',"'"," "]


def isvalid(resp):
    for i in resp:
        if i in chars2:
            pass
        else:
            if i not in chars2:
                return False
    return resp


def hawian(resp):
    new = ''
    i = 0
    result = []
    while i < len(resp):
        resps = resp[i]
        if i < len(resp) - 1:
            pair_letters = resps + resp[i + 1]
            catches = catch.get(pair_letters)
            if catches is None:
                catches = vowels.get(resps)
            else:
                i = i + 1
        else:
            catches = vowels.get(resps)

        if catches is not None and i < len(resp) - 1:
            catches = catches + '-'
        result.append(catches or resps)
        i = i + 1
    for i in result:
        if "'" in result:
            x = result.index("'")
            if result[x - 1] == "-":
                new = result[:n-1] + result[n:]
        if ' ' in result: 
            x = result.index(" ")
            if result[x - 1] == " ": 
                new = result[:n-1] + result[n:]
    print("The Hawaiian pronunciation of",resp,"is",new)
    new = new.join(result).capitalize()
    return new

    

resp= input("what is Hawaiian word?")
resp= resp.lower()
while not isvalid(resp):
    resp = input("Invalid input, please use a valid word: ")   

print(hawian(resp))

again = input("Want to do another word? Y/YES/N/NO ")
again = again.upper()
while again != "N":
    if again == "Y":
        resp= input("what is Hawaiian word?")
        resp= resp.lower()
        while not isvalid(resp):
            resp = input("Invalid input, please use a valid word: ")
        print(hawian(resp))
        again = input("Want to do another word? Y/YES/N/NO ")
        if again == "N":
            break
    
