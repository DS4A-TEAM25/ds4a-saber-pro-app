# Dash Identifying Factors that Contribute to SABER PRO score
This is a demo of the Dash interactive Python app created for 2020 Colombia Data Science for All DS4A.

Dash abstracts away all of the technologies and protocols required to build an interactive web-based application and is a simple and effective way to bind a user interface around your Python code. To learn more check out our [documentation](https://plot.ly/dash).


## Running the app locally

### Using Anaconda

**1.** Open Anaconda Prompt and activate your working environment.

**2.** Install the requirements using pip install -r path to file/requirements.txt

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