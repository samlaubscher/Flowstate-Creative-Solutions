﻿<div align="center">

<br>

<img src="media/flowstate.png" alt="Main Logo" width="500">


# Flowstate Creative Solutions

#### Flowstate offer custom solutions to common music production problems in the form of Max for Live devices that work within the DAW, Ableton Live.

Flowstate aims to promote inclusion, improve learning, 
and augment the output of creative professionals within the music industry. 
Services are also offered in Python MIDI Remote Scripting and custom MAXMsp solutions, 
as well as consultation in anything that bridges the gap between music and programming.

[**Click here to visit Flowstate Creative Solutions**](https://flowstate-creative-solutions.herokuapp.com/)

</div>

---

## Table of Contents

- [**1 UX**](#1-ux)

  - [**1.1 Overview**](#11-overview)
  - [**1.2 Project Goals**](#12-project-goals)
  - [**1.3 User Stories**](#13-user-stories)
  - [**1.4 Design Process**](#14-design-process)

- [**2 Features**](#2-features)

  - [**2.1 Existing Features**](#21-existing-features)
  - [**2.2 Features Left to Implement**](#22-Features-left-to-impliment)

- [**3 Technologies Used**](#3-technologies-used)
  - [**3.1 Languages**](#31-languages)
  - [**3.2 Frameworks & Libraries**](#32-frameworks-&-libraries)
  - [**3.3 Tools**](#33-Tools)

* [**4 Testing**](#4-testing)
  - [**4.1 Completed**](#41-completed)
  - [**4.2 Bugs**](#42-bugs)

* [**5 Deployment**](#5-deployment)

  - [**5.1 Heroku**](#51-github-pages)
  - [**5.2 Locally**](#52-locally)

* [**6 Credits**](#6-credits)
  - [**6.1 Contents and code**](#61Contents-and-code)
  - [**6.2 Media**](#62-media)
  - [**6.3 Acknowledgements**](#63-Acknowledgements)

---


## 1 UX

### 1.1 Overview

Flowstate Creative Solutions develop custom solutions to music production problems. They provide Max for Live devices and pythin MIDI remote scripts.

There could be potantially multiple target markets for this website including: 
  - Users interested in music production tools.
  - Users interested in python MIDI scripts.

The site is built to be efficient, meaning information and products are displayed in a clear manner.

### 1.2 Project Goals

The purpose and goals of this project are to:
- Create a full stack site based around business logic used to control a centrally-owned dataset.
- Implement CRUD functionality.
- Allow all users to read data from the database on the site.
- Allow users to sign up and create an account.
- Allow full checkout functionality with webhooks and Stripe.
- Allow users to review products once purchased.
- Modify the sites content and functionality based on visitors and registered users.
- Clearly display the sites purpose.
- Display images effectively.
- Categorise and group products by category, price & rating.

### 1.3 User Stories

### First Time Users/Shoppers

- As a user, I want a site to have a clearly defined purpose when I first enter so that I know what I am viewing.
- As a user, I want all functionality on the site to work to avoid a bad experience.
- As a shopper, I want to be able to browse all products in the db.
- As a shopper, I want to clearly see the name, price, description, category and image for each product.
- As a shopper, I want to be able to easily browse all individual product categories in the db.
- As a shopper, I want to register for an account so that I can buy products from the database.
- As a shopper, I want to be able to easily identify deals and offers, so that i can take advantage of savings on products id like to buy.
- As a shopper, I want to see how to contact the company, so that I can easily ask for assistance with bought software in the future.
- As a shopper, I want to be able to query for a product in the db so that i can refine my search.
- as a shopper, I want to be able to easily enter my card payment details without lots of hassle.

### Returning/Registered Users

- As a returning user, I want to log into my account and be presented with my own profile page.
- As a returning user, I want to see what I have bought, so that I can track my purchases.
- As a returning user, I want to let other users know how I feel about using the software, by leaving product reviews.
- As a registered user, I want to confirm my email so that i can ensure only I am using this account.
- As a registered user, I want to be able to reset or change my password if needed.
- As a registered user, I want to know my data will be securely transferred to the server so that my details are safe.

### Site Owner

- As the site owner, I want users to register for accounts so that I can implement authentication.
- As the site owner, I want users to register for accounts so that I can personalise their experience.
- As the site owner, I want access to all features available to the site when logged in as admin.
- As the site owner, I want access to an admin panel to see all content related to the site so that I can track what is displayed and update, edit or delete content if needed.

### 1.4 Design Process

### **Logo**

Flowstate provided me with their own custom designed logo.

### **Colour scheme**

I implemented a white and light blue color scheme, fitting with the existing brand colours.

- #555 - Grey was used for most of the text.
- #FFFFFF - White was used for the background color.
- #3ea6eb - Blue was used as seen on the main logo.

### **Typography**

The font I used for the main site body including the navbar was 'Rubik', supplied by Google Fonts.

### **Wireframes**

For this project, I created a number of wireframes for the layout of different pages.

<details>
<summary><b>Wireframes</b> - (click to expand)</summary>

### Landing Page

The landing page will display a splash image with some info about the site and an enter button.

<div align="center">
<img src="media\readme\landing-page-wireframes.jpg" width="500">
</div>

### Products Page

The products page will display 3 products in each row. At the top there will be a search bar, and a filter sort by button.

<div align="center">
<img src="media\readme\products-page-wireframes.jpg" width="500">
</div>

### Product Details Page

The product details page will display all details of the products as well as a reviews section.

<div align="center">
<img src="media\readme\product-details-wireframes.jpg" width="500">
</div>

</details>

### **Project Management**

This project was designed using an agile approach, utilising a Kanban board to track my development progress throughout the build. You can view the board I created using Trello [here](https://trello.com/b/sFMVph7W/flowstate-creative-solutions-project-ms4).

[Back to Table Of Contents](#table-of-contents)

---

## 2 Features

### 2.1 Existing Features

### **Intro Index Landing Page**

When users visit the sites main index page ***(/)***, they are taken to a landing page displaying information about the sites main purpose. From this page, users can either click an Enter button.

### **Products Page**

This page displays all products available for purchase.

### **Product details Page**

This page displays all products available for purchase.

### **Register & Login Pages**

These pages display a form below allowing users to enter both a username and password. They allow users to either create a new account or login to an existing one by entering these unique values. Registration requires the user to enter their password twice. The application will run validation and authentication on passwords and usernames for character and invalid or existing data checks.

### **Profile Page**

When a user registers, they will have their own profile page. This will display order history and allow users to leave a review.

### **Reviews Page**

This page allows users to review products.

### 2.1 Features Left To Implement

### About page

This would have displayed more info about the site.

### Discount functionality

This would have applied a discount to the order.

[Back to Table Of Contents](#table-of-contents)

---

## 3 Technologies Used

### 3.1 Languages

### [**HTML/HTML 5**](https://html.com/html5/)

### [**CSS/CSS3**](https://www.w3.org/Style/CSS/Overview.en.html)

### [**JavaScript ES6**](https://www.w3schools.com/Js/js_es6.asp)

### [**Python**](https://www.python.org/)

### 3.2 Frameworks & Libraries

### [**Django**](https://www.djangoproject.com/)

### [**PostgreSQL](https://www.postgresql.org/)

### [**Bootstrap**](https://mdbootstrap.com/)

### [**Font Awesome**](https://fontawesome.com/)


### [**Google Fonts API**](https://fonts.google.com/)


### 3.3 Tools

### [**VSCode**](https://code.visualstudio.com/)

### [**AWS S3***](https://aws.amazon.com/)

### [**Chrome DevTools**](https://developers.google.com/web/tools/chrome-devtools/)

### [**Git**](https://git-scm.com/)

### [**Github**](https://github.com/)

### [**Heroku**](https://www.heroku.com/)

### [**Balsamiq**](https://balsamiq.com/)

[Back to Table Of Contents](#table-of-contents)

---

## 4 Testing

### 4.1 Completed

### **Automated Testing**

- Django automated testing

- DevTools Lighthouse - I ran extensive testing with the lighthouse tool. Any pages that did not return green 90+ scores in each area were worked on to solve issues that could be addressed. Some issues included image sizes and redundant code in Bootstrap files.

- [HTML Validator](https://validator.w3.org/) - All code passed except for a few duplicate IDs and warnings on external code. I was able to discover and fix a duplicate anchor link bug using this validator.

- [CSS Validator](https://jigsaw.w3.org/) - All code passes this validator with no errors. Only warnings on external code from MDB. 

- [JavaScript Validator](jshint.com) - All code passed with no errors.

- [Python PEP8 Validator](http://pep8online.com/) - Most of my code was python based. I ran my code through the PEP8 validator and made sure no issues were raised.

### **Manual Testing**

<details>
<summary><b>Checking User Stories</b> - (click to expand)</summary>

- As a user, I want a site to have a clearly defined purpose when I first enter so that I know what I am viewing. - PASS
- As a user, I want all functionality on the site to work to avoid a bad experience. - PASS
- As a shopper, I want to be able to browse all products in the db. - PASS
- As a shopper, I want to clearly see the name, price, description, category and image for each product. - PASS
- As a shopper, I want to be able to easily browse all individual product categories in the db. - PASS
- As a shopper, I want to register for an account so that I can buy products from the database. - PASS
- As a shopper, I want to be able to easily identify deals and offers, so that i can take advantage of savings on products id like to buy. - PASS
- As a shopper, I want to see how to contact the company, so that I can easily ask for assistance with bought software in the future. - PASS
- As a shopper, I want to be able to query for a product in the db so that i can refine my search. - PASS
- as a shopper, I want to be able to easily enter my card payment details without lots of hassle. - PASS

### Returning/Registered Users

- As a returning user, I want to log into my account and be presented with my own profile page. - PASS
- As a returning user, I want to see what I have bought, so that I can track my purchases. - PASS
- As a returning user, I want to let other users know how I feel about using the software, by leaving product reviews. - PASS
- As a registered user, I want to confirm my email so that i can ensure only I am using this account. - PASS
- As a registered user, I want to be able to reset or change my password if needed. - PASS
- As a registered user, I want to know my data will be securely transferred to the server so that my details are safe. - PASS

### Site Owner

- As the site owner, I want users to register for accounts so that I can implement authentication. - PASS
- As the site owner, I want users to register for accounts so that I can personalise their experience. - PASS
- As the site owner, I want access to all features available to the site when logged in as admin. - PASS
- As the site owner, I want access to an admin panel to see all content related to the site so that I can track what is displayed and update, edit or delete content if needed. - PASS

</details>

<details>
<summary><b>Testing Functionality</b> - (click to expand)</summary>

### Navbar

- Each navbar link tested and working from each page. - PASS
- The main logo takes the user to the welcome page. - PASS
- Viewing the website on tablet or mobile devices, the navbar links dissapear and a hanmburger icon appears instead. Clicking this shows a drop down menu with all links.  - PASS

### Buttons

- The main header takes the user to the welcome page. - PASS
- The ENTER button on the welcome page returns the /products page with a 200 status code. - PASS
- Checkout buttons - When users are not signed in, they get redirected to the login page with a 302 status code. When users are signed in, they are taken to the correct page with a 200 status code, as long as the page is not admin only. - PASS
- All Back To.. buttons return 200 codes to the correct page. - PASS
- All form submit buttons POST data sucessfully. - PASS
- All Edit/Delete buttons correctly modify their data. - PASS

### Links

- All social media links redirect to the correct websites. - PASS
- Clicking any image takes the user to that images page. - PASS
- Clicking a category name takes the user to the individual pages, where more detail about the object is correctly displayed. - PASS
- No links are broken. - PASS

### Forms

- All forms were tested for prompting incorrect input types. - PASS
- All correct validation working and displaying. - PASS
- Character count limitations working. - PASS
- When posting a form with empty data, the form validation prompts the user that they must enter a value. - PASS

### Responsiveness

- All pages respond to different screen sizes effectively. - PASS
- No content behaves weirdly when resized and correctly repositions. - PASS
- No content overflows off the page at any size. - PASS

### Cross Browser and Device Testing

- All devices and broswers performed correctly during testing. - PASS
- The bug detected is in the bugs section.

### Pagination

- All pagination works on the main page - PASS

### Search & Filter Works

- Searching works by artist name returns correct works. - PASS
- Each filter route selected with the Sort By menu returns the correct filtering of works. - PASS

</details>

<details>
<summary><b>Testing 200 Codes</b> - (click to expand)</summary>

### All Users Pages

- /home - PASS
- /login - PASS
- /register - PASS
- /products - PASS
- /product_details - PASS
- /cart - PASS
- /checkout - PASS
- /profile - PASS
- /review - PASS
- /contact - PASS

</details>

<details>
<summary><b>Testing 302 Codes</b> - (click to expand)</summary>

### Visitor Page Redirects

When a user is not logged into an account, they are unable to access any payment pages beyond cart will be redirected to the login page. - PASS

### Admin Only Pages

Logging in with the username 'test', I tried to access admin pages that only the admin should have access to. - PASS

</details>

### 4.2 Bugs

### **Fixed**

- Spelling mistakes in some class and id names were discovered and fixed through testing.
- Orders were duplicating.
- Created onerror image for images that break and cause the site to look bad.

[Back to Table Of Contents](#table-of-contents)

## 5 Deployment

### 5.1 Heroku

This project was automatically deployed to Heroku from my GitHub repository. To do this, first I created my repository containing my ***.gitignore*** file set to ignore my virtual environment and ***env.py*** files, then followed these steps:

- Within the IDE's terminal window, create a requirements.txt file by typing ***pip3 freeze --local > requirements.txt***, and similarly create a Procfile by typing ***python app.py > Procfile***.

- Login or sign up for a new account on [Heroku](https://id.heroku.com/login), then click ***New > Create New App*** from your dashboard.

- Enter a name for your app and select the correct region before pressing ***Create App***.

- Select the ***Deploy*** tab and then click on the ***GitHub*** button under ***Deployment method***.

- Type your repository name in the search box next to the dropdown box displaying your GitHub account name. When the repository appears, click ***Connect***.

- In the ***Settings*** tab, under the ***Config Vars*** section, click the ***Reveal Config Vars*** button.

- Enter the key value pairs as found in your env.py file as such:
    - IP: 0.0.0.0
    - PORT: 5000
    - SECRET_KEY: YOURSECRETKEY
    - DEBUG: FALSE

- Select the ***Deploy*** tabe again and click ***Enable Automatic Deploys*** under the ***Automatic Deploys*** section. Below this is the ***Manual Deploy*** section. Select your ***Master*** branch and click ***Deploy Branch***.

- Your app will now be built, and when its completed you should see the message ***"Your app was successfully deployed"***. You can click ***View*** to launch the deployed app.

### 5.2 Locally

If you would like to run this code locally on your own machine, follow these steps:

- First open your IDE and navigate to the working directory you want to use.

- You then need to create a ***virtual environment*** to install all dependencies in a sandbox. To do this using venv use the following code:
  - ***python3 -m venv <YOUR_DIR>***

- When your virtual environment is created you need to activate it with the following code:
  - ***<YOUR_DIR>\Scripts\activate***

- Follow this link to the repository for [Flowstate Creative Solutions](https://github.com/samlaubscher/Flowstate-Creative-Solutions).

- In the top corner next to the ***About*** section, click the ***Code*** button with the downwards facing arrow icons.

- Under the ***Clone*** section, make sure the HTTPS tab is highlighted, and copy the link displayed to your clipboard. It should look like this:
    > https://github.com/samlaubscher/Flowstate-Creative-Solutions.git

- Open ***Git Bash*** in your IDE.

- Then type into the terminal window ***git clone {URL}*** and replace the ***{URL}*** with the link copied from the repository page.

- Upon hitting ***Enter*** the repository will be cloned into your current working directory.

- To then remove the origin link to this repository from your IDE, type ***git remote rm origin***.

- Alternatively, you can download the repository directly as a compressed ZIP folder from the ***Code*** dropdown box, underneath the ***Clone*** section. Unpack this ZIP folder into your virtual environment location.

- When the project is successfully cloned or downloaded and opened in the virtual environment, you need to install any dependancies and requirements by typing ***pip3 install -r requirements.txt*** into your IDE's terminal window.

- You next need to create an ***env.py*** file to store your environment variables. For this project, they are: 
    - import os
    - os.environ.setdefault("IP", "YOUR IP")
    - os.environ.setdefault("PORT", "5000")
    - os.environ.setdefault("SECRET_KEY", "YOURSECRETKEY")
    - os.environ.setdefault("DEBUG", 0)

- Then create a ***.gitignore*** file, and include this env.py file inside it to ensure your environment variables are never published publically by being pushing to GitHub.

- You are now ready run this project and push any modifications to your own repository. To run, type into the terminal ***python app.py***.

To read more about cloning repositories, you can read [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to Table Of Contents](#table-of-contents)

## 6 Credits

### 6.1 Content and code

Small parts of code were re-used from the original Boutique Ado project for the Data Centric module.

Comments inline will show any external code used.

All additional code was my own.

### 6.2 Media

The splash image used was https://unsplash.com/photos/t06xJHRFoYU

### 6.3 Acknowledgements

I would like to thank my mentor Ignatius for the time he has spent with me going over this project and all other past projects. I would also like to thank all students that offered advice, all people who supported me in any way during the project, and all friends that took the time to look at the site during development. It has been an amazing experience, and I am very thankful for everyone I have met on the course, and for all friends I will continue to keep in contact with.

[Back to Table Of Contents](#table-of-contents)
