# Create lexicon from corpus for generating Markov Chain strings...
import pickle, sys

# Loading bar for progress on the corpus
# http://stackoverflow.com/questions/2122385/dynamic-terminal-printing-with-python
# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int) 
        barLength   - Optional  : character length of bar (Int) 
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")

#http://stackoverflow.com/questions/5306729/how-do-markov-chain-chatbots-work
#lukebot-trainer.py
corpus = raw_input('enter a corpus: ')
corpus_name = 'lexicons/lexicon-' + corpus
filename = 'books/' + corpus + '.txt'
b = open(filename)
text = []
for line in b:
    for word in line.split():
        text.append (word)
b.close()
textset = list(set(text))
follow = {}
textset_length = len(textset)
for l in range(textset_length):
    working = []
    check = textset[l]
    printProgress(l, textset_length, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
    for w in range(len(text)-1):
        if check == text[w] and text[w][-1] not in '(),.?!':
            working.append(str(text[w+1]))
    follow[check] = working
a = open(corpus_name,'wb')
pickle.dump(follow,a,2)
a.close()
print ''
print corpus_name + ' complete!'