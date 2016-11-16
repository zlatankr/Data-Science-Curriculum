# Git Workflow

### Setting up environment

- `git config -global user.name "zlatankr"`: set the user name
- `git config -global user.email "zlatankr@gmail.com"`: set the email
- `git config --list`: view all the current settings

To connect to a repo:
- `git clone [paste the repo URL]`: clones repo into current directory
    - _Note:_ you still have to enter into this directory once you've created it 

...or you can link your working directory to an online repo with:
- `git init`
- `git remote add origin [paste repo URL]`

To see what the origin is linked to:
- `git remote -v`

To remove the existing remote repository link:
- `git remote rm origin`

### Pushing and pulling basics

Before beginning work, make sure your local directory is synced with the master branch in your remote repo:
- `git pull origin master`

If you get this error, "your local changes to the following files would be overwritten by merge," then try:
- `git checkout HEAD^ [file to overwrite]`

If you get this error, "the following untracked working tree files would be overwritten by merge," then try:
- `git add *`: this is the same as `git add .`, except it excludes file names that start with a dot
- `git stash`: use when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. The command saves your local modifications away and reverts the working directory to match the HEAD commit.
- `git pull`

Once you are ready to add files to source control:
- `git add .`: adds everything in the directory to source control
- `git add -u`: adds only the files that are already tracked
- `git add -A`: only takes into account any deletions

To commit these changes into the log:
- `git commit -m "[message]"`: make sure you write the change summary in the message

- `git status`: inspects the contents of the working directory and staging area
- `git diff`: shows the difference between the wroking directory and the staging area
- `git log`: shows a list of all the previous commits

...or you can break the process into a fetch followed by a merge:
- `git fetch`: fetches work from the remote into the local copy
- `git merge origin/master': merges origin/master into your local branch

To push all your commits to the remote directory:
- `git push origin master`

### Additional resources:
- Posting to Github using Gitbash:https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD 
- Git documentation: https://www.kernel.org/pub/software/scm/git/docs/git-add.html
- From the Git site: https://git-scm.com/doc