## Mutual Information ##

Mutual Information is a measure of mutual dependence between two random variables.

### Example Problem ###

Suppose we were to categorize newspaper articles into events, obituaries, and classifieds. 
We then asked ourselves how much does the term 'orange' contribute to those categories or classes? 
MI provides us a measure of this information for a term given a class. We would have a perfect MI 
score of 1 if 'orange' only appeared in obituaries and that is the class we were determining the MI score for. 
We would have a score of 0 if, however, the distribution of the term in the class is the same as the distribution 
of the term in the collection of classes as whole.

Consider the following matrix:
    
|                        | In class Obituaries | Outside of class Obituaries |
| Term 'orange' seen     |  49                 | 27,652                      |
| Term 'orange' not seen |  141                | 774,106                     |

Using Mutual Information we can determine that the MI of 'orange' in Obituaries is 0.0001105355861

### Further Reading ###
 - [Wikipedia](http://en.wikipedia.org/wiki/Mutual_information)
 - [Introduction to Information Retrieval](http://nlp.stanford.edu/IR-book/html/htmledition/mutual-information-1.html)
 - [Formula](http://mathurl.com/kqj8pa8)
