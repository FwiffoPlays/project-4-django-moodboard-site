## Functional Testing

**Authentication**

Description:

Confirm that a user can create a new account on the site.

Steps:
1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and when logged out, click the 'register' button on the navbar.
2. Fill in at least a username and password in the form
3. Click submit

Expected:

A new account is successfully created, with its details being added to the users table of the database.

Actual:

A new account is successfully created, with its details being added to the users table of the database.

Description:

Check that a user can log in to a valid account

Steps:
1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and when logged out, click the 'login' button on the navbar.
2. Fill in the login details of the previously created user.
3. Click login

Expected:

The user is now logged in to the site and redirected to the home page

Actual:

The user is now logged in to the site and redirected to the home page

Description:

Confirm a user can sign out of their account

Steps:

Steps:
1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and when logged in, click the 'logout' button on the navbar.
2. Click the 'sign out' button on the confirmation page.

Expected:

The user is logged out and redirected to the home page.

Actual:

The user is logged out and redirected to the home page.

**Create Moodboard**

Description:

Test that the user is able to successfully create a moodboard on the site when logged in.

Steps:

1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and when logged in, click the 'create moodboard' button on the navbar.
2. Fill in at least the title and upload at least one image.
3. Click the 'create moodboard' submit button.

Expected:

The moodboard is added to the site and now viewable on the home page and able to be searched for.

Actual:

The moodboard is added to the site and now viewable on the home page and able to be searched for.

**Edit Moodboard**

Description:

Test that the user is able to edit a moodboard they have rights to.

Steps:

1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and when logged in, click on the moodboard you have created.
2. Click the 'edit' button at the top right of the page.
3. Change some content on the form, such as uploading different images or editing the title/description.
4. Click submit

Expected:

The changes are applied to the correct moodboard and are live on the site.

Actual:

The changes are applied to the correct moodboard and are live on the site.

**Delete Moodboard**

Description:

Test that the user is able to delete a moodboard they have rights to.

Steps:

1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and when logged in, click on the moodboard you have created.
2. Click the 'delete' button at the top right of the page.
3. Click 'ok' on the confirmation prompt.

Expected:

The correct moodboard is removed from the site and is no longer accessible or able to be searched for.

Actual:

The correct moodboard is removed from the site and is no longer accessible or able to be searched for.

**Search**

Description:

Test that the user is able to search for a moodboard based on its title, tags or description.

Steps:

1. Go to the [site](https://ci-project-4-django-moodboards.herokuapp.com/) and in the searchbox within the navbar, type a query that will match at least one moodboard on the site, such as 'test'
2. Click 'search'

Expected:

The moodboards shown on the home page are filtered according to the user's search query.

Actual:

The moodboards shown on the home page are filtered according to the user's search query.

