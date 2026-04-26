# 🎓 IT Student Management System

A full-stack, role-based web application designed to centralize and simplify academic and administrative operations in educational institutions.

---

## 📌 Project Overview

The **IT Student Management System (IT-SMS)** is a web-based platform that integrates multiple academic processes into a single unified system. It replaces fragmented, manual, or disconnected tools used by schools for managing student data, attendance, grades, and learning materials.

This project was developed over **13 weeks using Agile Scrum methodology**, delivering a complete, tested, and functional system.

---

## 🚨 Problem Statement

Many educational institutions, especially in developing regions, rely on:

* Paper-based systems
* Multiple disconnected tools
* Manual data handling

This leads to:

* Poor data accessibility
* Increased workload for teachers/admins
* Lack of transparency for students and parents

This system solves that by providing **one centralized platform**.

---

## 🎯 Objectives

* Build a unified academic management system
* Implement **role-based access control (RBAC)**
* Enable real-time data access across users
* Ensure system security and usability
* Deliver within a fixed 13-week timeline

---

## 👥 Target Users

| Role        | Responsibilities                                  |
| ----------- | ------------------------------------------------- |
| **Admin**   | Manage users, assign roles, oversee system        |
| **Teacher** | Upload materials, record attendance, enter grades |
| **Student** | View grades, attendance, download materials       |
| **Parent**  | Monitor student performance (read-only)           |

---

## ⚙️ Tech Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Backend         | Django (Python)       |
| Database        | SQLite                |
| Frontend        | HTML, CSS             |
| Version Control | Git & GitHub          |
| Auth System     | Django Authentication |

---

## 🧠 System Features

* 🔐 Role-Based Authentication (Admin, Teacher, Student, Parent)
* 📁 File Upload & Class-Based Resource Access
* 📊 Attendance Tracking System
* 📝 Grade Management System
* 🧑‍💼 Admin Dashboard for User Management
* 📂 Centralized Database Integration

---

## 🏗️ System Architecture

The system follows the **Django MVT (Model-View-Template)** architecture with a shared database.

Core Entities:

* User
* StudentProfile
* Class
* Resource
* Attendance
* Grade

*(Based on architecture described in closure report, Appendix D)* 

---

## 🔄 Development Methodology

This project followed **Agile Scrum**:

* 4 Sprints (2 weeks each)
* Sprint Planning → Development → Review → Retrospective

### Sprint Breakdown

| Sprint   | Focus                                |
| -------- | ------------------------------------ |
| Sprint 1 | Authentication & Student Profiles    |
| Sprint 2 | Learning Services (file upload)      |
| Sprint 3 | Teacher Module (attendance & grades) |
| Sprint 4 | Admin Panel & Integration            |

*(Confirmed in project execution summary)* 

---

## 📅 Project Timeline

| Phase       | Duration    |
| ----------- | ----------- |
| Planning    | Week 1      |
| Design      | Week 2      |
| Development | Weeks 3–10  |
| Testing     | Weeks 11–12 |
| Deployment  | Week 13     |

---

## 💰 Budget

Total estimated cost: **~$1400–$1600 AUD**

Breakdown:

* Laptop: $1200
* Utilities: $100
* Misc: $100
* Software: $0 (Open Source)

The project achieved **high cost efficiency using free tools** 

---

## 🧪 Testing & Validation

All major testing phases were completed successfully:

* ✅ Functional Testing
* ✅ Integration Testing
* ✅ Security Testing
* ✅ User Acceptance Testing (UAT)

No critical failures were reported during final validation 

---

## ⚠️ Challenges Faced

* Solo project (handled all roles alone)
* Complex access control implementation
* Cross-module data integration
* Initial database design limitations

You addressed these using:

* Agile sprint planning
* Centralized permission logic
* Iterative debugging

*(Detailed in reflection report)* 

---

## 🏆 Key Achievements

* Built full system **end-to-end in 13 weeks**
* Implemented secure RBAC system
* Delivered all planned features on time
* Achieved stable, tested system
* Maintained cost efficiency using open-source tools

---

## 🚫 Limitations

* Not mobile responsive
* Uses SQLite (not scalable for large users)
* No cloud deployment
* No notification system
* No analytics dashboard

*(From closure report limitations section)* 

---

## 🚀 Future Improvements

* PostgreSQL migration
* Cloud deployment (AWS/Heroku)
* Mobile-responsive UI
* Notification system
* Analytics dashboard
* Multi-language support


---

## 🔗 GitHub Repository

👉 Add your repo link here

---

## 📘 Documentation

This project includes:

* Project Closure Report
* Reflection Report
* Presentation Slides

---

## 🙌 Final Thoughts

This project demonstrated that:

* Planning is harder than coding
* Agile works best with iteration
* Feedback improves usability
* Real-world systems require integration thinking

You successfully built a **production-ready academic system** as a solo developer within a fixed timeline.

---

## 📚 References

* Agile Manifesto
* Django Documentation
* Scrum Guide
* Software Engineering (Sommerville)
* PMBOK Guide

---

##figma Link

https://www.figma.com/proto/ATaesFDNO2W7KKbvlOZPJ0/SPMS?node-id=0-1&t=VEXuez6CPFlRFneM-1
