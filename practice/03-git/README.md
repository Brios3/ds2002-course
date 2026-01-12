# Git & GitHub

The goal of this activity is to familiarize you with version control using Git and GitHub. These tools are essential for tracking changes in your code, collaborating with others, managing project history, and contributing to open-source projects.

If the initial examples feel like a breeze, challenge yourself with activities in the *Advanced Concepts* section and explore the resource links at the end of this post.

* Start with the **In-class Exercises**.
* Continue with the **Additional Practices** section on your own time. 
* Optional: Explore the **Advanced Concepts** if you wish to explore Git and GitHub in more depth.

## In-class exercises

### Collaborations with Git/GitHub

We're going to collectively build a single file that contains a fun fact from everyone in the class. This will give you hands-on experience with the core workflow of collaborative development.

**The Objective**: Your goal is to add a single line to the 'class_log.txt' file in this repository in the Activity_2 folder.

### Step 1: Fork the Repository
First, you need to create your own copy of this repository. This is called forking. A fork is a personal sandbox where you can make changes without affecting the original project.
1. Open the repository in your web browser: `https://github.com/austin-t-rivera/DS-2002-F25`
2. In the top-right corner, click the "**Fork**" button.
3. A pop-up will ask you to confirm. Just click "**Create fork.**"
4. You will now have a copy of the repository under your own GitHub account.

<br>

### Step 2: Clone Your Fork
Now you need to get the code from your personal GitHub copy onto your local computer. This is called cloning.
1. On your new forked repository page, click the green "**Code**" button.
2. Make sure the **SSH** tab is selected.
3. Copy the URL to your clipboard. It will look like `git@github.com:YOUR-USERNAME/DS-2002-F25.git`.
4. Open your **Terminal** (or Git Bash/WSL) and run the `git clone` command followed by the URL you copied:
```
git clone [paste your copied URL here]
```
5. Use `ls` to confirm that a new folder named DS-2002-F25 has been created.
6. Change into that new directory:
```
cd DS-2002-F25
```

<br>

### Step 3: Add Your Contribution
Now that you have the repository on your computer, it's time to add your contribution.

1. Figure out what you want to put after your name for your fun fact and favorite Bash command, following this format:
```
[Your Name], [A Fun Fact About You], [Your Favorite Bash Command]
```
For example:
```
Jane Doe, I can play the ukulele, ls
```
2. NAVIGATE TO THE `Activity_2` DIRECTORY!
2. Choose one of the following methods to edit the `class_log.txt` file:
  - Open the file from the command line using the `nano` command:
```
nano class_log.txt
```
  - Use the `echo` command and the `>>` operator to append your message into the file:
```
echo 'Jane Doe, I can play the ukulele, ls' >> class_log.txt
```
  - Open the file in your favorite text editor.

3. Make sure the file is saved!

<br>

### Step 4: Add, Commit, and Push
You've made a change, but Git doesn't know about it yet. This is where the core Git workflow comes in.

1. Stage your change with `git add`, either implicitly or explicitly:
- **Implicitly**: this will stage any files you have added, deleted, or modified and saved on this branch.
```
git add .
```

- **Explicitly**: this will stage only files you explicitly name that you have added, deleted, or modified and saved on this branch.
```
git add class_log.txt
```

2. Commit your change to your local branch with a brief but descriptive message. The -m stands for "message".
```
git commit -m "Add my contribution to the class log."
```

3. Push your committed changes from your local computer back to your forked repository on GitHub.
```
git push origin main
```

<br>

### Step 5: Submit a Pull Request
Now you'll request that your changes be pulled into the original repository.

1. Go back to your forked repository page on GitHub.
2. You should see a yellow banner at the top that says, "This branch is 1 commit ahead of austin-t-rivera:main." Click the "Contribute" button.
3. Click "**Open pull request.**"
4. Give your pull request a clear title like "Adds [Your Name] to class log" and write a short description explaining what you did.
5. Click the "**Create pull request**" button.

Congratulations! Your pull request has been submitted. The repository owner (your instructor) will then review and merge your changes.

<br>

### Step 6: Submit Your Pull Request URL
1. Go to your pull request on GitHub and copy the URL.
2. Paste the URL of your PR into the submission box for Activity 2 on Canvas.

<br>

### Bonus Skill: Update Your Repository
Now that your contribution is merged, you're ready to see everyone else's. In your Terminal, run the `git pull` command to get the latest changes from the original repository:
```bash
git pull origin main --merge
```

**The `class_log.txt` file on your computer will now be updated with everyone else's contributions.**

<br>

If you completed these activities, feel free to continue with the [Small Group Activity](#small-group-activity) at your table.

<br>

### Small Group Activity

At your table, select one person to set up a new repository on GitHub. Work through these steps:

1. **Repository Setup:**
   * The creator adds all group members as collaborators to the new repository on GitHub. The repository should have a single `main` branch.

2. **Clone the Repository:**
   * All group members should clone the new repository to their own environment:
     ```bash
     git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
     cd REPO_NAME
     ```
   Replace the `YOUR_USERNAME` and `REPO_NAME` with your actual GitHub username and repository name.
   
   **Important:** Make sure you are **not** inside an existing Git repository when running the `git clone` command. You don't want to create nested Git repositories.

3. **Create Unique Files:**
   * Each group member should create a new text file in their local repository. Use unique filenames to avoid collisions (e.g., `alice.txt`, `bob.txt`). Each team member should commit and push their files to the GitHub repository:
     ```bash
     echo "Hello from Alice" > alice.txt
     git add alice.txt
     git commit -m "Add alice.txt"
     git push origin main
     ```

4. **Verify on GitHub:**
   * All: Check the presence of the new files on GitHub by visiting the repository page.

5. **Pull Latest Changes:**
   * All: Run the following command in your environment to get the latest changes from GitHub:
     ```bash
     git pull origin main --merge
     ```
     (The `--merge` flag is explicit and avoids warnings in newer Git versions.)

6. **Create Collision File:**
   * All: Create a new file `collision.txt` in your local repository. The file should contain a single line with your `first name, favorite animal`:
     ```bash
     echo "Alice, cat" > collision.txt
     git add collision.txt
     git commit -m "Add collision.txt"
     git push origin main
     ```

### Resolving Merge Conflicts:

**The early bird gets the worm:** If you are the first person to push the `collision.txt` file, you're in luck—the push should go through without a hitch. However, the others will encounter an error message like this:

```bash
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/YOUR_USERNAME/REPO_NAME.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**To resolve the conflict:**

Starting with the group member next to the first person who successfully pushed, go clockwise and perform the following steps:

1. Pull with rebase to reconcile the differences:
   ```bash
   git pull origin main --rebase
   ```

   **Alternative (using merge instead of rebase):**
   If you prefer to use a merge commit instead of rebasing, you can use:
   ```bash
   git pull origin main --merge
   ```
   (The `--merge` flag is explicit and avoids warnings in newer Git versions. You can also use `--no-rebase` which is equivalent.)
   
   This will create a merge commit. After resolving conflicts, you'll use `git commit` instead of `git rebase --continue` (see step 5 below).

2. Git will pause and indicate that there are conflicts. VSCode (or your editor) will highlight the conflicting lines in `collision.txt`.

3. **Resolve the conflict:** You want to **append** (not replace) the content so that everyone's entry is included. The file should contain all group members' entries, one per line:
   ```
   Alice, cat
   Bob, dog
   Carol, bird
   ```

4. After resolving the conflict, stage the resolved file:
   ```bash
   git add collision.txt
   ```

5. Complete the merge/rebase:
   - **If using rebase** (recommended for cleaner history):
     ```bash
     git rebase --continue
     ```
   - **If using merge**:
     ```bash
     git commit
     ```
     (This completes the merge commit)

6. Push your changes:
   ```bash
   git push origin main
   ```

7. The next person in the group should repeat steps 1-6 until everyone has successfully pushed their entry to the consolidated `collision.txt` file on GitHub. 

## Additional Practice

### Setting up and Managing Repositories

Read <a href="https://uvads.github.io/git-basics/" target="_blank" rel="noopener noreferrer">git in Data Science</a> for a brief introduction.

Then work through the <a href="https://uvads.github.io/git-basics/docs/creating-repositories/" target="_blank" rel="noopener noreferrer">Creating and Managing Git Repositories Exercises</a>. These exercises will cover:

* Init
* Fork (should be familiar from [Setup Instructions](../../setup/README.md))
* Delete
* Managing Collaborators 

### Working with branches

1. **List all branches:**
   ```bash
   git branch
   ```
   This shows all local branches. The current branch is marked with an asterisk (*).

2. **Create a new branch:**
   ```bash
   git switch -c feature-branch
   ```
   The `-c` flag creates a new branch and switches to it immediately. Alternatively, you can create a branch first with `git branch feature-branch` and then switch to it with `git switch feature-branch`.

3. **Switch to an existing branch:**
   ```bash
   # be safe, make sure you are not losing anything
   git add .
   git commit -m "committing everything before getting files from other branches"
   # now it is safe to switch
   git switch main
   ```
   This switches you to the `main` branch. **Make sure you've committed or stashed any changes before switching branches.**

### Pull requests

**Exercise:** Create a pull request on GitHub

1. Create a new branch for your changes:
   ```bash
   git switch -c my-feature
   ```

2. Make some changes:
   ```bash
   echo "## Features" >> README.md
   echo "- Feature 1" >> README.md
   git add README.md
   git commit -m "Add features section to README"
   ```

3. Push the branch to GitHub:
   ```bash
   git push -u origin my-feature
   ```
   The `-u` ensures that the `my-feature` branch is created in the remote repository if it doesn't exist already.

4. On GitHub:
   - Navigate to your repository
   - You should see a banner suggesting to create a pull request
   - Click "Compare & pull request"
   - Add a description of your changes
   - Click "Create pull request"

5. Review the pull request:
   - Check the "Files changed" tab to see your modifications
   - Add comments if needed
   - Merge the pull request when ready

6. After merging, update your local repository:
   ```bash
   git switch main
   git pull origin main --merge
   git branch -d my-feature
   ```

## Advanced Concepts (Optional)

### Initializing a new repo and connecting it to GitHub with gh cli

You may already have a project set up in a directory on your computer (or in codespace), but it's not set up as a Git repository yet. The following steps show you how to initialize it and connect it to GitHub.

### Create a new local Git repository

1. Create a new directory for your project:
   ```bash
   cd # go to your home directory, or any other directory that is NOT inside an existing repo
   mkdir my-git-project
   cd my-git-project
   ```

2. Initialize a Git repository:
   ```bash
   git init
   ```

3. Verify the repository was created:
   ```bash
   ls -la .git
   ```

   You should see a `.git` directory containing the repository metadata. 
   > **Note:** This repository only exists in your local environment; it is not on GitHub yet.


4. Create repository from command line (requires GitHub CLI)
```bash
# Install GitHub CLI if not already installed
# Then create the repository:
gh repo create my-git-project --public --source=. --remote=origin --push
```

This single command creates the GitHub repository and pushes your code.

### Stashing, rebasing, etc.

If you want to explore additional Git features, review the <a href="https://uvads.github.io/git-basics/docs/advanced/" target="_blank" rel="noopener noreferrer">Advanced git</a> tutorial.

### Creating a Repository from a Template

GitHub allows you to create new repositories from templates, which can include pre-configured files, workflows, and settings. This is useful for starting projects with best practices already in place.

### Using the Secure Repository Template

The course repository includes a template URL for creating repositories with security best practices. Here's how to use it:

**Step 1: Get the template URL**

The template URL is located in `github-new-repo-from-template.txt` in this directory (`practice/03-git/`). The URL format is:

```
https://github.com/new?owner=YOUR_USERNAME&template_name=secure-repository-supply-chain&template_owner=skills&name=YOUR_REPO_NAME&visibility=public
```

**Step 2: Customize the URL**

Replace the placeholders:
- `YOUR_USERNAME` - Your GitHub username or organization name
- `YOUR_REPO_NAME` - The name you want for your new repository
- `visibility=public` - Change to `visibility=private` if you want a private repository

**Step 3: Create the repository**

1. Copy the complete URL with your customizations
2. Paste it into your browser's address bar
3. Press Enter
4. GitHub will open the repository creation page with the template pre-selected
5. Review the settings and click "Create repository"

**Example:**

If your username is `johndoe` and you want to create a repo called `my-secure-project`:

```
https://github.com/new?owner=johndoe&template_name=secure-repository-supply-chain&template_owner=skills&name=my-secure-project&visibility=public
```

**What you get:**

The "secure-repository-supply-chain" template from GitHub Skills includes:
- Security best practices configuration
- Supply chain security settings
- Dependabot setup for dependency updates
- Security policies
- Code scanning workflows
- GitHub Actions for security checks

**Alternative: Using GitHub's Web Interface**

You can also create a repository from a template using GitHub's web interface:

1. Go to the template repository: https://github.com/skills/secure-repository-supply-chain
2. Click the green **"Use this template"** button
3. Select **"Create a new repository"**
4. Choose your owner, repository name, and visibility
5. Click **"Create repository"**

## Resources

- <a href="https://uvads.github.io/git-basics/" target="_blank" rel="noopener noreferrer">git in Data Science</a> - Brief introduction to Git
- <a href="https://skills.github.com/" target="_blank" rel="noopener noreferrer">GitHub Skills</a>
