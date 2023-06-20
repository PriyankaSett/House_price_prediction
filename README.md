## End to End ML project 
## House Price Prediction Assignment

### 1. Create a new enviornment 
```
conda create -p venv python==3.8 -y
```
Then activate using 
```
conda activate venv/
```
### 2. Create 'requirements.txt'. 
To install any library mentioned in 'requirements.txt' do : 
```
pip install -r requirements.txt
```
### 3. Create 'setup.py'. 
To build : 
```
pip install -r requirements.txt
```
or : 
```
python setup.py install
```
This will biuld the package.


### 4. Before proceeding for the modular coding we need to have a clear idea what and how to do. For this we perform a detailed data exploration which helps us to understand the data which further helps in data modelling. All these are usually done using jupyter notebooks and are kept in a different folder $notebooks$. The data is also kept in this folder. The data exploration with various insights can be found in 'EDA.ipynb'. Next comes training the models. This is done in detailed in 'Model_training.ipynb'. We try to use libraries like 'Pipeline', 'ColumnTransformer' and do a comparitive study for different models. 



### Once these are done now we are good to go for Modular coding. 


### In the home folder we do create 'src', 'notebooks', 'README.md', 'requirements.txt' and 'setup.py'. These are the main modules. Inside them we have broken the tasks in other modules. 


### 5. Create source module : 'src'. 
In this we have -  
- `__init__.py`   
- `logger.py`  
- `exception.py` 
- `utils.py` 
- 'components' : This consists of three important modules which help in data ingestion, data transformation and model training. 
- 'pipeline' : This consists of training pipeline and prediction pipeline. 



### 6. Brief idea of the above modules. 

       - logging.py : This module help us in logging the steps and let us know if everything is going ok. 

       - exception.py : This module will catch the exception and give information of its types and location. 

       - utils.py : This module will contain the functions/methods which can be called at any point of time inside any module.  
       
       - data_ingestion.py : Here we read the data and split in train and test set. 

       - data_tranformation.py : The main purpose of this module is to transform the data, i.e. both the train and the test data. In this module, we will load the splitted data and transform it. For transformation, we identify the numerical and categorical columns and transform those seperately and create pipelines for both of them. In this project we have only numerical data. In preprocessing we need to take care of missing values, outliers and then feature scaling needs to be done. After these are done, the module will return transformed train, test data. Along with this, the preprocessing/transforming steps are saved in a pickle file. 

       - model_trainer.py : In this module


       - training_pipeline.py : 


       - prediction_pipeline.py : 

### 7. Deployment : In this we use FLASK api to deploy the code. We need to write 'app.py' module, along with templates which includes the input html page and output html page. The information from input html page will read by 'app.py' and then it will perform the training and predict the output which will be displayed at output html page. 

The web page looks like this : 
![image1](image3.png)
![image2](houseprice2.png)          

Now we have to deploy this in cloud platform like - AWS, Azure, GCP etc. 


