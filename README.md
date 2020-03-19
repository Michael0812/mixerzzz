<div align="center">
<a href="https://ibb.co/Zf9VfyP"><img src="https://i.ibb.co/sqRbSzJ/Zrzut-ekranu-2020-03-19-o-13-29-17.png" style='width:100%' alt="banner-img"></a>
</div>


## UX/UI
This site is devoted to the world-famous whisky. You do not have to be a lover of this alcohol, but it's worth finding out what how to mix it to get the best flavour. You may surprise yourself but also your family or friends by serving them their drink in a different way. We hope that this information will be a good introduction to the world of whiskey and bring you closer to learning about different types of mixing. The purpose of this page is not to provide extensive book definitions, but to explain what is best mixed with your favorite whisky. However, if anyone has any information or questions that could not be find on this website, please do not hesitate to contact us.


## Wireframes
Wireframes were created in Adobe XD and can be found [here](wireframes)


## Existing Featurers


### HOME PAGE
#### Logo
The logo is of one of the most important things on every website . This is a suitable business card for brands, it is worth ensuring that it is transparent and legible to the user. Therefore, the logo idea was obvious for this page. The logo that I have used is simple but effective, straight away gives you an idea that the content on this website will have something to with drinks. Logo It is transparent and easily accessible. We have used the logo at the left hand side in the navigation bar as well as at the bottom of the page in the footer section. We are certain that these two location are the best to make sure user will remember the brand. Logo is visible on all devices.


#### Navbar
Navigation bar is located at the top of every page. For a better UX on smaller devices navbar is changed to toogle navbar. 

Links located in navbar are connect with following pages of the website :
* Drinks - goes to drinks page ( User can see all drink and manipulate them).
* Add - goes to add page (User can add new drink).
* Contact - goes to contact page (User can contact us).


#### Banner - image
In web design, a hero image is a large web banner image, prominently placed on a web page, generally in the front and center. The hero image is often the first visual element a visitor encounters on the site; it presents an overview of the site's most important content. A hero image often consists of image and text, and can be static or dynamic. On this website the hero image presents bar shelfs with loads o9f different bottles of alcohol. This image was used to make users aware of what the website is about, also it does make it a bit more interesting to scroll down to find a bit more. On small devices user can see title that is located on the bottom of the banner image. While, on the large devices for better view title is moved to the top of the banner.


#### Introduction
The main content on the website is located jest bellow the banner in the center for better view. There is an introductory paragraph about what the website is about.


#### Mixing
In this section user can find information and explanation how mixing works along with some whisky bottle graphic to support the text. Also, on a medium device user can see image with bootle. On larger devices image is located next to the text. However for a better view and website transparency image is not visible on a small device. Below this paragraph there is a list of drinks such as coke, water, tea etc. that we are going to score from 1-5 that taste good or bad with specific types of whiskeys. 


#### Scoring
This is where it gets even more interesting for the user. This section explains that they can rate they favorite whisky mixer drink from 1 being worst and 5 being best. Also, it tells the user the drinks page can be used as a guidance to try their favorite whiskeys with different drinks. 


#### CTA
This is the section that encourages users to stay on the page and take action by signing up and  adding their own ideas to the drink page. 


#### Footer
It is located on every page. Logo in the footer takes the user back to the Home page. There are few links that take you further to other pages on this site:

* Drinks - goes to drinks page ( User can see all drink and manipulate them).
* Add - goes to add page (User can add new drink).
* Contact - goes to contact page (User can contact us).

Also connects to social media:
- [Facebook](https://www.facebook.com/thewhiskyexchange)
- [Twitter](https://twitter.com/WhiskyExchange)
- [Instagram](https://www.instagram.com/whiskyexchange/)


#### DRINK PAGE
On this page, the user will see the cards with the drinks (pictures, type, name, description and scoring system). Information he has read on the previous page can now be used. He is allowed to use four basic functions of persistent storage.

**C**reate ( located in ADD page) - User are allowed to add new drink. All fields are required to be filled. Also, user is asked to add a small image. It was used to make it more user friendly for other people and to keep cards looking nice and clear. 

**R**ead - User can easily read all information located in the cards.

**U**pdate - There is an edit button located on each card, moves the user to edit page where they can change any field they want to what they think is correct. At the end they can use submit button that takes them to accept all changes and send user back to the drink page to see all the changes. While, cancel button will not go to change anything and will send them back to the home page

**D**elete - User is also allowed to delete one or even all of the database (cards). To make sure no one can broke the app, defensive design was created. After deleting all database (cards) information pops up to inform that there is no drinks at the moment and anyone is allowed to add new one.


#### Contact Page
On this page, user can easily find the contact form to send a message to the admin. If anything was unclear or if they have got any other information they can easily fill up the form giving details and send it.


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

### How to run this project locally

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
git clone https://github.com/Michael0812/mixerzzz
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

- ```IP  :  0.0.0.0```
- ```MONGO_DBNAME  :  database name```
- ```MONGO_URI  :  mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority```
- ```PORT  :  5000```

9. In the heroku dashboard, click **Deploy**.
10. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click **Deploy Branch**.
11. The site is now successfully deployed.
