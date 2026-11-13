# Architecture - Student Task Planner App

## Overview
A simple single-page web app. All logic runs in the browser and data is stored in the browser (no authentication, no backend server in the first version).

## High-Level System Diagram
+--------------------+
| User |
+---------+----------+
|
v
+---------+----------+
| UI (HTML/CSS) |
| Task form, list, |
| filters, progress |
+---------+----------+
|
v
+---------+----------+
| App Logic (JS) |
| Add/edit/delete, |
| filter, sort, |
| reminders, export |
+----+----------+----+
| |
v v
+----+-----+ +-+----------------+
| Browser | | CSV Export |
| Storage | | (file download) |
+----------+ +------------------+

## Components
- **UI layer**: task form, task list, filters, progress bar, reminders area.
- **App logic**: handles creating, updating, deleting, filtering, sorting tasks and the 100-task limit.
- **Storage**: tasks saved in the browser (localStorage).
- **Export**: converts the task list to a CSV file for download.
