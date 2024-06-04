# adk8cy_DS5111su24_lab_01
## LAB 1: DS 5111 Data Engineering Fall 2023

In this lab, you will gather materials from project gutenberg as simple text.  You will set up an automate way to download content, do some very basic operations to count words etc, and put all that in a repository so that someone else can retrace your steps with just one command.  They should also be able to expand, or pause the automation at certain steps to rerun parts of it.  The downloaded data should NOT save to the repo.  When someone clones your repo and runs it, the data should be downloaded from scratch (to save pushing around all the data)

# Lab 1 Instructions
Please read THROUGH ALL the instructions before you start, because only some of the files we use will be commited in your repository

Before we get going, let's update the package manager on your linux box.  
- `sudo apt update #` This is usual and necessary on new instances, but you don't have to do it every time you start, only if you terminate and start a whole new box

## Creating a repository ( 1 point)
- In your github account, create a repository with the name <UVA ID>_DS5111su24_lab_01, this is important since we'll automate some of the process.
- Make sure the repository is public
- Add EfrainOlivaresUVA and MiaHanzhangYuan as collaborators. https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repositoryLinks to an external site.
- On your AWS linux box, clone your repository so you can save your work

## Create a branch for your work.  (3 points)
Using the command line in the repo you just cloned you will create a branch for your work and push it up to github.  This is how we will communicate on your work.
- Create a new branch named project_gutenberg_texts and push that to github.
- The rest of your lab work should get checked into and pushed to this branch
 

### Sidebar: Project Gutenberg Project

This web page https://www.gutenberg.orgLinks to an external site. provides the text of many books that no longer have copyrights.  They include a LOT of the classics.  There are several formats you can download the text in.  They are variations of text formats.  We’ll be using the most plain of them all, just a simple txt.

Just like we did in class, you will gather the id’s of 10 books by Edgar Allan Poe.

## Makefile setup (2 pts)
- Create a  makefile and setup a default: task as shown in the lecture demo, so it just cats the makefile itself
- Create a job called `get_texts'` which should download (wget) the content.
- The easiest way to do this once you have the id of a book, is to use the wget command as shown in class `wget https://www.gutenberg.org/cache/epub/17192/pg17192.txtLinks to an external site.`

Running the `make get_texts` should download the set of files you’ve selected.

### (2 extra points)

You get two points for this part if you wrote a line per book.  However, there is another 2 points if you create a file and loop through the book id’s to make it easier to expand.  The makefile job should then run the script, as in `bash get_the_books.sh`

## .gitignore to exclude `.txt.` files (2 pts)
Since we do NOT want the data in the repository, at this point create a .gitignore, or update the existing one to insure that *.txt files to not get seen or committed by git.   Check in your .gitignore so that it becomes part of your project

## Processing Your Data:
url to The Raven txt: https://www.gutenberg.org/cache/epub/17192/pg17192.txtLinks to an external site.

Note that all these should be jobs in your makefile and output to console

- 1 pt: raven_line_count  Write a script that uses `wc` to count the number of lines in The Raven
- 1 pt: raven_word_count: How many words are there in the raven, use wc again.
- 1 pt: raven_counts: How many lines in The Raven have the word ‘raven’ in it.  This one should output counts for raven (lowercase), Raven (title case), and a count where case is ignored.
- 2 pt:  total_lines: how many lines are in all the files you downloaded?
- 2 pt: total_words: how many words are in all the files you downloaded?

## Creating a Pull Request PR (1 pt)
When you have some work started, create a Pull Request to merge your code into main.  Request a review from myself and Mia.  At the end of the lab we’ll merge your work into the main branch.

## Round Trip
By round trip here I mean how your repo performs when some one else checks it out, and runs make.  Did all the jobs run right out of the box?

Please note all the names of the makefile jobs and the names of the repo.  I will automate a git pull and running of the jobs.  And remember your repo should not have the data or the answers in it.  I should be able to git-pull, cd into the repo, and run the makefile jobs one after the other to see the results with no extra work.

This last part is worth 5pts
