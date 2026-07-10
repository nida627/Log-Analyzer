# 📊 Log Analyzer

A Python-based console application that parses log files using **Regular Expressions (Regex)** and generates a detailed analysis report.

---

## 📌 Project Overview

The Log Analyzer reads a log file (`logs.txt`), validates each log entry using **Regular Expressions**, extracts useful information such as **Date, Time, Log Level, and Message**, and generates a report summarizing the log analysis.

The application identifies **INFO**, **WARNING**, and **ERROR** logs, detects invalid log entries, stores error details, and automatically generates a `report.txt` file.

---

## ✨ Features

- Read log data from a text file
- Parse log entries using Regular Expressions (`re`)
- Count INFO, WARNING, and ERROR logs
- Detect invalid log entries
- Store ERROR log details
- Generate analysis report (`report.txt`)
- Display summary on the console
- Menu-driven interface
- Simple and beginner-friendly code

---

## 🛠️ Technologies Used

- Python 3.x
- Regular Expressions (`re`)
- OS Module (`os`)
- DateTime Module (`datetime`)
- File Handling

---

## 📂 Project Structure

```
Log_Analyzer/
│
├── log.py
├── logs.txt
├── report.txt
├── README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone <repository-link>
```

### 2️⃣ Open the Project Folder

```bash
cd Log_Analyzer
```

### 3️⃣ Run the Program

```bash
python analyzer.py
```

---

## 📄 Sample Log File

```
2026-07-07 09:00:15 INFO User Login Successful
2026-07-07 09:05:45 WARNING Low Disk Space
2026-07-07 09:08:20 ERROR Database Connection Failed
```

---

## 📋 Sample Console Output

```
========================================
      ANALYSIS SUMMARY
========================================

Total Logs     : 10
INFO Logs      : 5
WARNING Logs   : 2
ERROR Logs     : 3
Invalid Logs   : 2

Report Generated Successfully!
```

---

## 📑 Sample Report

The application automatically generates a **report.txt** containing:

- Report Generation Time
- Total Logs
- INFO Count
- WARNING Count
- ERROR Count
- Invalid Log Count
- Error Details

---

## 📚 Python Concepts Used

- File Handling
- Functions
- Loops
- Conditional Statements
- Lists
- Regular Expressions (Regex)
- Pattern Matching
- Report Generation
- Menu-Driven Programming

---

## 📦 Python Modules Used

| Module | Purpose |
|----------|---------|
| re | Parse log entries using Regular Expressions |
| os | Check if the log file exists |
| datetime | Add timestamp to the generated report |

---

## 📈 Future Enhancements

- Support for multiple log file formats
- Search logs by keyword
- Filter logs by log level
- Export reports in PDF and Excel
- Real-time log monitoring
- Graphical dashboard using Flask
- Database integration

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Practical use of Regular Expressions
- Log Parsing Techniques
- File Handling in Python
- Report Generation
- Pattern Matching
- Console Application Development
- Writing clean and modular Python code

---

## 👨‍💻 Author

**Nida Ansari**

Trainee Python Developer 
