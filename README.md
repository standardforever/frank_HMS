# HOSPITAL RECORD SYSTEM

## Overview
In this project, we're building an Hospital Record System that helps hospital to manage all the records of there patients.

## Project Architecture Link

- Architecture Link - 
- Design Link -
- Database Design -

## How to contribute
Follow these steps to contribute to this project
- Clone the repo to your local machine
```
	git clone https://github.com/standardforever/frank_HMS.git
```
- Create a new branch for the feature you are currently working on
```
	git checkout -b <name of branch>
```
- To check the branch you are currently on use
```
	git branch
```
- Always git pull first before pushing to avoid conflict 
```
	git pull origin master
```
- After making changes, stage all the changes you have made locally for a commit by running 
```
	git add <file-names>
```
- Commit your changes with a descriptive commit message
```
	git commit -m "your commit message"
```
- After making sure your branch is up-to-date, push the new changes to your new branch
```
	git push origin <your-current-branch-name>
```
- Create a pull request to the dev branch
- ***DO NOT*** merge your PRS. They'll be reviewed and merged

## How to run the code (Setup and Installation)
Follow these steps to setup and run server

- In the root directory of this project, create a virtual environment
```
	virtualenv my-env
```
- Activate the virtual environment (depending on your operating system) in linux operating system
```
	source my-env/bin/activate
```
- Make a copy of the .env examples file found in the config directory. Rename that copy to .env. That's where you'd put all future environment variable/configs

- install all Packages(dependece) 
```
	pip install -r requirement.txt 
```
	OR
```
	pip3 install -r requirement.txt
```
*** To Run server***  You have to be in route directory '/frank_HMS'
```
	python3 run.py
```
- ***NOTE:*** Whenever you install a new package to the project run
```
	pip freeze --local requirements.txt
```
