This project will take the .mbox file outputted from google takeout and turn it into daily problems folders for personal solution repo. I'm always behind, so I there are quite a few to catch up on..

Ideas on formatting of mbox:
starts with From:
ends with NmP line?
some emails are spam, so need to filter the subject for "Daily Coding Problem..."

found some python starter code for going through each email.
To get the subject(for the number), I can just go to the first instance of 'Subject: '
Then, probabably skip until Good Morning!, assuming they don't change that intro, I can use that to grab the important part up to ----------------------------------------------------
then the rest doesn't matter
