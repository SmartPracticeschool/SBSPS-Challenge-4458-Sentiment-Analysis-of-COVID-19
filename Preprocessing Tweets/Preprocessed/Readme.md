##About Datasets

There are 2 datasets in all. One is the combined version of all the datasets from March 20 to may 30.Due to the file size limitation set by Github, we did not upload the combined dataset. To combined the datasets in folders, please try:

``` # Read raw datas from the raw data file 
path = r'------path-------------'
files = os.listdir(path)
covid_twitter_data = pd.DataFrame()
# Concat the Twitters data into one-table
for file in files:
    data = pd.read_csv(str(path) + file)
    covid_twitter_data = covid_twitter_data.append(data, ignore_index=True) ``` 
    
Or use the join.py given before.
The other dataset is 'preprocessed_dataset1.csv' which contains the data of last 10 days that is June 20 to june 29.
