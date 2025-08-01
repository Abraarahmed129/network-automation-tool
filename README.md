 Network Automation Tool

A web-based tool built with Python and Flask that provides a simple dashboard to monitor a network device's status and automate basic VLAN configurations. 

---

Architectural decision

Initially, this application was designed to connect to a live Cisco DevNet sandbox. However, due to the unreliability of public sandboxes (potential downtime, password changes), a key architectural decision was made: **to refactor the backend into a mock service.**

This  practice ensures the application is stable and reliable for demonstration.

---

 Key Features

Web-Based Dashboard: A clean user interface built with Flask and HTML/CSS for easy interaction.
Simulated Device Monitoring: Displays realistic output from a network device's `show version` command.
Automated VLAN Configuration: Allows a user to input a VLAN ID and Name and see a simulated, successful configuration log.
Decoupled & Stable Mock Backend:** Ensures the application is always available and runs instantly.

Technology Stack

Backend: Python
Web Framework: Flask
Frontend: HTML5, CSS3
Version Control: Git & GitHub
