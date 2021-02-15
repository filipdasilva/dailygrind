To work properly with a remote git branch that is chang,
you want to make sure you are preserving the other peoples commits.

You may have ran into a merge conflict already. To mitigate this you can usually
run `git pull --rebase`.

This will
1) pull the remote branch from github
2) remove your `new` commits
3) play the `new` commits from the remote branch on the previous code
4) play your `new` commits back ontop of those.

If there are no conflicts, you're good to go.

If there are conflicts you can follow the prompt the
terminal prints for you to figure out how to resolve them.

TL:DR - if your local have diverged from the remote -> do `git pull --rebase`.
It's like touching base first.

