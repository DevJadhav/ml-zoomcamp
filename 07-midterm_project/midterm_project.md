# Midterm Project - Employee Retention Prediction

## Problem Description

This project is to train a model to predict if employees will leave a company.

## Dataset

Dataset used - https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction.

This dataset contains information about employees who worked in a company such as satisfaction levels, salary, number of projects, average monthly hours, tenure and more.

## Training

I commenced the project by conducting an extensive Exploratory Data Analysis (EDA), followed by meticulous data cleansing to ensure data quality and integrity. Subsequently, I initiated the training phase with several predictive models, specifically Logistic Regression, Decision Tree, Random Forest, and XGBoost. Post-training, I dedicated substantial effort to hyperparameter tuning for each model to optimize their performance. After a thorough evaluation process, XGBoost emerged as the superior model, exhibiting the most favorable results, and was therefore selected as the definitive model for deployment.

## Export

1. I have developed a `train.py` script that facilitates the training of the machine learning model, subsequently saving the trained model as a `model.bin` file.

2. Subsequently, I authored a `predict.py` script that initializes the model from the `model.bin` file and implements a function to process employee information through a POST request, yielding a predictive score.

3. To validate the prediction application's functionality, I crafted a `test.py` script that enables the input of employee data, processes it, and returns a predictive determination.

## Setup locally

1. Install Pipenv:
````
pip install pipenv
````


2. Install the requirements:
    - flask
    - numpy
    - scikit-learn==1.3.0
    - gunicorn
    - xgboost
````
pipenv install gunicorn flask numpy scikit-learn==1.3.0 xgboost
````


3. Clone the repo to the Pipenv directory


4. Run the `train.py` script to train the model and export the model file:
````
python train.py
````


5. Run the `predict.py` script to run the webservice using gunicorn and is then ready for input:
````
python predict.py
````


6. You can now run the `test.py` script in another terminal window to pass the employee data to the predict app and get back the termination prediction:
````
python test.py
````

7. Edit the `employee` json in the `test.py` file to be able to test out other variations and get different results.


## Setup using Docker

1. Build a docker image:
````
docker build -t NAME_OF_PROJECT .
````

2. Run the Docker image:
````
docker run -it --rm -p 9696:9696 NAME_OF_PROJECT
````

3. You can now run the `test.py` script in another terminal window to pass the employee data to the predict app and get back the termination prediction:
````
python test.py
````

4. Edit the `employee` json in the `test.py` file to be able to test out other variations and get different results.


## Cloud deployment

First we want to push our image to Docker hub.  

If you haven't logged into docker yet:
```bash
docker login
```

To be able to push the local image to hub you first need to tag it to your login and desired repository name:
```bash
docker tag NAME_OF_PROJECT devjadhav/NAME_OF_PROJECT:latest
```

Now it can be pushed to the hub:
```bash
docker push devjadhav/NAME_OF_PROJECT:latest
```

I chose to use Azure to deploy my container. This was done using their `Container App` service.  
The JSON template I used to deploy the container can be found [here](template.json).  
Alternatively the container app can be created in the portal all you need to specify is the name of the container in docker hub ie in my case `devjadhav/NAME_OF_PROJECT:latest`.  