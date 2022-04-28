from WordFrequency import *


def test_calculate_highest_frequency(text):
    obj = WordFrequencyAnalyzer()
    assert obj.calculate_highest_frequency(text) == 2, "Should be 2"


def test_calculate_frequency_for_word(text, word):
    obj = WordFrequencyAnalyzer()
    assert obj.calculate_frequency_for_word(text, word) == 2, "Should be 2"


def test_calculate_most_frequent_n_words(text, n):
    obj = WordFrequencyAnalyzer()
    expected = [WordFrequency('this', 2), WordFrequency('frequency', 1), WordFrequency('gives', 1)]
    actual = obj.calculate_most_frequent_n_words(text, n)
    set1 = set((x.word, x.frequency) for x in expected)
    difference = list(x for x in actual if (x.word, x.frequency) not in set1)
    assert difference == [], "Should be []"


text = 'Hi this is Testing, This gIveS you *HiGH Frequency@'
word = 'ThIS'
n = 3
test_calculate_highest_frequency(text)
test_calculate_frequency_for_word(text, word)
test_calculate_most_frequent_n_words(text, n)
