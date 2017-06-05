from arraystack import ArrayStack

def main(sentence):

    k = 0
    s = ArrayStack()
    sentence = str(sentence)
    for item in range(len(sentence)//2):
        s.add(sentence[item])

    for item in range(len(sentence), len(sentence)//2, -1):
        if s.isEmpty():
            print(True)
            return True
        if sentence[item - 1] == sentence[k]:
            s.pop()
            k += 1
        else:
            print(False)
            return False

    print(True)
    return True

main('srts')