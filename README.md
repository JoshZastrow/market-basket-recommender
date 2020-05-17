# Instacart Market Basket Analysis Challenge

Hello, this is a repo for the Instacart market basket challenge on Kaggle. It contains research and code related to designing a recommender system for shopping preferences. Background can be found here: https://www.kaggle.com/c/instacart-market-basket-analysis

# Why?
### Explore various recommender system implementations
The motivation for this project is to build working knowledge on designing and implementing recommender systems. We are working with real business data on actual business problems, so the design of this project is also a case study in a sense. The intention of this project is to be fun, a fast track to mastery through learning, and directly applicable to current industry challenges.

### Refine the framework for appling Machine Learning and Data Science
There are mental models that are really handy for framing business problems as prediction problems. There are also frameworks that allow you to get to a quality minimum-viable-ML-product quickly. This project is an opportunity to solidify these learnings and battle test them with low risk. Be bold and test your knowledge!

### Generate insightful and practical information from the data
This project is intended to simulate a real world challenge. So the deliverables on this project should provide actionable decisions for the client. Depending on your focus, the client could be a non-technical stake holder, another software application, or a future contributor. 


# Goals
### At least one end-to-end pipeline of a recommender model
The main focus here is to build recommender models. At least one will be considered a success

### A distilled data science story that walks the user through the problem and solution
I will refer to the familiar saying here--it's not what you know, it's what you show. Strive to frame the problem to it's simplest scope, explain the methodology, and provide a solution. The goal is to make all this simple, interesting and concrete--backed by solid reasoning and telling visualizations.

# Anti-Goals
### A collection of unfinished, unclear and unusable code
Sloppy, broken code as the completion of whatever you set out to do is unacceptable. If this seems insurmountable, reduce scope of your project so you can finish with quality code that delivers something, or delete your code.

### A lack of any recommender models
Having no recommender models in a recommender repo--avoid at all costs.

### Models that fail to produce results or meet evaluation benchmarks
A toy model is totally okay! A model that does not actually do anything (produce all zeros?) is not.

# Want To Contribute?
Looking forward to reading what you come up with! There is plenty of room for more models! Here are some of the current to do's if you're not sure where to start:

TO DO:
- write-up goal metrics and evaluation metrics in the main notebook
- develop a baseline model that can run end to end (ingest -> serve predictions)
- develop evaluation visualizations for model results


# Project Organization

### Main Notebook Holds all polished research

```./main.ipynb```

This is the "front page" of the project. Provide information for the audience and any telling conclusions you find in the data. The main.ipynb should be broken out by sections which include things such as:

- problem formulation
- success/failure metric
- evaluation approach
- data exploration
- feature engineering
- modeling approach
- model training
- evaluation results
- post processing
- experimentation approach
- conclusions / results. 

The content can be made up of written explanations, tables and data visualizations. For deliverables that require many lines of code, please reduce it by:

1) loading the outputs only, such as figures and tables through IO commands (load pandas table, load .png file), 
2) calling a function from within a module such as `/models/utils.py`.

or any other snazzy methods you know.

### Notebooks directory holds all the prototyping and development code

``` ./notebooks```

As you ask questions about the data and explore possible features for your model, and even select the best model, keep your WIP code here. Only the code needed to generate your best findings with either move to the main notebook if it's explorative, or moved to `models/utils.py` to be used in a model pipeline.

Please follow this file naming scheme:

```<Full Initials>_<YYY-MM-DD>_<description-of-what-purpose>.ipynb```

For example:

```JAZ_2020-05-01_feat-average-purchase-amount.ipynb```

### Models directory holds all the production-ready pipelines
    
    ```./models/baseline_model.py```
    
When you have developed new features, visualization pipelines, training schemes, or whole models, you can move your code into a pipeline or create a new pipeline of your own. Pipelines work as dags, so you can add a pipeline branch from any existing pipeline (say after an initial data ingestion step). While notebooks are free-form, consider these pipelines standardized and on their way to being production ready. 

**_NOTE: Keep your processing logic functions separate from the pipelines in a testable module, like utils.py. Import your functions and use them in the pipeline._**

Each pipeline is considered a script, so they are called from a bash script / command line to execute. Functions and models used in these pipelines should come from packages and modules. 

# Getting Started

1) Clone the repo into a destination folder
2) Navigate into the repo

3) Create an .env file in this repo and assign values to the environment variables:

```sh
# market-basket-recommender/.env
export KAGGLE_USERNAME=testestest
export KAGGLE_KEY=xxxxxxxxxxxxxx
export APP_DIRECTORY=/Users/joshzastrow/GitHub/market-basket-recommender

```

4) Create a virtual environment, activate it and install dependencies

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

```

5) Run the baseline model (as it stands currently)


```sh
$ python3 models/baseline_model.py show
$ python3 models/baseline_model.py run

```

6) Navigate to the notebooks directory and spin up a jupyter lab notebook to start your own modeling journey!


```
$ cd notebooks
$ jupyter lab

```

7) Useful code to get you started -- all the raw data from the lastest model run

```
from metaflow import Flow

data = Flow('BaselineModel').latest_successful_run['start'].task.data

orders_df = data.orders
orders_df.head()
```

Have Fun!
