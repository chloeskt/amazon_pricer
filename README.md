## Amazon Price Checker

This repo is small Amazon price checker. You can find multiple example of such scraper on the Internet. 
Here is a simple class which will send you an email (USING GMAIL) when the price of the desired object will have decreased on Amazon.

## Installation

To install this project:

```
git clone 
```

## Environment variables

In the `.env.dist` you will find a template of the environment variables you will need for this repo to work: 
```
EMAIL_ADDRESS = the email address used to connect to the GMAIL server
PASSWORD = the password of the previous email account
EMAIL_RECEIVER = the email which will receive the news once the price has decreased (can be the same has EMAIL_ADDRESS or not)
```

## Setup your GMAIL account so that you get App password

You can either hardcode your email and your password (and never commit them!) and in this case, 
you will be to enable the "less secure app access" (see official [documentation](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MJWSdhYTHTPnuN4shURUy9cRAeqC0Quz8ZvZAGtUDCzh63ZUvGur3F4kKnZ8c3f-QHMKXbaI2PxYp51GMIaPrbuz2exg))

Or, if you do not want to hardcode your password, you can create an app-password.
- First you need (recommended) to step the 2-factor authentification (see official Gmail documentation [here](https://www.google.com/landing/2step/)).
- Then you can create an app password and use it has `PASSWORD`. On the official page, you have to select `Mail` 
in the "Select app" in the text field, and then choose the corresponding device your script will run on. See [documentation](https://support.google.com/mail/answer/185833?hl=en).

