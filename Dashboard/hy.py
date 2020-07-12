import pandas as pd
import pandas as pd
dataframe=pd.read_csv("hydrator/corona_tweets_46.csv", header=None)

dataframe=dataframe[0].sample(5000)
dataframe.to_csv("Hydra/corona_"+str(46-43)+"may.csv", index=False, header=None)
