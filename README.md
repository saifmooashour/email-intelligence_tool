 

 Email Intelligence Tool:

A simple Python tool that analyzes email log files and identifies the most frequent email senders using SQLite.

 Overview:

This project reads an email log file (such as mbox format), extracts sender email addresses from lines that start with `From `, stores the counts in a SQLite database, and displays the top N email senders.

 Features:

- Reads email log files
- Extracts sender email addresses
- Stores counts in a SQLite database
- Displays top N senders sorted by frequency

 How to Run:

1. Make sure Python 3 is installed.
2. Run the script:

   ```bash
   python email_intelligence_tool.py

3. Enter:

The email log file name (press Enter to use mbox.txt)

The number of top senders to display




Example

Enter file name: mbox.txt
How many top senders? 2

cwen@iupui.edu 10
zqian@umich.edu 8

Technologies Used

Python

SQLite


Purpose:

This project was built as a learning exercise to practice:

File processing

Data extraction

Working with SQLite databases

Writing basic SQL queries

Building a simple data processing workflow


Author

Saif Ashour





ارفعها الآن وخلص.  
وبعدها نقرر المشروع التالي.
