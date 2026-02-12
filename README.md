Email Intelligence Tool

This project is a simple Python tool that analyzes email log files and identifies the most frequent email senders.
Features
Reads email log files in mbox-style format
Extracts sender email addresses from lines starting with From 
Counts occurrences using an SQLite database
Displays the top N most frequent senders
Included Sample File
The repository includes a small sample file named:

sample_mbox.txt
You can replace it with your own email log file.
How to Run
Make sure Python 3 is installed
Run:

python email_intelligence_tool.py
Enter:
The file name (press Enter to use the sample file)
The number of top senders to display
Technologies Used
Python
SQLite
