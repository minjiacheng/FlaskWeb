Visit https://flaskweb1234.azurewebsites.net/ to see the dog breed identifier in action.



Running on Azure server in Python 3.6



.skipPythonDeployment tells Azure to skip the normal Python deployment steps.



web.config and FlaskWeb.py are necessary to tell Azure how to set up the Fast CGI handler and how to run our program.



requirements.txt tells Azure the required packages.



To deploy this program on your Azure server,
 
  - fork this repository

  - open Azure portal and create a new Web App

  - install Python 3.6.4 via extensions

  - deploy via GitHub

  - open http://<your-app>.scm.azurewebsites.net/

  - selecting Debug Console --> CMD.

  - navigate to d:\home\python364x64

  - Use python.exe -m pip install --upgrade -r d:\home\site\wwwroot\requirements.txt to install all of the packages we need

  - restart your Azure app and you should be good to go!


(See tutorial at https://github.com/Cojacfar/FlaskWeb for a detailed guide.)



In FlaskWeb folder, the program is much similar to a Python package in structure.



logreg_model.sav is the model we created in python and will be loaded into our Web App



index.html is a html template we will use to display our prediction result



uploads is the folder that will store any user uploaded image temporarily



program will read labels.csv to obtain a list of all possible breeds it can predict



__init__.py initiates the program, loads the models once (to avoid loading it over and over on request)



upload_img.py allows user to upload their image for prediction and carries out some simple validation check



process_and_report.py does all the image processing, making predictions ploting the results etc. and returns the plot to be called by our html template.
