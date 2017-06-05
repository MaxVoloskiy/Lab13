from arraystack import ArrayStack


class Palindrome:
    """
    Find the pallindrome
    """
    def __init__(self, filename):
        """
        :param filename: name of import file
        """
        self.filename = filename

    def import_from_file(self):
        """
        Return the list of pallinromes
        :return: list of palindromes
        """
        self.palindrome_words = []
        with open(self.filename, 'r', encoding="UTF-8") as file:
            for word in file.readlines():
                if Palindrome.palindrome(word):
                    self.palindrome_words.append(word)
        return self.palindrome_words

    @staticmethod
    def palindrome(word):
        """
        Check the palindrome
        :param word: word
        :return: bool
        """
        PallindromeStack = ArrayStack()
        word = word.split()[0]
        if len(word) % 2 == 0:
            index = len(word) // 2
        else:
            index = len(word) // 2 + 1

        for item in range(len(word) // 2):
            PallindromeStack.push(word[item])

        for item in range(len(word) // 2):
            check_word = PallindromeStack.pop()
            if check_word != word[index + item]:
                return False
        return True

    def export_to_file(self, filename):
        """
        Write palindromes to file
        :param filename: the name of export file
        """
        with open(filename, 'w') as file:
            for word in Palindrome.import_from_file(self):
                file.write(word)


A = Palindrome("palindrome/base.lst")
A.export_to_file("palindrome/palindrome_uk.txt")
B = Palindrome("palindrome/words.txt")
B.export_to_file("palindrome/palindrome_en.txt")