# BITS issue_tracker

This project comprises an issue tracker full stack web application incorporating different apps to provide a range of functionality. The application integrates a tracker list containing a list of bugs and features with other applications. The tracker list consists of a summary list of issues with which various users can interact with, the degree of interaction relative to the level of permission, on authentication. Authorised users at minimum can create their own bugs and features and follow their development through the ability to comment and post blogs. A search app allows users to search the summary list by name. Authentication is through the use of an accounts app, where users either sign in or register. Template logic is used to allow the users access to various features subject to their level of permission. Staff users have further permissions to edit items while superusers have full permissions. An e-commerce functionality is provided through the use of cart and checkout apps with the stripe application used to handle payments. At least 50% of time is spent developing the highest paid features, with the remaining time spent fixing bugs for free. Upvoting is incorporated into the issues_list app for bugs (free upvote) and the cart and checkout apps for features (upvoted for a fee). A chart app provides transparency to users on time spent working on bugs and features. Non-authenticated users can access the home, about and activities pages to read about BITS and sign up if they desire so. A documents page is also provided providing information on the features, site navigation and use of forms to add data.
 
## UX
 
### Strategy: ###

#### Problem Definition 

In order to fulfill brief requirements the issues to be sorted are defined as:
Build  an issue tracker web app offering bug fixes and features. In doing so:
* Provide ticket functionality to allow users to create tickets
* Provide ticket functionality to allow users to comment on tickets
* Provide ticket functionality to show the status of tickets  (e.g. ‘to do,’ ‘doing,’ or ‘done’). 
* Bug ticket issues are fixed for free
* Provide upvote functionality to prioritise ticket issues
* Feature ticket issues involve e-commerce functionality (developed for a fee) paid on upvote. Highest paid up takes precedence.
* Provide visual transparency showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.
* Provide optional additional functionality such as a blog page
* Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
* Include an authentication mechanism, allowing a user to register and log in.
* Provide a description of the application.
* Provide documentation for the application.

Bugs and features can be present across the full spectrum of specifications, design, code and end product. Thus issues are not directly limited to a coding context only,  meaning the end-user of this product may be an individual or business user involved in any form of business or activity. Consequently a full proof management system enabling identification, prioritisation, assignment, processing, resolution and review of raised issues can apply to any line of work. An issue tracker focuses on resolution of issues with emphasis on accountability and progress, thereby ensuring that the work gets done, correctly. The intention is to have a community of users involved in driving the site and as the work is driven by how popular an issue is (upvote), consensus will ensure that work carried out is relevant and desirable. A competitive edge is maintained by only charging a nominal sum to carry out work on the most popular feature. At least 50% of time is spent on developing features with the remaining time spent working on bugs (free solutions).

A typical user profile would include team project managers who need a structured way to enable their team to raise and address issues within their projects. Small companies may not feel the need to design their own trackers if there is a plethora of companies already offering tracking solutions and thus would look externally for a solution. Even large companies may trawl the web in search of solutions difficult to solve in-house. Using outsourced solutions may also offer more flexibility and diversity than an in-house system.
The intention is to have a multidisciplined team with expertise in several other fields as well as software know-how. While this broadens the scope of the company it also widens the potential market of users.

#### User stories include: ####

- As a user of an issue tracker site I want a safe safe and reliable method for my team to raise issues
- As a user of an issue tracker site I want adequate transparency and accountability to ensure issues are dealt with professionally
- As a manager I want to my team to be be part of a well informed interactive online community participating in addressing issues raised by the community. 
- As a small company manager I want to outsource issues and participate in solutions with the community.
- As an interested party I want to use a site where issues are easily prioritised and pushed
- As an interested party I want to use a site to push for features to be developed by a motivated partner

### Scope: ###

Considerations to address include, who deals with issues and where? What was agreed in relation to the issue and when was it agreed? How important is it? What is the solution and who is responsible for it? What is the outcome and is it relevant? 
A simple issue tracker will be used combining both bugs and features, with the most popular issues, by upvote being prioritised. Authentication and authorisation is required as a security measure. In addition users need to be registered to persist their shopping cart between sessions. Users need to be allowed to create and comment on tickets. Other users also need to be allowed to create and edit models in the backend. Some form of graph is required to provide visual transparency on showing how many bugs or features are tended to and what is the upvote status is. A blog page is required to provide further interaction. Description and documentation pages are also required to inform users.
A landing page image is considered as is a brand logo. Fundamentally it is an information based activity and thus a functional way of presenting and accessing the data is required. Tables and simple but familiar form types are necessary. Background color is required to break the monotony of text and text itself can be intuitively coloured. Where possible icons can be used to portray meaning. 

### Structure: ###

Being a django based application the app fundamentally comprises a series of apps. Different links specific to the app function are provided where necessary to provide functionality and interactivity specific to the app being used. The intention is to create meaningful relationships between these apps as the user navigates the site. Main navigation elements are  provided conventionally (horizontally at the top of the page) and remain consistent throughout in form and function. They allow allows users to efficiently move through content. Buttons or links provide further navigation where necessary. Familiarity is induced by ensuring themes, content and imagery have a stable consistent style. Information is grouped into familar categories.Template logic is required to ensure authenticated users are catered for differently to a general peruser.  Authorisation is implemented through the use of permissions. 
A simple minimalistic page structure facilitates a mobile first approach while ensuring there is scope for growth and change to allow the site to evolve as more content is added.

### Skeleton: ###

The users navigate through the site through navigation menus, links and buttons. Navigation remains conventional throughout to cultivate familiarity and to promote a positive user friendly experience. Specific content is further built on through the specific link and progressive disclosure in conjunction with similar expression of  similar parts, ensures consistent perception throughout the site. The information is revealed  across a number of pages through the use of simple features and minimal clicks. Navigation is enhanced through the  use of representational icons that are conventional and visible.  Being familiar objects they are easily understood  and provide clear meaning to all users. Similar icons on different pages induce the same positive user experience.  Keyword searches and filters are used to manipulate the data in the backend and front end. Pagination is used to quickly cycle through data on the front-end.
Pencil wireframe was used to plot a two-dimensional model of the perceived end product. These static diagrams represented the content, navigations and interactions in a meaningful visual format. The wireframes are included with the project and located in the additional_info folder in the static directory.

### Surface: ###

Varying degrees of the color palette blue are chosen to represent the front-end background colors. Blue is favoured by both men and women and represents trust, professionalism and a business-like manner. Blue is also generally associated with scientific/technical type information and information technology (examples are: samsung, linkedIn, facebook, twitter, cloud9). The blue theme is also consistent with the default Django admin panel.
The background colors are kept consistent throughout the site. The main navigation bar and footer are the same on all pages. All forms are consistent in layout and color. The detail view for the issues and blog posts also keep this consistency. Across all pages button colors and styles are consistent. Comment buttons and icons for example are always orange. Submit form buttons are a custom grey. Button hover effects are also consistent. The colors on the charts are also consistent with bugs and features being represented by different shades of blue. The issue list uses the bootstrap success, warning and danger color styles to visually represent completed, ongoing and pending (i.e. the status) items respectively and these colors are carried into the charts where status is represented. Fonts are consistent so that, for example, header text is generally of exo style with paragraph content being of font style roboto. Both bootstrap and font-awesome icons are used. Icons are intuitive, in that, the thumbs-up icon represents upvoting and the shopping cart icon represents the cart, etc. Panels are also consistent in form and layout. Outer panels have a solid border to delineate between features and inner panels have transparent borders. 
There is progressive disclosure in the sense that clicking on a link or icon in the summary issues list takes you to more detail on that particular issue. In the detail view, further action can be taken. For example comments can be viewed or items can be upvoted and commented on.  Clicking on a link in the about page takes the user to the docs page. The read more button in the blog post list page, takes the user to a more detailed view where other actions such as commenting or editing can be done. Within the detail views, links are provided back to the previous view, thus mitigating against the use of the browser back button.  
Other navigation includes the use of a search bar allowing search by name. The tracker list page has forward and reverse pagination allowing pages to be cycled through without the use of scrolling or use of the browser back and forward buttons. All form pages have a back to button with text and icon, ensuring a user does not need to use the browser back arrow to escape from a form page if they change their minds.
Django messaging is used to enhance the user experience. A message will flash at the top of the page on successful login or logout. A message will also flash to indicate if an upvote was added in the case of a bug. If a user has already upvoted a bug, a message will flash to the user indicating that they have already voted that bug. In the case of features a message will inform users that payment has been received and upvotes added. Conversely error messages will inform the user if payment cannot be received or if login cannot be achieved. Tooltips are also used to enhance the user experience. They are used in the issues list on hover over icons and links to give instruction. The charts also reveal quantities on hover over a pie slice or chart bar (in desktop mode).
Template logic is used to reveal or hide various elements depending on user permissions. General authorised users do not have full CRUD permissions unlike staff. The general user can add items, upvote, post blogs and comment. Icons for upvoting and commenting are present for general authorised users. However as general authorised users cannot edit items, these icons only show when staff are logged in. Within the staff group superusers (admin1 and admin2) have full CRUD permissions in the admin panel and the browser. However deletion can only occur in the django admin panel at present. 3 senior staff members also have full CRUD permissions with 2 more junior staff having create, read and edit permissions. All staff also have access to the django admin panel.
Bootstrap is used as the main front-end framework, having ready made HTML and CSS based design templates for typography, forms, buttons, tables and navigation. Bootstrap also gives the ability to easily create responsive designs. Semantic elements are used in the html pages thus describing meaning to the browser and developer. Semantic elements such as form, table, section, navbar, etc clearly define the content. Classes are applied to quickly add bootstrap styles or build custom styles and enhance bootstrap styles as is the case with the buttons. The main issue table uses the bootstrap responsive class giving it a neat and scrollable form on smaller screen sizes. Many of the bootstrap ready made classes are used in the application. Classes like text-center, btn btn-sm, table-responsive, text-muted, etc are used to quickly style elements. A substantive custom css stylesheet (style.css) is also used to provide styles not present in bootstrap, to further enhance bootstrap styles and in some cases to overwrite bootstrap styles, where anothe style is preferred.
The dc.js charting library with crossfilter is used to render graphs, being very efficient in manipulating json type data and allowing for user interaction.
Data is mostly processed in the back end, in some cases employing filters, and either read directly into the templates or returned in json format for use in graphs. There are some calculations within the graph function in one script file to return durations in days. There are also some simple functions to return quantities.
In the backend choice fields where appropriate are used so the user just needs to select an option, ensuring theses fields will always have similar type data. For example a category will always either be a bug or a feature. Status will always be one of completed, ongoing or pending. A specific date format is also requested in the input date fields. Helper text suggests what needs to be inputted. Anything other that what is requested throws up a date invalid error.
For further information refer to the documentation within the application, accessible by clicking the link on the navbar. (the mile5Notes.pdf file in the additional info folder in the static directory also includes more abstract information on project approach.)

## Features

The features are listed below. More detail on the features can be found in the documentation within the application.
 
### Existing Features

- Feature 1 - An accounts app allowing users to either sign in or register to use the application.
  Users and permissions are discussed further in the documentattion.
- Feature 2 - An home app allowing all users even non-authenticated users to get a flavour of what goes on.    There is a home (landing page), an about page, an activities page and the docs page. Non-authenticated       users will see slightly different items on the home and docs pages.
- Feature 3 - A blog app allowing authorised users to post a blog or comment on a blogs.
- Feature 4 - A cart app which allows users to upvote the various features and retains the items until         either payment is made or the user is logged out. It uses a context to ensure contents are available on all   pages. 
- Feature 5 - A chart app to visually represent data returned from the backend in relation to numbers of bugs   and features dealt with over a period of time.
- Feature 6 - A checkout app that facilitates payments for upvoted features. Stripe a javascript based         API is used to securely process payments. Customer details are saved to the db.
- Feature 7 - A tracker issues_list app which takes stock of all bugs and features and provides an interface   for all authorised users to interact with the various items, to provide CRUD opeations subject to user       permissions. It also includes comment functionality. This app is outlined in detail in the docs.
- Feature 8 - A search app which uses the django filter capability to text search an item by name. 
- Feature 9 - Quick and easy navigation using pagination, search bar, anchor links and buttons.

### Features Left to Implement

- The accounts app can be developed to allow administrators to reset lost passwords. 
- More graph views can be established to show hourly durations on activities for example.
- Functionality to provide notifications on projects, issues assigned, status changes, due dates, etc would be a useful enhancement.
- Reporting mechanism allowing for the issue of reports as PDF, Word or Excel files.
- email support so that when a user has complex questions, detailed answers are supplied via an email support system.

## Technologies Used

In this project the following technologies were employed:

- [django](https://www.djangoproject.com/)
    - The project uses **django 1.11.16** as the main fully featured server-side web framework.
- [django_forms_bootstrap](https://django-bootstrap-form.readthedocs.io/en/latest/)
    - The project uses **django_forms** to fire django forms in the settings.py and bootstrap tags in the html.
- [django_vote](https://django-vote.readthedocs.io/en/latest/)
    - The project uses **django_vote** app to facilitate the use of upvoting.
- [pillow](https://pillow.readthedocs.io/en/5.3.x/)
    - The project uses **pillow** to facilitate the use of images in the application.
- [bootstrap](https://getbootstrap.com/docs/3.3/getting-started/)
    - The project uses **bootstrap3** to theme and style the html pages. Bootstrap glyphicons are also used for upvotes, editing and comments.
- [fontawesome](https://fontawesome.com/v4.7.0/)
    - The project uses **fontawesome** icons for shopping cart and users
- [stripe](https://dashboard.stripe.com/)
    - The project uses **stripe** API as the credit/debit card payment mechanism.
- [dc.js](https://dc-js.github.io/dc.js/)
    - The project uses **dc.js crossfilter** to render json type data received from the backend into graphs. 
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to fire tooltips and to link up django forms to the stripe API.
- [![Build Status](https://travis-ci.org/vmcggh18/bits_tracker.svg?branch=master)](https://travis-ci.org/vmcggh18/bits_tracker)
    - Travis Continuous integration testing

## Testing

The Django test case framework has been used to write some tests (64 in total across all apps) for the various model, form and views.py files within each app. The test files are easily identifyable being prefixed with test_.
After writing some tests coverage was installed to see the extent of testing in the local ide.
For example use the *coverage run --source=issues_list manage.py test* command to run the tests for the issues-list app. To run the tests for a different app use the above command but change the app name.
After running the test, typing *coverage report* in the command line shows the coverage for that particular app rather than the whole system.
The *coverage html* command generates a new folder where files can be inspected to pinpoint where additional tests may be required.
Travis continuous integration testing through the github repository is also used.
In addition to automated testing, extensive manual testing was carried out to ensure that the requirements of the brief were adequately addressed.
For example entering a wrong username during login gives a "Your username or password is incorrect" error. Entering an incorrect email address format during registration gives a "Enter a valid email address" error and entering differing passwords gives a "Passwords must match" error.
When upvoting a feature, if 0 is used, a message comes up stating that "A" value must be greater than or equal to one".
While testing stripe 4242424242424242 was used as a visa card number and 111 as the CVC number to make a valid payment. Typing 4242424242424241 for example returns 'Your card number is incorrect.' Typing 4242424242424242 but 11 for the cvc number returns 'Your card's security code is invalid.'
The app was fully tested on chrome and firefox for responsiveness and performed similarly well in both browsers. It worked fine in microsoft edge desktop mode but the emulation panel would not open to allow testing of different browser profiles. Microsoft edge kept throwing up a this page cannot open error. This was true while trying to view any website page in emulation mode, indicating a problem with microsoft edge. The application did appear responsive while resizing the browser window in desktop mode. The app was also directly tested using a samsung S5 and all pages with the exception of chart pages were fully responsive. However the charts being compact bar and pie charts render reasonably well on smaller screen sizes. The issue tracker list is a responsive table in that it can be horizontally scrolled to view all columns on smaller screen sizes. During testing it was noticed that some of the form pages were not fully responsive but adding a container-fluid class to the form resolved this. 
Chrome was used to develop the application and chrome developer tools was useful in pin-pointing elements where styles could be experimented with and then adopted. It was particularly useful in tracing bootstrap styles that needed to be overridden. The form width was chosen as 75% to cater for smaller screen sizes and then a media query used to reduce the width further to 50% on larger screen sizes. During development there was an issue loading the graphs into the activities page. Sometimes the page needed to be refreshed to load all charts. While charts on the charts page were all loading there seemed to be conflict between the 2 chart javascript files. This was resolved by taking both files out of the base html file and loading them from their respective html files. The developer tool also facilitated testing for different device sizes such as ipad, pixels, samsung and iphone. The width upvote input form for example needed to be widened to cater for tablet sizes such as ipad and kindle. On these devices it was difficult to see the inputted number of upvotes as the form was squeezed into a line with other link buttons rather than being stacked as on smaller screen sizes.
Some of the errors encountered during development and testing of the application and their solutions have been written into the tracker list as part of the bugs list. 


## Deployment

This project was depoyed to Github and Heroku. A repository was set up in Github and the following commands used to push it from the ide (cloud9) to github, git remote add origin (https://github.com/vmcggh18/bits_tracker.git) and git push -u origin master
On github the repo can be downloaded as a zip file for installation into a local ide or cloned to receive the full commit history.  When installed locally, ensure any dependencies needed to run it are installed, by checking the requirements.txt file. Use the django secret key generator to generate a secret key and save it to the env.py file stored in the local ide. To use stripe functionality the secret keys for this also need to be obtained and saved to the env.py file. When running locally ensure the the env file is imported into the settings.py file. Then just type run to view in the browser.      
Alternatively the working application can be viewed at (https://bits-tracker.herokuapp.com/).
A new app called bits-tracker was created in heroku. In resources a postgres add on was created giving a database url in the config vars in settings. This url was copied for use in the env.py file and linked to the settings.py file using an environment variable. 2 packages were installed (sudo pip3 install dj-database-url was used to enable connection to a database url in heroku) and (sudo pip3 install psycopg2 installed a package allowing connection to a postgresql database). These dependencies were added to the requirements.txt file. The database was imported into the application using import dj_database_url in the settings.py file. In the database section of the settings.py file, the following line was added: DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }. A requirements.txt file was installed to the root directory, listing the dependencies and allowing heroku to build the application when deployed to heroku.
The mile5Notes.pdf file in the additional info folder in the static directory, outlines the methodology adopted in wiring the application up to the aws cloud server.
For deployment on Heroku the secret key variables were added to the config variables in the app settings. Then click deploy, github and search for app. Once found click connect. sudo pip3 install gunicorn installs a package which allows the application to connect to heroku. Then update the requirements.txt file. Ensure the Procfile has been created in the root directory so that heroku knows the type of application being received. Set DISABLE_COLLECTSTATIC to 1 in the config variables to prevent heroku uploading static files. Ensure the heroku app name is added to allowed hosts in the settings.py file. Click deploy, deploy branch to build.



## Credits

### Content
The following documentation was consulted for ideas on writing the about page 
- [Mindtools Z](https://www.mindtools.com/pages/article/newPPM_69.htm)
- [Sifter](https://sifterapp.com/academy/overview/why/)

### Media
The images used in this site were obtained from:

- [Landing-page image](https://www.pexels.com/photo/group-hand-fist-bump-1068523/)
- [Free use license link](https://www.pexels.com/photo-license/)
- [Logo-image](https://pixabay.com/en/bug-animal-nature-windows-162019/)
- [admin1 image](https://pixabay.com/en/man-avator-person-admin-161282/)
- [admin2 image](https://pixabay.com/en/user-person-people-profile-account-1633249/)
- [Staff 01 image](https://pixabay.com/en/head-man-portrait-face-big-40119/)
- [Staff 02 image](https://pixabay.com/en/cartoon-child-comic-characters-face-2026702/)
- [Staff 03 image](https://pixabay.com/en/girl-illustrate-portriat-design-3405035/)
- [Staff 04 image](https://pixabay.com/en/caricature-head-male-man-portrait-157235/)
- [Staff 05 image](https://pixabay.com/en/bald-bald-man-caricature-comic-man-1295928/)
- [user01](https://pixabay.com/en/avatar-boy-cartoon-comic-human-2027366/)
- [user02](https://pixabay.com/en/woman-girl-avatar-female-pretty-159169/)
- [user03](https://pixabay.com/en/avatar-icon-document-entrepreneur-1789663/)
- [user04](https://pixabay.com/en/avatar-cartoon-eyes-female-funny-2026510/)
- [Use of django logo](https://www.djangoproject.com/trademarks/)
- [Use of postgresql logo](https://www.postgresql.org/about/licence/)
- [Adaptability image](https://pixabay.com/en/businesswoman-business-puzzle-2822607/)
- [Cost-effective image](https://pixabay.com/en/triangle-quality-time-cost-3125882/)
- [Transparency & Accountability image](https://pixabay.com/en/accounting-statistics-excel-finance-1928237/)
- [Knowledge sharing image](https://pixabay.com/en/smartphone-hand-photomontage-faces-1445489/)
- [Management Framework image](https://pixabay.com/en/whiteboard-strategy-diagram-849803/)
- [Creative Commons license link](https://pixabay.com/en/service/terms/#usage)

### Acknowledgements
- The sources below provided inspiration for this application:

#### Code Institute 
- Code Institute Modules (1 -9), in particular Module 9 Full Stack Development
- Haley of Code Institute Tutor Support for assistance in solving bugs relating to rendering of graphs and navbar.

#### Other Documentation Consulted ####
- [Django Documentation:](https://www.djangoproject.com/start/overview/)    
    - Overview of django. Django pagination, chaining of filters, testing.
- [Other pagination:](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html )
    - Django pagination
- [Moderating Comments](https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/)
    - Moderating comments to be approved or deleted

  