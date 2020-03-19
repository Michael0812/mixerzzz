
<img src="https://i.ibb.co/fDsBFvR/responsive-img.png" style="max-width:100%;" alt="responsive-img">

## Navigation

- [UX/UI](#UX/UI)
- [Wireframes](#wireframes)
- [Existing Featurers](#existing-featurers)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Heroku deployment](#How-to-deployment-project-in-Heroku)
- [Testing](#testing)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## UX/UI

## Wireframes

## Existing Featurers


## Technologies Used

#### Languages:

- HTML
- CSS
- JavaScript
- [Python](https://www.python.org/)

#### Tools:

- [Gitpod](https://www.gitpod.io/)
- [Github](https://github.com/)
- [MongoDB](https://www.mongodb.com/)
- [Git](https://git-scm.com/)
- [PIP](https://pypi.org/)

#### Libraries:

- [JQuery](https://jquery.com/)
- [Flask](https://palletsprojects.com/p/flask/)
- [PyMongo](https://api.mongodb.com/python/current/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Google Fonts](https://fonts.google.com/)
- [Materialize](https://materializecss.com/)


## Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [GitPod](https://gitpod.io/workspaces/)
- Also, full workspace [template](https://github.com/Code-Institute-Org/gitpod-full-template) for GitPod were taken from Code Instutite.

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).
    
### Instructions

1. Save a copy of the github repository located at [Github](https://github.com/Michael0812/mixerzzz) by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/AJGreaves/familyhub
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:

```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `familyHub`, with 2 collections called `users` and `activities`. You will find example json structures for these collections in the [schemas](familyhubapp/data/schemas) folder.

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`


### How to deployment project in Heroku

1. Create a ```requirements.txt``` file using the terminal command ```pip freeze > requirements.txt```.
2. Create a ```Procfile``` with the terminal command ```echo web: python app.py > Procfile```.
3. Then, please put ```git add``` and ```git commit``` the new requirements and Procfile and then ```git push``` the project to GitHub.
4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the **New** button in your dashboard. Give it a name and set the region to Europe.
5. From the heroku dashboard of your newly created application, click on ```Deploy``` > ```Deployment method``` and select GitHub.
6. Confirm the linking of the heroku app to the correct GitHub repository.
7. In the heroku dashboard for the application, click on **Settings** > **Reveal Config Vars**.
8. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

9. In the heroku dashboard, click **Deploy**.
10. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click **Deploy Branch**.
11. The site is now successfully deployed.


## Testing
Testing can be found in [TESTING.md](TESTING.md)


## Credits

 - Logo was made by [Lidia Kabala](https://www.linkedin.com/in/lidia-kabala-3b2036137/)
 
 - Text - was copied from the book [Whisky - The Manual Dave Broom](https://www.goodreads.com/book/show/17899896-whisky)
 
 - Images - was copied and shared from [The whisky exchange](https://www.thewhiskyexchange.com/)
 
 ##### Also, I was working with different websites that gave me some helps, advices and ideas for this project:
- [Mozilla Developer](https://developer.mozilla.org/en-US/docs/Learn)
- [w3schools](https://www.w3schools.com)
- [Google developers](https://developers.google.com/)
- [awwwards](https://www.awwwards.com)


## Acknowledgements

 - I would like to thanks my [girlfriend](https://www.linkedin.com/in/lidia-kabala-3b2036137/) immensely who was supporting and helping me for all my journey with this project.
 - Massive thanks to my mentor [Simen Daehlin](https://www.github.com/Eventyret), he gave me so many very useful tips and advices, and who was always open, helpful and kind me.
 - Also, I would like to thank students and tutors from Code Institute that were helping me with every issue I had, they were always trying to give me the best tips and help me sort things out.
 
 ### The content of this Website is for educational purposes only.


[Back to the top](#navigation)
