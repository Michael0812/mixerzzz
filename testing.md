## Testing

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox). Also, the following tools were used to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes:

- [Google Chrome's Development](https://www.google.com/chrome/dev/)

- [Responsinator](http://www.responsinator.com)

- [Am I Responsive](http://ami.responsivedesign.is/#)

- [Responsive test tool](http://responsivetesttool.com)


- I have creted my wireframes at the planning stage. However, during build I find out that some sections may not be suitable or work properly, therefore I had to come up with another solutions.

- By mistake, I have used 2 frameworks (Bootstrap and Materialize) which is not allowed. After session with my mentor we have  decided to concentrate on Materialize. However, within Materialize you can not style padding and margins in html file, as you can do in Bootstrap. I decided to crete a new css file that I called materialize.css. Within that file there is all of the margins and padding from 1rem to 5rem that helped me out with my styling.

 - I had another issue with flash message. When I was trying to add or edit a new task the aler appear on every single drink card. I did my reserach and after talking to one of the tutor I have manged to move ```{% include 'components/flash_message.html' %}``` from drinks.html file to base.html and that solved my issue.

 - I had also, faced an issue wile adding description of the drinks. I found out that different lengths of text have resulted with different sizes of cards. To stop this from happening I had to set minimum and maxium amount of text for description and this has solved the problem. Also, now I can make sure that all of the boxes are nice and consistent.
 
Also, many other small issue was solving during this project. I was doing many research, talking with people in Slack community, my mentor, tutors.


I have asked a friend to test this website which I found very helpful. Please find feedback attached

1. Is the site friendly to you? - It is very friendly, the text is easy and nice to read. I came from the phone and laptop and definitely think there is more eye catchy on the laptop. Photos and text settings on the phone do not reflect the effect of a larger screen. I like that everything is black and white, nothing is striking.
2. Would you recommend it to someone? Definitely, first of all because there are many interesting facts even though the whiskey tastes great with green tea. Everything is easy to choose and edit.
3. What does the navigation look like in it? - very simply, nothing is complicated so you do not need to be nervous, you know what to click to get where you want.
4. Is it easy to use? It is very easy to quickly and efficiently get from one side to the other
5. Is it easy access to everything and clearly explained what and how - yes, I understand what's going on. It's nice that it is first explained with what whiskey goes well, such an intro. The site is very engaging, it is nice that you read one and want to go further out of curiosity.
6. Is the website responsive on the phone tablet desktop - Yes, it is responsive on every devices. However, as I wrote above in my opioin it looks much better on a larger screen, it makes a better impression and everything is nicer set than on the phone.
7. Do all links work - all links work correctly.


### Code Validation
-  This project used [W3C  HTML Validator](https://validator.w3.org/) to validate HTML code.
- ![](https://i.imgur.com/Dt1KHNu.png) This project used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate CSS code.    
	<p>
	<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Poprawny CSS!" />
    </a>
</p>

- This project used [PEP8](http://pep8online.com/) to validate Python code.
