# Borrow This
A Peer to Peer Rental Community
## Scope:  
Build a web application similar to craigslist, sharegrid, or AirBnB where users can post items for rent and make reservations for those items.  
## User Stories:
- A user creates a profile upon signing up.  This includes a profile image, a bio, and location.  
- A user may browse through items for rent by visiting the browse page.  They can filter by or category or location.
- A user may select an item and visit the item’s detail page.  
- A user may select an item to rent and they are brought to a reservation form page where they can fill out the needed information to rent the item.  They can then submit their reservation.  
- A user may see their reservation on their dashboard page.  They can edit or cancel the reservation.  
- A user may update their information on their dashboard page.  A User may delete their account.  
- A user may choose to add a rental item by clicking on a link in their dashboard page where they will be brought to a form.  On this form they can upload images and all the details about the item they want to rent.
- A user can view their rental items on their dashboard.  They can see if an item is rented or they can change the status of their item to unavailable.  They can delete their item from the website.  
- A User can see past reservations as well.  
- A user can visit another user’s page via a link on a rental item or reservation.
- A user may visit the website and see items for rent but if they are not signed in, they cannot make a reservation.  
##### 1st Stretch:
- A User cannot make a reservation for an item that is already reserved or out.
Image upload for rental items  

### Stretch User Stories:
Rental Items:
- Cancellation Policy
- Late Fees
- Rental Terms (weekends are free etc)
- Minimum Rental Period (reservation won’t submit if minimum is not met)
- Prepped and ready for pick up
- Location
- Invoices Generated based on price and length of reservation
- User can see invoices on their dashboard page
- Reviews for rental items
- Comments for reviews

### More Stretch User Stories:
- Calendar Implementation, book using calendar and block people through calendar
- Model for L and D, Loss and Damages
- Foreign Key for item, order, description of damages.  Repair costs.
- Google Maps implementation for location of items
- Chat feature between users, once a reservation has been placed or if they have questions.
#### Emails sent when
- You sign up
- Your reservation is made
- Someone reserves your item
- When an item is due back


## Technologies:
- Web Framework: Django
- CSS Library: Bulma
- Templates: Django Templating Language
- Database: PostgreSQL
- Heroku for Deployment
- AWS S3 for image storage

## Milestones and Sprints (Due Date Times are EOD):
### Milestone 1: A Finished Looking App - Due Fri Aug 21
#### Sprint 1: Basic Templates and User Sign Up
- Start Repo, Start Django App
- Navbar with links
- Create basic templates based on wireframes with template data
- Home Page
- Browse Items Page
- User Dashboard
- Item Details
- User Info (probably similar to User Dashboard)
- About Me Section
- Basic Styling of templates
- Sign Up Form and Login Form Page
- Create a User account, login and logout.

### Milestone 2: Full Crud - Due Mon Aug 24
#### Sprint 2 - Rental Items
- Add Form to Rental Item Form Page
- Added Rental Items appear on Browse Items
- Added Rental Items appear on Dashboard
- Added Rental Items appear on User’s Public Page
- Rental Items come with their details page
- Rental item has link to the user that posted the item

#### Sprint 3 - Reservations and finish CRUD
- Select item and be taken to reservation form page
- Make reservations by hitting submit
- See reservations on dashboard page, your item or your reservation
- Update and Delete for Rental Items
- Update and Delete for Reservations

### Milestone 3: Validation - Due Tues Aug 25
#### Sprint 4 - Validation and Image Upload
- Image upload for rental items and profile pictures
#### Validation:
- User can only edit their own rental items
- User can only edit their own reservation
- User cannot make a reservation that conflicts with another reservation
- User can browse site without signing up but can’t make reservations. 
- Navbar changes depending on if they are logged in

### Milestone 4: Stretching the Features
#### Stretch Sprint 1 - More Functionality
- Add Categories and Location to Rental Items
- Filter Browse Items page by category and/or by location
- Calendar implementation
- Pop Up calendar for making reservations
- See dates crossed out on calendar for days not available
- Rental Price added to items
- Calculate Total when making reservation
- Total amount for reservations appear on dashboard

#### Final Sprint - Styling
- After feature freeze, finalize styling.
- Deploy to Heroku
- Finalize ReadME
