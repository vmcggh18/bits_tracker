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

Varying degrees of the blue palette are chosen to represent the front-end background colors. Blue is favoured by both men and women and represents trust, professionalism and a business-like manner. Blue is also generally associated with scientific/technical type information and information technology (examples are: samsung, linkedIn, facebook, twitter, cloud9). The background colors are kept consistent throughout the site. The main navigation bar and footer are the same on all pages. There is progressive disclosure in the sense that clicking on a link or icon in the summary issues list takes you to more detail on that particular issue. Comments can also be viewed  or items can be upvoted or commented on.  In the detail view, button colors and styles are consistent with similar type buttons on other pages. Fonts are consistent and icons are intuitive. For example header text is generally of exo style with paragraph content being of font style roboto. Form layout is standard throughout.

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

### Features Left to Implement

- The accounts app can be developed to allow administrators to reset lost password. 
- Comment approval has been set up in the models and needs to be implemented so that inappropriate comments    can be deleted.
- Functionality to provide notifications on projects, issues assigned, status changes, due dates, etc would    be a useful enhancement.
- Reporting mechanism allowing for the issue of reports as PDF, Word or Excel files.
- email support so that when a user has complex questions, detailed answers are supplied via an email support   system.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
- [django](https://www.djangoproject.com/)
    - The project uses **django 1.11.16** as the main fully featured server-side web framework.
    - 
- [django_forms_bootstrap](https://django-bootstrap-form.readthedocs.io/en/latest/)
    - The project uses **django_forms** to fire django forms in the settings.py and bootstrap tags in the html.
- [bootstrap](https://getbootstrap.com/docs/3.3/getting-started/)
    - The project uses bootstrap to theme and style the html pages (buttons)
- [fontawesome](https://fontawesome.com/v4.7.0/)
    - The project uses fontawesome icons for shopping cart
- [stripe](https://dashboard.stripe.com/)
    - The project uses **stripe** API as the credit/debit card payment mechanism.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to fire tooltips and to link up django forms to the stripe API.


## Testing

Django test case framework has been used to write some tests. The additional notes describe the use of coverage..........
Try, except............nducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet. (graph, burger bar,) Some bugs alrady listed in the tracker list.....

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements
- I received inspiration for this project from X