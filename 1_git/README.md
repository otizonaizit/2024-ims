# Random git notes

## fixing mistakes
- how to revert mistakes?
    - before commit:
      - `git restore <file>` [discard changes in the working directory] __changes files__
      - `git restore --staged <file>` [unstage changes ➔ opposite of `git add <file>`, does not modify the working directory]
    - after commit:
      - `git revert <commit>` [creates a new commit, modifies the working directory]
      - `git reset <commit>` [only reset the HEAD pointer, does not modify the working directory] __rewrites history__ ➔ can not be used if you have already pushed to some remote
      - `git reset --hard <commit>` [reset HEAD and modify working directory] __rewrites history__ and __changes files__ ➔ can not be used if you have already pushed to some remote
- how to *move* the whole working directory to a specific point in history?
    - `git checkout <commit>` ➔ `DETACHED HEAD` problem, __changes__ __files__
    - interaction with branches: `git branch <branch_name>` + `git switch <branch_name>`
- how to copy a file from a different branch (without commits): `git restore --source other_branch filepath` ➔ very dangerous: overwrites any non-commited local changes
- `git gui`: building commits along the way interactively (for the *mess around* type of workflows)

## The Open Source model
- remotes: `git pull <from_where> <what>`, `git push <where> <what>`, `git fetch <from_where> <what>`, `git merge <another_branch>`
- GitHub: forks, branches and PRs: important ➔ explain fork vs. clone!!!
- strategies for keeping your fork up-to-date: your `main`, origin's and upstream's `main`, short-lived and long-lived topic branches
- a more thorough and detailed explanation can be found on the [Numpy Contributor's Guide](https://docs.scipy.org/doc/numpy/dev/gitwash/index.html). This guide can be adapted to your own needs, see [gitwash](https://github.com/matthew-brett/gitwash).
- make it clear that GitHub is just an option (git≠GitHub)

## Scenarios
1. lone scientist working alone in the cellar without Internet (local git)
2. lone scientist uploading their software to the Internet in the hope it can be useful for other people (local git + one personal GitHub repo)
3. lone scientist sharing one software project with some other befriended lone scientist working in a different place (local git + one personal GitHub repo + permissions)
4. research group sharing software among members (local git + several GitHub repos + permissions + branches + [optional] PRs)
5. fully distributed software development using the most typical open source software workflows as used by numpy, scipy, sklearn, etc. (like above + we don't trust our contributors, i.e. work strictly with forks)


