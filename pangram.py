#pangramGenerator
import pickle,random

#prompt for a lexicon first
corpus = raw_input('enter a corpus: ')
corpus_name = 'lexicons/lexicon-' + corpus

#load our trained lexicon
a = open(corpus_name,'rb')
successorlist = pickle.load(a)
a.close()

#get the next word in the sentence
def nextword(a,r):
    if a in successorlist:
        #look through list and update probability based on ratio of new letters
        # for i in successorlist:
        #     print i
        #count number of new letters in word
        #count number of total letters in word
        #place this ratio in an array assigned with this index
        #normalize the array values
        
        #alternate: choose randomly with the weightings assigned by new letter ratio
        #to do this, the easiest way was to create a new list where a word
        #appears in the list as many times as it has new and useful letters
        weightedList = []
        for word in successorlist[a]:
            # count = 0
            for i in range(0,len(r)):
                if r[i] in word:
                    # count += 1
                    weightedList.append(word)
                    # print str(count) + word
        if len(weightedList) > 0:
            return random.choice(weightedList)
        else:
            return random.choice(successorlist[a])
    else:
        return 'the'

speech = ''

#main loop (only quit when user types quit)
while speech != 'quit':
    #start us off with a word, if we don't have it, we'll start with 'the'
    speech = raw_input('>')
    s = random.choice(speech.split())
    response = ''
    
    #keep track of letters used in the pangram so far
    remaining = 'abcdefghijklmnopqrstuvwxyz' 

    while True:
        if s[-1] in ',?!.':
            # print 'yup there is punctuation in ' + s + ' and it is ' + s[-1]
            s = s[:-1]
        neword = nextword(s, remaining)
        response += ' ' + neword
        # print response
        s = neword

        #remove letters used in the latest word from the remaining string
        count = 0
        for i in range(0,len(remaining)):
            if remaining[count] in neword:
                # print remaining[count] + ' is in ' + neword
                remaining = remaining[:count] + remaining[count+1:]
            else:
                count -= 1

        # only finish when we have a sentence with all letters       
        if len(remaining) < 1:
            print str(len(remaining)) + ' letters remaining: ' + remaining
            break 

    # show the magic
    print response