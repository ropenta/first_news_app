Rohith's News App
-----------------
1. I started by creating and entering a virtualenv
$ virtualenv first_news_app
$ source activate first_news_app
2. You can check your envs with this command:
$ conda info --envs
3. I then created a git repository in machine:
$ git init  <--- this also creates a folder called 'repo'
4. Then I created a public repo in GitHub
https://github.com/new
5. GitHub gave a few commands that would link the local repo with GitHub
$ git remote add origin https://github.com/ropenta/first_news_app.git
$ git push -u origin master   <--- this only matters once a few files are created
6. All files I created on local machine were in the 'repo' folder, now the workflow:
$ git add asdf.ext
$ git commit -m "commit message"
$ git remote add origin https://github.com/ropenta/first_news_app.git  <-- this can be done here or earlier
$ git push origin master  <--- for the master branch
7. Repeat step 6 as needed