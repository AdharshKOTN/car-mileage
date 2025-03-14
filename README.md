# Tesla Fleet Tracker (OAuth 2.0 Integration & Vehicle Data Access)

> A personal project designed to securely access and analyze Tesla vehicle data using the official Fleet API, with a focus on clean OAuth 2.0 flow, data visibility, and scalable architecture.

---

## 🚀 Overview

This project is an in-progress **Tesla Fleet API integration**, developed as a way to better understand vehicle telemetry, battery status, and mileage logs through secure OAuth 2.0 access. It uses a clean Flask-based backend flow to authenticate with Tesla's OAuth server and retrieve API access tokens for accessing live fleet data.

I'm building this as part of a deeper goal: to **become technically self-sufficient**, break down complex systems, and deploy automation that reflects both personal curiosity and professional rigor.

---

## 🎯 Objectives

- ✅ Build a step-by-step OAuth 2.0 flow using Tesla’s Fleet API
- ✅ Authenticate using client credentials and secure redirect flow
- ✅ Retrieve access and refresh tokens from Tesla servers
- ✅ Lay the groundwork to log vehicle data like:
  - Mileage (odometer)
  - Battery level
  - Vehicle state
- 🔄 Use this as a base for further automation, scheduling, and logging on a local home server

---

## 🛠 Tech Stack

| Tool           | Purpose                                   |
|----------------|-------------------------------------------|
| `Flask`        | Lightweight backend for redirect & callback handling |
| `requests`     | Making HTTP requests to Tesla API         |
| `python-dotenv`| Manage environment variables cleanly       |
| `Tesla OAuth`  | Secure authentication and token exchange   |
| `bash`         | Supporting scripts for automation and setup |
| *(Future)*     | SQLite or CSV logging for mileage snapshots |

---

## 🧠 Why This Project Matters to Me

This project isn’t just about getting a token and hitting an API. It’s about:
- **Building from the ground up**
- **Understanding every step in a secure system**
- **Turning documentation into capability**
- **Owning my learning through full-stack responsibility**

I’m driven by clarity and the desire to work on systems that are reliable, reusable, and well understood — even when they’re hard.

---

## 🔐 OAuth Flow Summary

1. **User clicks login**
2. Redirected to Tesla’s `authorize` page
3. Tesla redirects back with a `code`
4. Flask server exchanges that code for:
   - `access_token`
   - `refresh_token`
5. Token is used to query Tesla Fleet API endpoints

---

## 🔄 Example Endpoints

- `GET /login` → Redirect to Tesla login
- `GET /callback` → Handle authorization code
- `GET /vehicle_data` (in progress) → Log or display odometer, battery level

---

## 📈 What's Next

- Add secure storage for tokens
- Add automatic token refresh flow
- Expose vehicle data in a lightweight dashboard or JSON API
- Log data periodically using scheduler or cron on my Raspberry Pi server

---

## 🤝 Collaboration & Feedback

I’m open to feedback and ideas! Whether you’ve used Tesla’s Fleet API or want to nerd out about secure token handling, hit me up.

---

## 💬 Final Note

This project is a reflection of how I work: **start with understanding, focus on flow, and build with purpose**. I'm passionate about blending backend systems with real-world devices, and this is just one step in a much larger journey toward building smart, responsive tools that serve both people and planet.