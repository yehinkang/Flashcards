
# Flashcards Project (for Mac Users New to Python & Git)

Welcome! This guide will walk you through installing Python, using git to get the project, setting up your environment, and running the flashcards program on your Mac.

## 1. Install Homebrew (if you don't have it)

Homebrew is a package manager for Mac. Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. Install Python 3

Still in Terminal, run:

```bash
brew install python
```






## 3. Download the Project from GitHub (No Command Line Needed)

1. Go to the project’s GitHub page in your web browser (you should have been given a link, for example: https://github.com/yehinkang/Flashcards).

2. Click the green **Code** button, then choose **Download ZIP**.

3. Once the ZIP file downloads, double-click it in your Downloads folder to unzip it. This will create a folder named something like `Flashcards-main` or `Flashcards-master`.

4. Move this folder to a location you can find easily, such as your Documents folder.

5. Open the folder. You should see files like `flashcards.py`, `requirements.txt`, and `README.md` inside.


**Tip:**
- To get the full path to this folder for use in Terminal, hold the Option key and right-click the folder in Finder, then choose "Copy (folder) as Pathname". You can then paste that path after `cd` in Terminal.
- If you use Visual Studio Code (VS Code), you can open the project folder by going to **File > Open Folder...**. Once the folder is open in VS Code, you can open a new Terminal window directly in that location by selecting **Terminal > New Terminal** from the menu. This will save you from having to navigate with the `cd` command manually.

## 5. Create a Virtual Environment

In the project folder, run:

```bash
python3 -m venv .venv
```

## 6. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

You should see `(.venv)` at the start of your Terminal prompt.

## 7. Install Required Packages

With the virtual environment activated, run:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```


## 8. Run the Flashcards Program

With your virtual environment activated and inside the project folder, run:

```bash
python flashcards.py
```

This will generate a file named like `flashcards_YYYYMMDDHHMMSS.apkg` in the same directory. The numbers represent the date and time the file was created. You can then import this `.apkg` file into Anki.

**How to navigate to the folder:**

- Use the `cd` command in Terminal to move into the folder where `flashcards.py` is located. For example:
	```bash
	cd /path/to/your/Flashcards
	```
- On a Mac, you can copy the full path to a folder by holding the Option key and right-clicking the folder in Finder, then choosing "Copy (folder) as Pathname". Paste that path after `cd` in Terminal.

## 9. Deactivate the Virtual Environment (when done)

```bash
deactivate
```

---

### Troubleshooting

- If you see "command not found" for `python3` or `pip`, make sure Homebrew and Python are installed and your Terminal is restarted.
- If you see errors about missing packages, double-check you ran the `pip install -r requirements.txt` step with the venv activated.

---

If you have any questions, ask the person who shared this project with you!
