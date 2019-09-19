This is basic steps for processing text. The library is based on NLTK:

1. Tokenization;
2. Stopwords;
3. Stemming;
4. Speech Tagging.
-----------------------------------------------------------
Questions:

#### 1.	Is ‘Stemming’ required before ‘PunktSentenceTokenizer’ to tag speech?
(Because I think some words will be stemmed to be ‘non-tense’: riding/rides/rode->ride, 
As the model for speech tagging, the result from ‘PunktSentenceTokenizer’ will be tagged the words with tense.)

#### 2.	Any other surrogate models (more than linear) match with the complicated NLP model for interpretation?
(The most frequent surrogate model I found to mimic COMPLICATED NLP model (e.g. fastText model etc.) is Linear classifier, 
seems no more surrogate models for interpreting complicated NLP models. )


