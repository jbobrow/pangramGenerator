# pangramGenerator
Using a simple probabalistic method for generating sentences, called a Markov Chain, the pangram generator is first trained on a dataset, such as a favorite author, book, blog... and then set free to generate pangrams, sentences that contain all of the letters of the alphabet, to use while showing off or testing out different fonts. Inspired by listening to Lumi's podcast interview of Frere Jones, http://blog.lumi.com/wellmade/2-tobias-frere-jones.

## How to use the Pangram Generator
1. Download or clone this repository
2. Open Terminal (on a Mac) or a command prompt (on a PC)
3. Navigate to the pangram generator (easiest to do on a mac by typing `cd` and dragging/dropping the folder into the terminal window and pressing return)
4. Create a lexicon from a corpus of your choosing
	1. place a `.txt` file in the `Books` folder
	2. in Terminal, type `python pangram-trainer.py`
	3. `enter a corpus: ` prompts you to enter the name of the `.txt` file you want to train from (i.e. if my corpus is mobydick.txt, hypothetically, then I would enter `mobydick`) and press return
	4. A progress bar should show you how far the trainer is in the process, which can be long and slow, depending on your hardware. Just so you know, the computer is looking at every word in the document and adding each word that follows that word to a running list, so it knows all of the possible words that can follow any single word in the text.
	5. Lexicon trained!!! (celebrate a small victory!)
5. Create some pangrams from your trained lexicon
	1. in Terminal, type `python pangram.py`
	2. `enter a corpus: ` prompts you to enter the name of the lexicon you just trained or want to use (i.e. if my corpus is mobydick.txt, definitely hyppthetical here, then I would enter `mobydick`) and press return
	3. `start with a specific word: ` allows you to start/seed the pangram with a word of your choosing. Alternatively you can enter anything (not nothing) and press return, and the script will return you a "sentence" in the form of a pangram.
	4. Rinse, Repeat... Honestly, this is more fun than I can convey in a github readme, just try it :)
