# 🏥 Inclusive Digital Health (SNI)

![HTML](https://img.shields.io/badge/Code-HTML-orange?logo=html5)
![CSS](https://img.shields.io/badge/Style-CSS-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/Logic-JavaScript-yellow?logo=javascript)
![Python](https://img.shields.io/badge/Backend-Python-green?logo=python)
![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20compliant-brightgreen)
![Centrale Lille](https://img.shields.io/badge/Made%20at-Centrale%20Lille-red)

---

## 🩺 Description
**Inclusive Digital Health (SNI)** — also known as **Accessillage** — is a student project developed at **Centrale Lille (2023–2025)** in collaboration with the **CRIStAL Laboratory (OSL team)**, **SIB (publisher of Sillage)**, **CHU de Lille**, and **APF France Handicap**.  
The goal is to make hospital management software accessible to **visually impaired and dyslexic healthcare professionals** through inclusive interface design and adaptive assistive technologies.  

The project delivers a functional prototype, **Accessillage**, compliant with **WCAG 2.1** and **RGAA 4.1** accessibility standards, featuring a **Confidential Mode** that ensures data privacy for screen-reader users.  

---

## 📑 Table of Contents
1. [Description](#-description)  
2. [Installation](#-installation)  
3. [Usage](#-usage)  
4. [Project Structure](#-project-structure)  
5. [Technologies / Stack](#-technologies--stack)  
6. [Results](#-results)  
7. [Contributors](#-contributors)  
8. [License](#-license)  
9. [Future Improvements](#-future-improvements)  

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/inclusive-digital-health.git
   cd inclusive-digital-health
   ```
2. Launch the project locally (example with Python):
   ```bash
   python -m http.server
   ```
3. Open your browser at:
   ```
   http://localhost:8000
   ```

---

## 🖱️ Usage
- Navigate the interface using **keyboard-only controls** (no mouse required).  
- Activate **Confidential Mode** to protect sensitive data:  
  - `Ctrl + Shift + M` (Windows/Linux)  
  - `Cmd + Shift + M` (MacOS)  
- Screen readers (NVDA, VoiceOver) automatically adapt to the selected mode.  
- All features remain accessible with or without assistive technologies.  

---

## 🧱 Project Structure
```
Accessillage/
│
├── backend/                      # Server-side logic
│   ├── config/                   # Configuration files (database, environments, etc.)
│   ├── controllers/              # Business logic: request handling and model interactions
│   ├── models/                   # Data schemas and database definitions
│   └── routes/                   # API endpoints for frontend communication
│
├── frontend/                     # Client-side interface
│   ├── assets/                   # Shared static resources
│   │   ├── images/               # Application images and icons
│   │   ├── scripts/              # JavaScript files for specific features
│   │   └── styles/               # CSS or SCSS style files
│   │
│   ├── components/               # Reusable UI components
│   └── pages/                    # Main application pages
│
└── docs/                         # Technical and user documentation
```

---

## 💻 Technologies / Stack

| Category | Tools / Technologies |
|-----------|----------------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python |
| **Design & Mockups** | Figma |
| **Accessibility** | ARIA attributes, WCAG 2.1, RGAA 4.1 |
| **Assistive Tools** | NVDA, VoiceOver |
| **Methodology** | Agile workflow, UX testing, heuristic evaluation |

---

## 📈 Results
- Achieved **90% accessibility and UX score**.  
- Validated by **visually impaired healthcare professionals** and **accessibility experts**.  
- Developed a **Confidential Mode** ensuring screen-reader data protection.  
- Delivered **complete documentation**: technical guide, user manual, and accessibility report.  

---

## 👥 Contributors
**Team SNI – Centrale Lille (2023–2025)**  
Supervisors: *S. Hammadi*, *S. Ben Othman*  
Partners: *CRIStAL Laboratory (OSL)*, *SIB*, *CHU de Lille*, *APF France Handicap*  

**Team Members:**
- Clément Marie  
- Maxime Fauchere--Collin  
- Shuyan Zhang  
- Lucas Royanez  
- Baptiste Sorel  
- Yuxiao Wang  
- Pierre-Henri Landrin  
- Zineb Ferhoun  
- Thomas Delplace  
- Pierre Le Gall  
- Gabriel Dalla Corte  
- Samy Benzaim  

---

## 📄 License
This project is distributed under an **academic open license** for research and educational purposes.  
You may reuse or adapt the code with proper attribution.

---

## 🔮 Future Improvements
- Integration of **Accessillage** features into the **Sillage** platform (SIB).  
- Continued development under the **CRIStAL OSL Laboratory**.  
- Participation in the **Handicap & Technology Challenge (ENI Metz, 2025)**.  
- Exploration of **AI-driven adaptive accessibility systems** for personalized user experiences.  
