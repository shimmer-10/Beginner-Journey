# Git Basics

- ```bash git init``` : Construct a .git folder (brain of git) which stores history, Refrences, Commits, configuration etc. It is mainly like telling folder that its a repository now.
- ```bash git remote add origin <path of repository> ``` : Set a connection between Git and Folder.
- ```bash git remote -v ``` : Tells , show me the remote you know.
- ```bash git status ``` : Shows modified, staged, and untracked files along with the current branch.
- ```bash git add . ``` : Stage the changes we want to save.
- ```bash git commit ``` : Save the changes Locally.(creates history)
- ```bash git push ``` : Uploads local commits to the remote repository i.e, GitHub.(Uploads History)

## Important Terms

**Local Repository** → Repository stored on your computer.
**Remote Repository** → Repository stored on GitHub.
**Branch** → An independent line of development.

## How We Merged Local & Remote History

**Problem:** I accidentally created two independent Git histories.

```text
GitHub
└── Add initial README

Local
├── Add initial README.md
├── Two Sum
├── Maximum Sum Subarray
└── Git Basics
```

Git refused to push because the remote repository already had commits that my local repository didn't have.

**Solution:**

- Rename local branch to match GitHub:
```bash
git branch -M main
```

- Merge both independent histories:
```bash
git pull origin main --allow-unrelated-histories
```

- Git found a conflict in `README.md` because both histories had modified the same file.

Git showed:

```text
<<<<<<< HEAD
My version
=======
GitHub version
>>>>>>> commit-id
```

I manually combined the required content, removed the conflict markers and saved the file.

- Tell Git the conflict is resolved:
```bash
git add README.md
```

- Create a merge commit:
```bash
git commit -m "Merge local and remote repository histories"
```

- Upload everything to GitHub and set the upstream branch:
```bash
git push -u origin main
```

**Final History:**

```text
              Merge Commit
             /            \
GitHub README          Local History
                           │
                      Two Sum
                           │
              Maximum Sum Subarray
                           │
                      Git Basics
```

Now both histories are connected into one history (`main`). Future work only requires:

```bash
git add .
git commit -m "..."
git push
```