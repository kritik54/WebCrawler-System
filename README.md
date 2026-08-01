# Topic-Specific Web Crawler and Search Engine

## BCS 3107 – Object-Oriented Systems Analysis and Design (OOAD)

### System Design Project

---

## Project Overview

The **Topic-Specific Web Crawler and Search Engine** is an Object-Oriented System Analysis and Design (OOAD) project developed as part of the **BCS 3107** course.

The system automatically crawls selected websites, extracts relevant job information, eliminates duplicate pages, indexes the collected data, and provides a searchable interface for users. The design follows software engineering best practices, UML modelling, and object-oriented principles.

---

## Project Objectives

The system aims to:

- Automatically crawl websites from administrator-provided seed URLs.
- Respect website crawling policies (`robots.txt`).
- Differentiate web pages from downloadable files.
- Prioritize URLs during crawling.
- Detect and remove duplicate pages.
- Build a searchable index of job opportunities.
- Provide fast keyword-based search.
- Generate crawler reports and statistics.

---

## Functional Requirements

- Administrator authentication
- Seed URL management
- URL prioritization
- Web crawling
- HTML parsing
- Duplicate detection
- Search indexing
- Job search
- Report generation
- Crawl monitoring

---

## Non-Functional Requirements

- High performance
- Scalability
- Security
- Reliability
- Availability
- Maintainability
- Usability

---

# Project Structure

```
WebCrawler-System/
│
├── docs/
│   ├── Part1_System_Design_Document.docx
│   ├── Part2_System_Design_Document.docx
│   └── README.md
│
├── diagrams/
│   ├── FishboneDiagram.png
│   ├── SystemArchitecture.png
│   ├── UseCaseDiagram.png
│   ├── ClassDiagram.png
│   ├── SequenceDiagram.png
│   ├── ActivityDiagram.png
│   ├── ComponentDiagram.png
│   ├── DeploymentDiagram.png
│   ├── DFD_Level0.png
│   ├── ERD.png
│   └── Wireframes.png
│
├── database/
│   └── schema.sql
│
├── src/
│   ├── crawler/
│   ├── parser/
│   ├── search/
│   ├── authentication/
│   └── utils/
│
├── tests/
│   ├── UnitTests/
│   ├── IntegrationTests/
│   ├── PerformanceTests/
│   └── SecurityTests/
│
├── screenshots/
│
└── README.md
```

---

# UML Diagrams

The project includes the following UML diagrams:

- System Architecture Diagram
- Fishbone (Root Cause Analysis)
- Use Case Diagram
- Class Diagram
- Sequence Diagram
- Activity Diagram
- Component Diagram
- Deployment Diagram
- Data Flow Diagram (Level 0)
- Entity Relationship Diagram (ERD)
- User Interface Wireframes

---

# Database Design

The database consists of the following entities:

- Users
- Seed URLs
- Crawl Queue
- Crawled Pages
- Indexed Jobs
- Crawl Logs
- Search History

Database script:

```
database/schema.sql
```

---

# Technologies Used

### Programming Languages

- Java / Python

### Database

- MySQL
- PostgreSQL

### Web Technologies

- HTML5
- CSS3
- JavaScript

### Development Tools

- Visual Studio Code
- Git
- GitHub

### UML Tools

- Draw.io
- StarUML
- Visual Paradigm

### Testing Tools

- JUnit
- Selenium
- Postman
- Apache JMeter
- OWASP ZAP

---

# Design Patterns

The system applies several Object-Oriented Design Patterns:

- Singleton Pattern
- Factory Pattern
- Strategy Pattern
- Observer Pattern
- MVC Architecture

---

# Security Features

- User Authentication
- Role-Based Access Control (RBAC)
- BCrypt Password Hashing
- HTTPS Communication
- SQL Injection Prevention
- Cross-Site Scripting (XSS) Protection
- CSRF Protection
- Audit Logging

---

# Testing

The project includes:

- Unit Testing
- Integration Testing
- System Testing
- Performance Testing
- Security Testing
- User Acceptance Testing (UAT)

Overall expected test pass rate:

**100%**

---

# Deployment

Recommended environment:

- Ubuntu Server
- Apache/Nginx
- Java or Python
- MySQL/PostgreSQL

Deployment follows a three-tier architecture:

Client → Web Server → Application Server → Database Server

---

# Future Improvements

- AI-based job recommendation
- Distributed web crawling
- Cloud deployment
- Mobile application
- REST API
- Real-time analytics dashboard
- Machine learning search ranking

---

# Learning Outcomes

This project demonstrates the application of:

- Object-Oriented Analysis and Design
- UML Modelling
- Software Engineering Principles
- Database Design
- System Architecture
- Design Patterns
- Testing Methodologies
- Secure Software Development

---


# Author

**Alvin Mwaura- BOBITNRB115221
Tabitha Wanjiru -bobinrb110625
Grace Wanjiku Thairu bobitnrb610024**

Bachelor of Business and Information Technology

St. Paul's University

---

# Supervisor

BCS 3107 – Object-Oriented Systems Analysis and Design

School of Computing and Informatics

---

# License

This project is submitted strictly for academic purposes.

© 2026 Alvin Mwaura. All Rights Reserved.
