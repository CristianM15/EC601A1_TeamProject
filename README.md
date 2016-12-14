# This README file is intended to let any user/reviewer know that our Github is generally very disorganized (I'm not really too confident navigating Github yet so cleaning it up via CLI is very frightening and I'm not sure I can do it.) Additionally, because the master branch is already hopelessly cluttered, creating a new branch to copy our AWS structure too just copies along the clutter which I have no idea how to fix. Therefore, if you'd like to view our AWS instace, you can download the .pem file found on our master branch ("EC601_GroupProject.pem") and simply SSH into our AWS instance via the following command:

ssh -i ~/Desktop/School/EC601_Alshaykh/GroupProject_NASAFirePrediction/AWS/EC601_GroupProject.pem ec2-user@35.164.49.69

(Althogh in this case, the file path name will change depending on where you store the .pem file on your local machine.)

Below is the README for the AWS instance, although it can also be immedietely found in the directory where you SSH into:




----------  AWS README  ----------

#Created by Cristian Morales, crism@bu.edu, on 13 December 2016

----------  ACCESSING THIS AWS INSTANCE  ----------
To access the AWS instance, you can SSH into it using the following command:
ssh -i ~/Desktop/School/EC601_Alshaykh/GroupProject_NASAFirePrediction/AWS/EC601_GroupProject.pem ec2-user@35.164.49.69
(The 'EC601_GroupProject' .pem file can be found on our Github page on the master branch. The pathname in the SSH command will change depending on where you store the .pem file.)


----------  AWS STRUCTURE  ----------
This AWS instance is divided into three main sections: 'testing', 'tools', and 'training'. 
(There is also a github folder, but it is just used to store the files on our github in a directory different from our mainly used directories, all in the interest of keeping files/folders organized.)


----------  TESTING, TRAINING DIRECTORIES  ----------
The structure of the 'testing' and 'training' directories is identical. Each contains four subdirectories: 'activefireCSV', 'latlongCSV', 'temperatureCSV', and 'watervaporCSV'. The first, third, and fourth of these subdirectories contains CSV files downloaded in their original format from the NASA Earth Observatory website. Each CSV file represents the active fire, land surface temperature, or water vapo concentration across the entire globe for a given date, where this date is represented by the suffix of the CSV file name. (ex. 'activefire_31_12_2012_global.csv' corresponds to the active fire data around the globe on December 31, 2012). This original format of the CSV file contains 180 rows and 360 columns, corresponding to the conditions at intersections of the globe's 180 latitude points and 360 longitude points. Therefore, we should have many CSV files stretching back years for these three different data types.

In order to be used by our machine learning program though, these CSV files need to be reformatted so that instead of describing the conditions of all geographic positions from a single date, they instead describe the conditions of a single geographic position over the course of all days. This is done using the 'NASAdata_combine.sh' script found in the 'tools' directory (described later.) Once these CSV files have been reformatted, they are then stored in the 'latlongCSV' folder found in the 'training' and 'testing' directories. In the 'latlongCSV' folder, CSV files are named with suffixes involving the geographic location which they correspond to (ex. 'NASAdata_lat1_long17.csv' corresponds to the latitude 1deg, longitude 17deg geographic location and it's wealth of active fire, water vapor, and surface temeperatures across the past years.
In this case, not all CSV files have been reformatted because the bash/python script which does this process takes a while and we didn't believe we needed to download/reformat all the data to explain our system.


----------  TOOLS DIRECTORY  ----------
In the tools directory, we immediately have a 'python3.5 folder' in which our python program and it's related dependencies are installed. Additionally, we have a 'scripts' folder which includes the subdirectories: 'dataCollection', 'machineLearning', and 'visualization.' In 'dataCollection', we have the python scripts which downloads data from NASA websites ('activefireCSV_download.py', 'temeperatureCSV_download.py', and 'watervaporCSV_download.py') and the bash script which initiates and automates the process and finally stores them in their appropriate locations. Additionally, we have the 'NASAdata_combine.py' program which reformats CSV files according to the methods described in the previous section, a process automated by 'NASAdata_combine.sh'

In the subdirectory 'machineLearning', we find all the matlab scripts which are used by our machine learning program, although this part of the project has yet to be fully automated because it requires user input from the system visualization which was not completed in time. As such, running the CLI command "ocatve ex6.m" runs the machine learning algorithm on the file '9.csv', a choice hardcoded into 'ex6.m' until such a time as we can reliably receive input from the user.

Lastly, in the 'visualization' subdirectory, there are a few scripts that were being written to prepare for being able to automate the visualization process, but since that larger process was never completed, so neither were these preliminary bash scripts.

----------  OTHER  ----------
Lastly, we are currently hosting a static webpage off our AWS intance, which would ideally be replaced with a dynamic webpage that visualizes our fire predictions and allows us to truly interact with our users and provide them with the most relevant results to them. This static webpage is stored in the following path: /var/www/html
