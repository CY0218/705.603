# Welcome to a Readme File
## Module 4 - Assignment 4

### Tokenization, Stemming, and Lemmatization*

This notebook demonstrates tokenization, stemming, and lemmatization techniques from natural language processing on the Amazon musical instrument review data obtained from Kaggle. The techniques are used to generate summary information from the reviews. Natural language processing is a field that deals with the interaction between computers and human languages. Tokenization involves breaking text into individual words or phrases (tokens). Stemming and lemmatization, on the other hand, are techniques used to reduce words to their base form. Stemming involves removing the suffixes from words to get the root form, while lemmatization involves converting words to their base form using a vocabulary and morphological analysis. These techniques help in extracting meaning from natural language and have a wide range of applications, including sentiment analysis, text classification, and machine translation, among others.

**Requirements to run Amazon_Musical_Instrument_Review.ipynb:**
  - pandas
  - nltk ('stopwords', 'punkt', 'wordnet', 'omw-1.4').  
  
    Also, import functions from nlkt library for tokenization, stemnning, and lemmatization (stopwords, PorterStemmer, WordNetLemmatizer, word_tokenize).

## image build multi platform command
docker buildx build -t "eyi5/705.603:assignment4_1" --platform linux/amd64,linux/arm64 --push .

## docker build 
docker build -t eyi5/705.603:assignment4_1 .

## docker run command
docker run -it -v output:/output eyi5/705.603:assignment4_1

## enter into bash in the image
 docker run --entrypoint "/bin/bash" -it eyi5/705.603:assignment4_1

## Publish to Dockerhub
$ docker push eyi5/705.603:assignment4_1