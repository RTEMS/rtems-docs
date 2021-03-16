.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project


Software Development (Git Users)
********************************

.. COMMENT: TBD - Convert https://devel.rtems.org/wiki/Developer/Git/Users to
.. COMMENT: TBD - Rest and insert here.

.. COMMENT: TBD - Managing a (private/public) Git mirror, using GitHub,
.. COMMENT: TBD - submitting pull requests...

Browse the Git Repository Online
--------------------------------

You can browse all available repositories online by
accessing https://git.rtems.org/.

Using the Git Repository
------------------------

The following examples demonstrate how to use the RTEMS' Git repos. These
examples are provided for the main rtems module, but they are also valid
for the other modules.

First, we need to obtain our own local copy of the RTEMS Git repository:

.. code-block:: shell

  git clone git://git.rtems.org/rtems.git rtems

This command will create a folder named rtems in the current directory. This
folder will contain a full-featured RTEMS' Git repository and the current HEAD
revision checked out. Since all the history is available we can check out any
release of RTEMS. Major RTEMS releases are available as separate branches in
the repo.

To see all available remote branches issue the following command:

.. code-block:: shell

  git branch -r

We can check out one of those remote branches (e.g. rtems-4.10 branch) using
the command:

.. code-block:: shell

  git checkout -b rtems410 origin/4.10

This will create a local branch named "rtems410", containing the rtems-4.10
release, that will track the remote branch "rtems-4-10-branch" in origin
(git://git.rtems.org/rtems.git). The ``git branch`` command prints a list of
the current local branches, indicating the one currently checked out.

If you want to switch between local branches:

.. code-block:: shell

  git checkout <branch-name>

With time your local repository will diverge from the main RTEMS repository. To
keep your local copy up to date you need to issue:

.. code-block:: shell

  git pull origin

This command will update all your local branches with any new code revisions
available on the central repository.

Making Changes
--------------

Git allows you to make changes in the RTEMS source tree and track those changes
locally. We recommend you make all your changes in local branches. If you are
working on a few different changes or a progression of changes it is best to
use a local branch for each change.

A branch for each change lets your repo's master branch track the upstream
RTEMS' master branch without interacting with any of the changes you are
working on. A completed change is emailed to the developer's list for review
and this can take time. While this is happening the upstream's master branch
may be updated and you may need to rebase your work and test again if you are
required to change or update your patch. A local branch isolates a specific
change from others and helps you manage the process.

First, you need to clone the repository:

.. code-block:: shell

  git clone git://git.rtems.org/rtems.git rtems

Or if you already cloned it before, then you might want to update to the latest
version before making your changes:

.. code-block:: shell

  cd rtems
  git pull

Create a local branch to make your changes in, in this example, the change is
``faster-context-switch``:

.. code-block:: shell

  git checkout -b faster-context-switch

Next, make your changes to files. If you add, delete ormove/rename files you
need to inform Git

.. code-block:: shell

  git add /some/new/file
  git rm /some/old/file
  git mv /some/old/file /some/new/file

When you're satisfied with the changes you made, commit them (locally)

.. code-block:: shell

  git commit -a

The ``-a`` flag commits all the changes that were made, but you can also
control which changes to commit by individually adding files as you modify
them by using. You can also specify other options to commit, such as a message
with the ``-m`` flag.

.. code-block:: shell

  git add /some/changed/files
  git commit

Create a patch from your branch, in this case, we have two commits we want to
send for review:

.. code-block:: shell

  git format-patch -2

 There are new changes pushed to the RTEMS' master branch and our local branch
 needs to be updated:

.. code-block:: shell

  git checkout master
  git pull
  git checkout faster-context-switch
  git rebase master

Working with Branches
---------------------

Branches facilitate trying out new code and creating patches.

The previous releases of RTEMS are available through remote branches. To check
out a remote branch, first query the Git repository for the list of branches:

.. code-block:: shell

  git branch -r

Then check out the desired remote branch, for example:

.. code-block:: shell

  git checkout -b rtems410 origin/4.10

Or if you have previously checked out the remote branch then you should see it
in your local branches:

.. code-block:: shell

  git branch

You can change to an existing local branch easily:

.. code-block:: shell

  git checkout rtems410

You can also create a new branch and switch to it:

.. code-block:: shell

  git branch temporary
  git checkout temporary

Or more concisely:

.. code-block:: shell

  git checkout -b temporary

If you forget which branch you are on

.. code-block:: shell

  git branch

shows you by placing a * next to the current one.

When a branch is no longer useful you can delete it.

.. code-block:: shell

  git checkout master
  git branch -d temporary

If you have unmerged changes in the old branch Git complains and you need to
use ``-D`` instead of ``-d``.

Viewing Changes
---------------

To view all changes since the last commit:

.. code-block:: shell

  git diff HEAD

To view all changes between the current branch and another branch, say master:

.. code-block:: shell

  git diff master..HEAD

To view descriptions of committed changes:

.. code-block:: shell

  git log

Or view the changeset for some file (or directory):

.. code-block:: shell

  git log /some/file

To view the changesets made between two branches:

.. code-block:: shell

  git log master..HEAD

Or for a more brief description use shortlog:

.. code-block:: shell

  git shortlog master..HEAD

Reverting Changes
-----------------

To remove all (uncommitted) changes on a branch

.. code-block:: shell

  git checkout -f

Or to selectively revert (uncommited) files, for example if you
accidentally deleted ./some/file

.. code-block:: shell

  git checkout -- ./some/file

or

.. code-block:: shell

  git checkout HEAD ./some/file

To remove commits there are two useful options, reset and revert. ``git reset``
should only be used on local branches that no one else is accessing remotely.
``git revert`` is cleaner and is the right way to revert changes that have
already been pushed/pulled remotely.

git reset
---------

``git reset`` is a powerful and tricky command that should only be used on
local (un-pushed) branches): A good description of what it enables to do can be
found here. The following are a few useful examples. Note that adding a ~
after HEAD refers to the most recent commit, and you can add a number after
the ~ to refer to commits even further back; HEAD by itself refers to the
current working directory (changes since the last commit).

.. code-block:: shell

  git reset HEAD~

Will undo the last commit and unstage those changes. Your working directory
will remain the same, therefore a ``git status`` will yield any changes you
made plus the changes made in your last commit. This can be used to fix the
last commit. You will need to add the files again.

.. code-block:: shell

  git reset --soft HEAD~

Will just undo the last commit. The changes from the last commit will still be
staged (just as if you finished git adding them). This can be used to amend the
last commit (e.g. You forgot to add a file to the last commit).

.. code-block:: shell

  git reset --hard HEAD~

Will revert everything, including the working directory, to the previous
commit. This is dangerous and can lead to you losing all your changes; the
``--hard`` flag ignores errors.

.. code-block:: shell

  git reset HEAD

Will unstage any change. This is used to revert a wrong ``git add``. (e.g. You
added a file that shouldn't be there, but you haven't 'committed')

Will revert your working directory to a HEAD state. You will lose any change
you made to files after the last commit. This is used when you just want to
destroy all changes you made since the last commit.

git revert
----------

``git revert`` does the same as reset but creates a new commit with the
reverted changes instead of modifying the local repository directly.

.. code-block:: shell

  git revert HEAD

This will create a new commit which undoes the change in HEAD. You will be
given a chance to edit the commit message for the new commit.

Merging Changes
---------------

Suppose you commit changes in two different branches, branch1 and branch2,
and want to create a new branch containing both sets of changes:

.. code-block:: shell

  git checkout -b merged
  git merge branch1
  git merge branch2

Or you might want to bring the changes in one branch into the other:

.. code-block:: shell

  git checkout branch1
  git merge branch2

And now that branch2 is merged you might get rid of it:

.. code-block:: shell

  git branch -d branch2

If you have done work on a branch, say branch1, and have gone out-of-sync
with the remote repository, you can pull the changes from the remote repo and
then merge them into your branch:

.. code-block:: shell

  git checkout master
  git pull
  git checkout branch1
  git merge master

If all goes well the new commits you pulled into your master branch will be
merged into your branch1, which will now be up-to-date. However, if branch1
has not been pushed remotely then rebasing might be a good alternative to
merging because the merge generates a commit.

Rebasing
--------

An alternative to the merge command is rebase, which replays the changes
(commits) on one branch onto another. ``git rebase`` finds the common ancestor
of the two branches, stores each commit of the branch you are on to temporary
files and applies each commit in order.

For example

.. code-block:: shell

  git checkout branch1
  git rebase master

or more concisely

.. code-block:: shell

  git rebase master branch1

will bring the changes of master into branch1, and then you can fast-forward
master to include branch1 quite easily

.. code-block:: shell

  git checkout master
  git merge branch1

Rebasing makes a cleaner history than merging; the log of a rebased branch
looks like a linear history as if the work was done serially rather than in
parallel. A primary reason to rebase is to ensure commits apply cleanly on a
remote branch, e.g. when submitting patches to RTEMS that you create by working
on a branch in a personal repository. Using rebase to merge your work with the
remote branch eliminates most integration work for the committer/maintainer.

There is one caveat to using rebase: Do not rebase commits that you have pushed
to a public repository. Rebase abandons existing commits and creates new ones
that are similar but different. If you push commits that others pull down, and
then you rewrite those commits with ``git rebase`` and push them up again, the
others will have to re-merge their work and trying to integrate their work
into yours can become messy.

Accessing a developer's repository
----------------------------------

RTEMS developers with Git commit access have personal repositories
on https://git.rtems.org/ that can be cloned to view cutting-edge
development work shared there.

Creating a Patch
----------------

Before submitting a patch read about `Contributing
<https://devel.rtems.org/wiki/Developer/Contributing>`_ to RTEMS and the
`Commit Message <https://devel.rtems.org/wiki/Developer/Git#GitCommits>`_
formatting we require.

The recommended way to create a patch is to branch the Git repository master
and use one commit for each logical change. Then you can use
``git format-patch`` to turn your commits into patches and easily submit them.

.. code-block:: shell

  git format-patch master

Creates a separate patch for each commit that has been made between the master
branch and the current branch and writes them in the current directory. Use the
``-o`` flag to redirect the files to a different directory.

If you are re-submitting a patch that has previously been reviewed, you should
specify a version number for your patch, for example, use

.. code-block:: shell

  git format-patch -v2 ...

to indicate the second version of a patch, ``-v3`` for a third, and so forth.

Also, in order to create a patch specifying the repo name in the patch message,
you should use the``--subject-prefix`` flag. For example, if contributing to
the rtems-docs repo, use

.. code-block:: shell

  git format-patch --subject-prefix="PATCH rtems-docs" ...

Patches created using ``git format-patch`` are formatted so they can be emailed
and rely on having Git configured with your name and email address, for example

.. code-block:: shell

  git config --global user.name "Your Name"
  git config --global user.email name@domain.com

Please use a real name, we do not allow pseudonyms or anonymous contributions.

Submitting a Patch
------------------

Using ``git send-email`` you can easily contribute your patches. You will need
to install ``git send-email`` first:

.. code-block:: shell

  sudo yum install git-email

or

.. code-block:: shell

  sudo dnf install git-email

or

.. code-block:: shell

  sudo apt install git-email

Then you will need to configure an SMTP server. You could install one on your
localhost, or you can connect to a mail server such as Gmail.

Configuring git send-email to use Gmail
---------------------------------------

Configure Git to use Gmail:

.. code-block:: shell

  git config --global sendemail.smtpserver smtp.gmail.com
  git config --global sendemail.smtpserverport 587
  git config --global sendemail.smtpencryption tls
  git config --global sendemail.smtpuser your_email@gmail.com

It will ask for your password each time you use ``git send-email``. Optionally
you can also put it in your ``git config``:

.. code-block:: shell

  git config --global sendemail.smtppass your_password

Sending Email
-------------

To send your patches just

.. code-block:: shell

  git send-email /path/to/patch --to devel@rtems.org

To send multiple related patches (if you have more than one commit in your
branch) specify a path to a directory containing all of the patches created by
``git format-patch``. ``git send-email`` has some useful options such as:

* ``--annotate`` to show/edit your patch
* ``--cover-letter`` to prepend a summary
* ``--cc=<address>`` to cc someone

You can configure the to address:

.. code-block:: shell

  git config --global sendemail.to devel@rtems.org

So all you need is:

.. code-block:: shell

  git send-email /path/to/patch

Troubleshooting
---------------

Some restrictive corporate firewalls block access through the Git protocol
(git://). If you are unable to reach the server git://git.rtems.org/ you can
try accessing through http. To clone the rtems repository using the http
protocol use the following command:

.. code-block:: shell

  git clone http://git.rtems.org/rtems/ rtems

This access through http is slower (way slower!) than through the git protocol,
therefore, the Git protocol is preferred.

Manage Your Code
----------------

You may prefer to keep your application and development work in a Git
repository for all the good reasons that come with version control.
For public repositories, you may like to try `GitHub <https://github.com/>`_
or `BitBucket <https://bitbucket.org/>`_. RTEMS maintains
`mirrors on GitHub <https://github.com/RTEMS>`_ which can make synchronizing
with upstream changes relatively simple. If you need to keep your work private,
you can use one of those services with private repositories or manage your own
server. The details of setting up a server are outside the scope of this
document, but if you have a server with SSH access you should be able to `find
instructions
<https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server>`_ on
how to set up Git access. Once you have git configured on the server, adding
repositories is a snap.

Private Servers
---------------

In the following, replace @USER@ with your username on your server, @REPO@ with
the name of your repository, and @SERVER@ with your server's name or address.

To push a mirror to your private server, first create a bare repository on your
server.

.. code-block:: shell

  cd /home/@USER@
  mkdir git
  mkdir git/@REPO@.git
  cd git/@REPO@.git
  git --bare init

Now from your client machine (e.g. your work laptop/desktop), push a git,
perhaps one you cloned from elsewhere, or one that you made locally with
``git init``, by adding a remote and pushing:

.. code-block:: shell

  git remote add @SERVER@ ssh://@SERVER@/home/@USER@/git/@REPO@.git
  git push @SERVER@ master

You can replace the @SERVER@ with another name for your remote if you like.
And now you can push other branches that you might have created. Now you can
push and pull between your client and your server. Use SSH keys to authenticate
with your server if you want to save on password typing; remember to put a
passphrase on your SSH key if there is a risk the private key file might get
compromised.

The following is an example scenario that might be useful for RTEMS users that
uses a slightly different approach than the one just outlined:

.. code-block:: shell

  ssh @SERVER@
  mkdir git
  git clone --mirror git://git.rtems.org/rtems.git
  ## Add your ssh key to ~/.ssh/authorized_keys
  exit
  git clone ssh://@SERVER@/home/@USER@/git/rtems.git
  cd rtems
  git remote add upstream git://git.rtems.org/rtems.git
  git fetch upstream
  git pull upstream master
  git push
  ## If you want to track RTEMS on your personal master branch,
  ## you should only push changes to origin/master that you pull
  ## from upstream. The basic workflow should look something like:
  git checkout master
  git pull upstream master
  git push
  git checkout -b anewbranch
  ## Repeat: do work, git commit -a
  git push origin anewbranch

  ## delete a remote branch
  git push origin :anewbranch
  ## delete a local branch
  git branch -d anewbranch

Learn more about Git
--------------------

Links to the sites with good Git information:

* http://gitready.com/ - An excellent resource from beginner to very advanced.
* http://progit.org/book/ - Covers Git basics and some advanced features.
  Includes some useful workflow examples.
* https://lab.github.com/ - Learn to use Git and GitHub while doing a series of
  projects.
* https://git-scm.com/docs - The official Git reference.
