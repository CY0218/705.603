# Project 3: Deep Learning
## Module 5 - Assignment 5

### Categorical Data Transformation using Ordinal Encoder

This notebook showcases the usage of the ordinal encoder in scikit-learn to transform categorical data into a numerical format. The dataset used in this demonstration is a sample of a used car dataset downloaded from Kaggle, which was pre-processed using Google Colaboratory. A total of 10 columns were transformed using the ordinal encoder to enable further processing by a deep neural network.

The ordinal encoder in scikit-learn is used  in this notebook to transform categorical data into numerical format. It assigns a unique integer to each category in the data, which represents its position in a predefined ordering scheme. This allows machine learning algorithms to interpret categorical data as numerical values and operate on them. Google Colaboratory was also used for working with large datasets.  It is a cloud-based Jupyter notebook environment that provides access to powerful computing resources that enables users to write and run code in a browser, making it an ideal platform for working with resource-intensive machine learning tasks.

### Install

This project requires Python 3 and the following Python libraries installed:
  - Pandas
  - Sklearn
You will also need to import a function OrdinalEncoder from scikitlearn library to transform categorical data into numerical format.

### Code

The code is listed above as Used_Car_DataTransformation.ipynb notebook file.  Additional supporting code can be found in sed_Car_DataTransformation-2.py.

### Run

In a terminal or command window, navigate to the top-level project directory Assignment5 (that contains this readme) and run the following command:  jupyter notebook Used_Car_DataTransformation.ipynb 

### Data
The dataset used in this project is available at *https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog*.  This dataset contains the following categorical features:

**Features**

- manufacturer_name
- model_name
- transmission
- color
- engine_fuel
- engine_type
- body_type
- state
- drivetrain
- location_region

**Link to Google Colab:**
  *https://colab.research.google.com/drive/1AH74prX3uge1bRwBMVs1MMPnYcrdS7-d?usp=sharing*
