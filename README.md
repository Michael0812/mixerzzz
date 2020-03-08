<a href="https://ibb.co/NTMQCSh"><img src="https://i.ibb.co/fDsBFvR/responsive-img.png" alt="responsive-img"></a>

## Technologies Used

- Languages:

- #### HTML
- #### CSS
- #### JavaScript
- #### Python

-Tools:

- #### [Gitpod](https://www.gitpod.io/)
- #### [Github](https://github.com/)
- #### [MongoDB](https://www.mongodb.com/)
- #### [Git](https://git-scm.com/)
- #### [PIP](https://pypi.org/)

-Libraries:

- #### [JQuery](https://jquery.com/)
- #### [Bootstrap](https://getbootstrap.com/)
- #### [Flask](https://palletsprojects.com/p/flask/)
- #### [PyMongo](https://api.mongodb.com/python/current/)
- #### [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- #### [Google Fonts](https://fonts.google.com/)
- #### [Materialize](https://materializecss.com/)


## Deployment

To deploy this page to GitHub Pages from its Github repository, the following steps were taken:

1. Create an account in GitHub.
2. Sign in to the account.
3. On the home page choose **Start a project**.
4. Then, create a name for the project [mixerzzz](https://github.com/Michael0812/how_to_drink_whisky).
5. Create a respository.
6. Upload the folder to the respository.
7. Click on the **Settings** button.
8. On this subpage, in section **GitHub Pages** change the Source from **None** to **Master Branch**.
9. The website will refresh autmaticlly.
10. In section **Github Pages** is ready link waiting.

## How to deployment project in Heroku

1. Create a ```requirements.txt``` file using the terminal command ```pip freeze > requirements.txt```.
2. Create a ```Procfile``` with the terminal command ```echo web: python app.py > Procfile```.
3. Then, please put ```git add``` and ```git commit``` the new requirements and Procfile and then ```git push``` the project to GitHub.
4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
5. From the heroku dashboard of your newly created application, click on ```Deploy``` > ```Deployment method``` and select GitHub.
6. Confirm the linking of the heroku app to the correct GitHub repository.
7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:

- ```IP```  :  0.0.0.0
- ```MONGO_DBNAME```  :  ```database name```
- ```MONGO_URI```  :  ```mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority```
- ```PORT```  :  5000


9. In the heroku dashboard, click "Deploy".
10. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".
11. The site is now successfully deployed.


## Testing
Testing can be found in [TESTING.md](TESTING.md)


## Credits

 - Logo was made by [Lidia Kabala](https://www.linkedin.com/in/lidia-kabala-3b2036137/)
 
 - Text - was copied from the book [Whisky - The Manual Dave Broom](https://www.goodreads.com/book/show/17899896-whisky)
 
 - Images - was copied and shared from [The whisky exchange](https://www.thewhiskyexchange.com/)
