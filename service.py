import os
import numpy as np
import io
import random
import glob

def run(jobID):
  """
  title:: 
      run
  description:: 
      Run the model/get the predictions according the service.
  inputs::
      jobID 
            Job ID from datashop application used for search file or save file

  returns::
      insightsDataFileLocation
      insights data file location.

  load data from temp folder
    >  json data is data.json
    >  all images and CSV are named with jobID_"filetype"
    >  jobiD_csv.csv   "61ef72ed396fc5330c15f250_csv.csv"
    >  jobiD_image.png   "61ef72ed396fc5330c15f250_image.png"
  """
  # load data as list from temp folder

  fileslist = glob.glob(os.getcwd() + "/tmp/" + jobID + "-image"+"*")

  ## perform model inference
  result_1 = random.random()

  print("model inference finished!",result_1 )

  ## for multiple results return list of resutls   results = [result_1,result_2,result_3]

  return [result_1]
