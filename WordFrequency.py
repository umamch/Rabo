import re
from collections import Counter

class WordFrequency():

    def __init__(self, word='', frequency=0):
        self.word = word
        self.frequency = frequency

class WordFrequencyAnalyzer():

    def computation(self):
        # Create a regex pattern to match all characters except letter or numbers
        pattern = r'[^A-Za-z]+'
        processedTxt = re.sub(pattern, ' ', self.text).lower()  # Substitute the special character with space and convert to lower case
        self.wordList = re.split('\s', processedTxt)  # convert text in to word list
        self.wordList = list(filter(None, self.wordList))
        self.counter = Counter(sorted(self.wordList))
        return self.counter

    def calculate_highest_frequency(self, text)-> int:
        self.text = text
        wordObj = self.computation() # computation for counter
        return max(wordObj.values()) # return max value in frequency list

    def calculate_frequency_for_word(self, text, word)->int:
        self.text = text
        wordObj = self.computation() # computation for counter
        return wordObj.get(word.lower()) # return frequency of word given

    def calculate_most_frequent_n_words(self, text, n)->list:
        self.text = text
        wordObj = self.computation() # computation for counter
        listMost = []
        for (word,freq) in wordObj.most_common(n): # Looping most frequent n words
            wordFreq = WordFrequency(word,freq)
            listMost.append(wordFreq)
        return listMost

    def __init__(self):
        pass

if __name__ == '__main__':


    print("Starting the WordFrequency\n"
          "Please Enter the Input text below:")
    Input_Text= input()
    obj= WordFrequencyAnalyzer()
    print("The highest frequency in the given text is: ",obj.calculate_highest_frequency(Input_Text))
    print("Do you wish to continue to get the frequency of a given word in the text? Press 'Y' or \
     'N'")
    Answer = input()

    if Answer == "Y" or Answer == 'y':
        print("Enter the word below:")
        word = input()
        print("The frequency of the word {} in text is:".format(word), obj.calculate_frequency_for_word(Input_Text, \
                                                                                                        word))
    elif Answer == 'N' or Answer == 'n':
        print ("please continue with the rest of program")

    else:
        print("You've not selected the correct option, please continue with the rest of program")

    print("Do you wish to calculate the most frequent words? Press 'Y' or \
     'N'")
    Answer_most_frequent= input()

    if Answer == "Y" or Answer == 'y':
        print("Enter the number of frequent words:")
        number = input()
        print("The frequency of the latest {} words in text are:".format(number))
        wl = obj.calculate_most_frequent_n_words(Input_Text,int(number))
        for elm in wl:
            print(elm.__dict__)
    elif Answer == 'N' or Answer == 'n':
        print("Thanks for using the Word Frequency Analyzer")

    else:
        print("You've not selected the correct option, Thanks for using the Word Frequency Analyzer")