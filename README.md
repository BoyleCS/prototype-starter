# Python prototype classroom

Your teacher supplies the student workbook. Begin with Worksheet 1 parts A to F.
Those pages teach account sign-in, project copying, Codespace creation,
Explorer, opening app.py, the terminal, the preview, saving, and reopening.
Finish that walkthrough before using this short daily command reference.

## First use

Create your own repository from the class template. In your repository, choose
Code, Codespaces, then Create codespace. The initial setup installs Streamlit.

In the TERMINAL INSIDE CODESPACES run:

```bash
python -m streamlit run app.py --server.address 0.0.0.0
```

In the Ports panel, open port 8501 in your browser.

## Every lesson

Reopen the SAME workspace at https://github.com/codespaces.
If the app is stopped, run the command above again.
When the worksheet asks you to load a starter, first stop the app with Ctrl+C.
Copy the named starter into app.py using the exact command on the worksheet.
Then run the app command again. The copy replaces app.py, so commit and sync
your previous work before doing it. Your saved versions remain in GitHub.

## Saving and finishing

Save your files. In Source Control, stage your changed files with +, enter a
short message, Commit, and Sync Changes. At the end of class, go to
https://github.com/codespaces and choose Stop codespace from its ... menu.
The Codespaces preview works only while the workspace and app are running.

## Folders

app.py is your current application. data.py contains the supplied sample data.
lessons contains starting checkpoints. Keep that folder unchanged.
Your teacher has separate worked solutions; this repository does not include them.
