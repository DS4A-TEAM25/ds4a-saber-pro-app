# SABER PRO Exploratory Dashboard Repo
This is the code to deploy an interactive Python Dash app created for 2020 Colombia Data Science for All DS4A. You can see the live app [here](https://ds4a-saber-pro.herokuapp.com/). 


## Introduction

Each year, Colombian undergraduates take the Test for the Quality of Higher Education - Saber PRO, as a prerequisite for graduation. The test assesses math, reading, citizenship, writing and English skills of students at every higher education institution. The scores of this test become publicly available each year, with the idea that institutions and the Government identify vulnerable populations and adjust their education policies. 

This interactive dashboard allows universities and other institutions to easily explore which factors matter the most to student performance on the SABER PRO. Our application lets institutions visualize the results of predictive models to explore how changing some of these factors could affect scores in future exams.

## App Description






## Deployment

### Plotly Dash

The app was built on [Dash](https://plot.ly/dash), which is a simple and effective way to bind a user interface around Python code. It functions as a multipage application where each *.py* file within the apps folder of this repo is a page on the app. 

### GitHub Integration (Heroku GitHub Deploys)
The app is currently deployed using Heorku through GitHub integration on the Heroku website. [GitHub integration](https://devcenter.heroku.com/articles/github-integration) is configured for a Heroku app and manually deployed, which creates an immediate deployment of the master branch from the current [GitHub repo](https://github.com/DS4A-TEAM25/ds4a-saber-pro-app). 

## Running the app locally

### Using Anaconda

**1.** Open Anaconda Prompt and activate your working environment.

**2.** Install the requirements using 

```
pip install -r path to file/requirements.txt
```

**3.** Set the current directory to the folder App and run the index.py file. This can be done by typing

```
cd path_to_folder/ds4a-saber-pro-app
python index.py
```

**4.** Navigate to http://127.0.0.1:8050/

## Deploying App from Heroku using Heroku CLI

**1.** Create heroku account

**2.** Download and install the Heroku CLI

**3.** Log into Heroku account in CMD

```
$ heroku login
```

**4.** Use Git to clone dash-saber-pro's source code to your local machine

```
$ heroku git:clone -a dash-saber-pro
$ cd dash-saber-pro
```
**5.** Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```


