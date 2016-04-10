# SumCrossword
Summarize Webpage into a crossword puzzle.

This works by frankensteining three python scripts. (Rake[https://github.com/aneesha/RAKE], Sumy[https://github.com/miso-belica/sumy], and http://bryanhelmig.com/python-crossword-puzzle-generator/).

1. Uses sumy to capture and summarize any webpage into SENTENCES_COUNT sentences. 
2. Use RAKE (Rapid Automatic Keyword Extraction) to extract the keywords from those sentences
3. Use crossword puzzle generator to make the puzzle from the clues previously made
4. Parse the crossword output into a canvas drawing
5. Enjoy crossword puzzle. Solve it! [Print it out]
6. (Anticipated) Share through a generated .html file.



  - - - -
#### Input ####
A Url. This python file will allow you to summarize any webpage into a crossword file. 
#### Output ####
The result is a postscript image (vector) with the crossword and a .txt with the clues.


## Usage: ##
* Download python.
* Download the stuff it needs [like nlp library]. # See the imports 
* Download files.
* Find a website with article/news style text.
* run:

> python test.py [url]

Sample Use cases:
Political Research/Govnt[https://www.washingtonpost.com/politics/cruz-picks-up-all-delegates-in-colo-sanders-win-in-wyo/2016/04/09/5bf92a3e-fec5-11e5-813a-90ab563f0dde_story.html]. 
![picture alt](https://github.com/TauqirA/SumCrossword/blob/master/primary.PNG?raw=true)

Market Research[http://seekingalpha.com/article/3964204-bmw-takes-leap-ahead-tesla]:
![picture alt](https://github.com/TauqirA/SumCrossword/blob/master/bmwVTesla.PNG?raw=true)

Science/Tech [http://blogs.discovermagazine.com/d-brief/2016/03/08/go-google-sedol-artificial-intelligence/#.Vwo7_aQrKhc]:
![picture alt](https://github.com/TauqirA/SumCrossword/blob/master/go.PNG?raw=true)

Solutions are also posted. 


