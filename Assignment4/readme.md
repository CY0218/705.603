# Project 2: Natural Language Processing
## Module 4 - Assignment 4

### Tokenization, Stemming, and Lemmatization*

This notebook demonstrates tokenization, stemming, and lemmatization techniques from natural language processing on the Amazon musical instrument review data obtained from Kaggle. The techniques are used to generate summary information from the reviews. Natural language processing is a field that deals with the interaction between computers and human languages. Tokenization involves breaking text into individual words or phrases (tokens). Stemming and lemmatization, on the other hand, are techniques used to reduce words to their base form. Stemming involves removing the suffixes from words to get the root form, while lemmatization involves converting words to their base form using a vocabulary and morphological analysis. These techniques help in extracting meaning from natural language and have a wide range of applications, including sentiment analysis, text classification, and machine translation, among others.

### Install

This project requires Python 3 and the following Python libraries installed:

  - Pandas
  - Nltk ('stopwords', 'punkt', 'wordnet', 'omw-1.4') 
  
You will also need to import functions stopwords, PorterStemmer, WordNetLemmatizer, word_tokenize from nlkt library for tokenization, stemnning, and lemmatization.

###  Code

The code is listed above as Amazon_Musical_Instrument_Review.ipynb notebook file.  Additional supporting code can be found in Amazon_Musical_Instrument_Review.py.  

### Run

In a terminal or command window, navigate to the top-level project directory Assignment4 (that contains this readme) and run one of the following commands:  jupyter notebook Amazon_Musical_Instrument_Review.ipynb

This will open the Jupyter Notebook softeware and project file in your web browser.

### Data

The dataset used in this project is included as Musical_instruments_reviews.csv.  This dataset is provided by Kaggle and contains the following attributes:

**Features**
* reviewerID
* asin
* reviewerName
* helpful
* reviewText
* overall
* summary
* unixReviewTime
* reviewTime

### Docker Commands 

- image build multi platform command
docker buildx build -t "eyi5/705.603:assignment4_1" --platform linux/amd64,linux/arm64 --push .

- docker build 
docker build -t eyi5/705.603:assignment4_1 .

- docker run command
docker run -it -v output:/output eyi5/705.603:assignment4_1

- enter into bash in the image
 docker run --entrypoint "/bin/bash" -it eyi5/705.603:assignment4_1

- Publish to Dockerhub
$ docker push eyi5/705.603:assignment4_1

**Link to Docker Repository:** 
*https://hub.docker.com/repository/docker/eyi5/705.603/general*
