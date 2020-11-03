'''
Given two strings representing sentences, 
return the words that are not common to both strings 
(i.e. the words that only appear in one of the sentences). 
You may assume that each sentence is a sequence of words 
(without punctuation) correctly separated using space characters.

Ex: given the following strings...


sentence1 = "the quick", 
sentence2 = "brown fox", 
return ["the", "quick", "brown", "fox"]


sentence1 = "the tortoise beat the haire", 
sentence2 = "the tortoise lost to the haire",
return ["beat", "to", "lost"]


sentence1 = "copper coffee pot", 
sentence2 = "hot coffee pot", 
return ["copper", "hot"]
'''
def divide_words(strng):
    """This function takes a sentence and return a set of the word of the input sentence with no duplicates

    Args:
        strng ([String]): [This is a sentance that needs to be divided into words]

    Returns:
        [set]: [This set contains all the words in the input with no duplicate, strng.]
    """
    word = ''
    word_lst = set()
    for i in range(len(strng)):
        if strng[i] == ' ':
            # divide the word from the sentence
            word_lst.add(word)
            word = ''
        elif i == len(strng)-1:
            # divide the last word of the sentence
            word += strng[i]
            word_lst.add(word)
            word = ''
        else:
            word += strng[i]
    
    return word_lst

def sort_unique(sentence1, sentence2):
    """This function takes two sentences, divide them into words, then find the words that don't appear in both sentences and return these words as a set

    Args:
        sentence1 ([string]): [This is the first sentence. It will be compared to the second sentence]
        sentence2 ([string]): [This is the second sentence. It will be compared to the first sentence]

    Returns:
        [set]: [this will retun the words that never appear in both sentences as a set]
    """
    words1 = divide_words(sentence1)
    words2 = divide_words(sentence2)

    unique_words = set()
    
    for word in words1:
        unique_words.add(word)

    for word in words2:
        if word in unique_words:
            unique_words.remove(word)
        else:
            unique_words.add(word)
    
    return unique_words



if __name__ == '__main__':
    sentence1 = "the quick"
    sentence2 = "brown fox"
    print(sort_unique(sentence1,sentence2))
    print()
    
    sentence1 = "the tortoise beat the haire"
    sentence2 = "the tortoise lost to the haire"
    print(sort_unique(sentence1,sentence2))
    print()
    
    sentence1 = "copper coffee pot"
    sentence2 = "hot coffee pot"
    print(sort_unique(sentence1,sentence2))
    print()