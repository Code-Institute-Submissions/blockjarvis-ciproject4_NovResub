# Understore

![Mockup](/media/readme/responsive.png)

This comprehensive site was designed for an ecommerce site. The focus of the site is to provide a functional ecommerce site with a clean and modern design.

This is the fourth of four Milestone Projects that the developer must complete during the Full Stack Web Development Program at The Code Institute.

The main requirements were to build a full-stack site based around business logic used to control a centrally-owned dataset, set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

## UX

The purpose is to design an attractive website to buy products and interact with it, with a simple and intuitive layout that works on mobiles, tablets or desktops.

## User Stories
### First Time Visitor Goals
1. As a first time visitor, I want to easily see the products.
2. As a first time visitor, I want to register and add products to my bag.

### Returning Visitor Goals
1. As a Returning Visitor, I want to check products by categories.
2. As a Returning Visitor, I want to buy products.
3. As a Returning Visitor, I want to be able to access my profile and check my purchase.

### Frequent User Goals
1. As a Frequent User, I want to check new products.
2. As a Frequent User, I want to try my image on the product.

### Admin Goals
1. As an Admin User, I want to delete and edit products.
2. As an Admin User, I want to add more products by category.
   


## Design
### Colour Scheme

- The main colours used are dark grey, white and black, to give the site a clean, modern and professional look.

### Typography

- The Montserrat font is used throughout the website with Sans Serif.

## Existing Features

### Navigation Bar

![Navbar](/media/readme/navbarloggedoff.png)
![Navbar](/media/readme/navbarloginuser.png)
![Navbar](/media/readme/navbaradminlogin.png)

The navigation bar contains links to Home, Log In, Log Out, Register, Profile, Products divided by categories and How it Works. When logged as Admin, Product Management available.

This section will allow the user to have an easier navigation from page to page across all devices without having to revert back to the previous page via the ‘back’ button.


### Footer

![Footer](/media/readme/footer.png)

The footer provides the user links to the social media accounts (Youtube, Instagram, Facebook and Twitter), only used on home page to keep the reset of the site cleaner.

### Home Page

![Home page](/media/readme/home.png)

### Products Page

![Products page](/media/readme/products.png)

### How It Works Page

![How It Works Page](/media/readme/howitworks.png)

### Try Your Design Page

![Try Your Design Page](/media/readme/tryourdesign.png)

### Profile Page

![Profile page](/media/readme/profile.png)

### New Product Page

![New Product Page](/media/readme/newproduct.png)

### Edit Product Page

![Edit Product Page](/media/readme/editproduct.png)

### Register Page

![Register page](/media/readme/register.png)

### Log In Page

![Log In page](/media/readme/login.png)

### Bag Page

![Bag page](/media/readme/bag.png)

### Checkout Page

![Checkout page](/media/readme/checkout.png)

## Frameworks, Languages & Programs Used

### [VSCode](https://code.visualstudio.com/)
- This developer used VSCode for their IDE while building the website.

### [Materialize CSS](https://materializecss.com/)

- Materialize was used to build the NavBar, cards and collapsible itens.

### [Google Fonts](https://fonts.google.com/)
- The project uses Google fonts to style the website fonts.

### [Balsamiq](https://balsamiq.com/) 
- The project uses Balsamiq to create the wireframe mockups.

### [HTML 5](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- Markup language designed to be displayed in a web browser.

### [CSS 3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- Style sheet language used for describing the presentation of a document in HTML.

### [JavaScript](https://www.javascript.com/)
- JavaScript is a scripting language used to create and control dynamic website content.

### [Python](https://www.python.org/)
- Python is commonly used for developing websites and software, task automation, data analysis, and data visualization.

### [Fontawesome](https://fontawesome.com/)
- Icons library and toolkit.

### [Django](https://django.com/)
- Django was used to create the framework.

### [Stripe](https://stripe.com/)
- Stripe was used to accept and authorise payment for any item purchased on the site.

### [AWS](https://s3.console.aws.amazon.com/)
- Amazon S3 was used to manage and save media and static files.

### [Heroku](https://heroku.com/)
- Heroku was used to deploy our app.


## Testing

### Development Testing

-  The Google Chrome Developer tools during the development of the website to inspect the site at different device sizes and in responsive mode.

### Manual Testing

- Navigation Bar
1. When each link on the navbar is clicked, it takes the user to the correct page.

- Social Media Links
1. When each link is clicked, it opens a new tab.
2. When each link is clicked, it takes the user to the correct page.

- Products
1. When submitted a new product is added to the database. 
2. Edit product function was tested multiple times by the developer.

- Log in and Register
1. Log in and Register working according to the pattern defined on code (A-Z, 0-9).
2. When registered, user is successfully added to the database, profile and permissions working accordingly.

- Purchase
1. When the user clicks on purchase, data is loading properly and is added to the database together with stripe process.
2. Add and remove itens from bag manually tested.
3. Webhooks working properly.

- Buttons
1. All the buttons have been tested multiple times.

### Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors in the project.

- W3C Markup Validator

![Markup HTML](/media/readme/htmlchecker.png)

   - Same ID is needed as one occurence is on base.html and the other on mobile-top-header.html.
   - Tested the JS without the type attribute and the application didn't work properly. 

- W3C CSS Validator 

![Markup CSS](/media/readme/csschecker.png)

- PowerMapper 

![PowerMapper](/media/readme/powermapper.png)

## Testing User Stories from User Experience (UX) Section
### First Time Visitor Goals
1. As a first time visitor, I want to easily see the products.
    - At first glance the user can already see the products clicking on Shop Now.
    - The Nav bar contain links to the products divided by categories.. 
  
2. As a first time visitor, I want to register and add products to my bag.
   - Register process is easy and the user can add products to the bag and keep shopping.
   - User can skip to checkout process through a toast window.

### Returning Visitor Goals
1. As a Returning Visitor, I want to check products by categories.

2. As a Returning Visitor, I want to buy products.
    - The user can use the information provided at registration process or in profile, making the purchase process easier.

3. As a Returning Visitor, I want to be able to access my profile and check my purchase.
    - The user can check his information at profile and purchase details.
    - On order details is possible to check order ID, billing address and other important informations.

### Frequent User Goals
1. As a Frequent User, I want to check new products.
2. As a Frequent User, I want to try my image on the product.
    - On try your design, the user can try some text and upload image to test on a t-shirt model.
    - You can resize the image and the text input.

### Admin Goals
1. As an Admin User, I want to delete and edit products.
    - The admin can delete or entirely edit the product.
2. As an Admin User, I want to add more products by category.

### Issues
- Had an issue with Procfile during the deployment to Heroku, file was saved as UTF-16, changed to UTF-8 to fix it.
- Try your Design feature not suitable for mobile.

### Known Bugs

- On old devices, the images can break the layout.
- Products layout can break depending of text size.
- Products image differ in size breaking the layout harmony.

### Future Improvements

- Try your design for mobile, more base products to test it, save button for your created design, posting on user's profile.
- Instead of receiving the user image by email, create a post system or a dashboard where admin and user can interacte.

## Deployment

This project was developed using Visual Studio Code Insiders, committed to git and pushed to GitHub using git bash terminal.

### Deployment to Heroku

The live link can be found here - https://understore.herokuapp.com/

### Deploying on Heroku

The website was deployed to heroku by doing the following:

1. Navigate to heroku.

2. Click "new" and create a new App.

3. Give your app a name, choose your region and Click "Create app".

4. The menus that we are concerned with are "Deploy" and "Settings". Click on "Settings" First.

5. Buildpacks now need to be added. These install future dependancies that we need outside of the requirements file. The first is python and the second is node.js. Select Python first and then node.js and click save. Make sure they are in this order.

6. Then go to the deploy section and choose your deployment method. To connect with github select github and confirm.

7. Search for your repo, select it and click connect.

8. You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes. For this option choose the branch to deploy and click enable automatic deploys. This can be changed at a later date to manual. Manual deployment deploys the current state of a branch.

9. Click deploy branch.

If successful you should be able to view your deployed app by clicking "View".

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps.

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
7. Press Enter. Your local clone will be created.
   
### AWS S3

The AWS account creation and all the process involved was made using the Codeinstitute tutorial and updated PDF version.

## Credits

### Code

- MaterializeCSS was used through the project.
- Authentication methods, connecting to AWS and Heroku codes used from Codeinstitute mini project videos.
- This project is based on Boutique Ado Project, teached by Codeinstitute.
- Try your Design application was based on [oxleberry](https://github.com/oxleberry/) project.

### Media
1. Images were sourced from [Unsplash](https://unsplash.com/).
  
2. All icons were sourced from [Fontawesome](https://fontawesome.com/).

3. Photoshop was used by a graphic designer to make the background (Rodrigo Lorenzo).

4. Deploying on Heroku explained steps from [KSheridan86](https://github.com/KSheridan86).

### Acknowledgements
- [Tim Nelson](https://github.com/TravelTimN) for explaining in a way that makes everything easy.
- Student care and fellow students at Code Institute for their support.
- I would like to thank my friend, Diego Laterza for his help and guidance through the process.
