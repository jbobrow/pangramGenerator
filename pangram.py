#pangramGenerator
import pickle,random

#prompt for a lexicon first
corpus = raw_input('enter a corpus: ')
corpus_name = 'lexicons/lexicon-' + corpus

# load our trained lexicon
a = open(corpus_name,'rb')
successorlist = pickle.load(a)
a.close()

# get the next word in the sentence
def nextword(a,r):
    if a in successorlist:
        # look through list and update probability based on ratio of new letters
        # count number of new letters in word
        # count number of total letters in word
        
        # choose a next word randomly, weighted by new letter ratio
        # (i.e. if we need l,z,y and the word is lazy, the array being chosen 
        # from will add the word 3 times, once each for l, z, y)
        #
        # we create a new list where a word appears in the list as many times 
        # as it has new and useful letters
        weightedList = []
        for word in successorlist[a]:
            numNewLetters = 0
            numUniqNewLetters = 0
            totalLetters = len(word)
            # iterate through the remaining letters and see how much they occur in a word
            for i in range(len(r)):
                # number of times a letter appears in the word
                occurence = word.count(r[i])    
                count = 0
                if occurence > 0:
                    numUniqNewLetters += 1
                for j in range(occurence):
                    numNewLetters += 1
                    count += 1
                    weightedList.append(word)
                # print r[i] + ' occurs ' + str(count) + ' times in ' + word
            
            # starting to figure out how to weight stronger for words that are "efficient"
            wasteCount = totalLetters - numUniqNewLetters
            # if numUniqNewLetters > 0:
            #     print word + ' contains ' + str(numUniqNewLetters) + ' needed letters and ' + str(wasteCount) + ' wasted letters'

            #TODO: add words to the list with a ratio favoring uniqueness
            # this will help shorten the pangrams (but will start to constrain variety)

        if len(weightedList) > 0:
            return random.choice(weightedList)
        else:
            return random.choice(successorlist[a])
    else:
        return 'the'

speech = ''

# main loop (only quit when user types quit or enters nothing...)
while speech != 'quit':
    #start us off with a word, if we don't have it, we'll start with 'the'
    speech = raw_input('start with a specific word: ')
    s = random.choice(speech.split())
    response = ''
    
    # keep track of letters used in the pangram so far
    remaining = 'abcdefghijklmnopqrstuvwxyz'

    while True:
        if s[-1] in ',?!.':
            # print 'yup there is punctuation in ' + s + ' and it is ' + s[-1]
            s = s[:-1]
        neword = nextword(s, remaining)
        response += ' ' + neword
        # print response
        s = neword

        # remove letters used in the latest word from the remaining string
        count = 0
        for i in range(0,len(remaining)):
            if remaining[count] in neword:
                # print remaining[count] + ' is in ' + neword
                remaining = remaining[:count] + remaining[count+1:]
            else:
                count -= 1

        # only finish when we have a sentence with all letters       
        if len(remaining) < 1:
            # print str(len(remaining)) + ' letters remaining: ' + remaining
            break 

    # show the magic
    print response