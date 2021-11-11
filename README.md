# find-number-palindrome

#### I watched a YouTube video recently: https://bit.ly/3HikIVU.

#### This video suggested that when you take any number, and added it with its reverse value (ie, 174 + 471), you would eventually find a palindrome. If the addition was not a palindrome, take that number and add it to its reverse value, until you reach a palindrome.

#### This seems to work for most numbers. Within three to four iterations, you'll find a palindrome. The example posed in the video went a little like this:

#### (174 + 471) = 645
#### (645 + 546) = 1191
#### (1191 + 1911) = 3102
#### (3102 + 2013) = 5115

#### Congrats. 5115 is the palindromic number, Game over.

### However...

#### There's a number that bucks the trend, which is why I wanted to give this a go and try for myself - that number is 196. Supposedly, 196 doesn't ever produce a palindromic number. As part of the video, I thought this was a gimmick for views and likes. So, I wanted to put it to the test and create a programme that proved or disproved this guy's theory.

#### After 100 iterations, it didn't work. Same with 10,000 iterations too.

#### 98: <br>1643130837774473154788262996461373387738131345 + <br>5431318377833731646992628874513744777380313461 = <br>7074449215608204801780891870975118165118444806
#### 99: <br>7074449215608204801780891870975118165118444806 + <br>6084448115618115790781980871084028065129444707 = <br>13158897331226320592562872742059146230247889513
#### 100: <br>13158897331226320592562872742059146230247889513 + <br>31598874203264195024727826529502362213379885131 = <br>44757771534490515617290699271561508443627774644

#### On the 100th iteration, it was spewing musbers like "44757771534490515617290699271561508443627774644". Once you get there, how likely is it to find a palindrome? I would post the final few iterations before 10,000 but Chrome crashed whan I began editing this document. There were 4,159 characters in the 10,000th number, just for size!

#### There we have it - 196 is a problematic, un-palindromic number!
