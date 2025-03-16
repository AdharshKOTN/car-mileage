# Tesla Fleet Tracker (OAuth 2.0 Integration & Vehicle Data Access)

> A personal project to securely access and analyze Tesla vehicle data using the official Fleet API, with a focus on OAuth 2.0 flows, authentication, and data architecture.

---

## 🚀 Overview

Tesla Fleet Tracker is a self-hosted platform that integrates with Tesla’s Fleet API to retrieve live vehicle data (such as odometer readings, battery level, and state) using a secure authentication process. It runs on a Raspberry Pi server and is designed to be modular, scalable, and extensible for home automation or logging use cases.

---

## 🎯 Project Goals

- Implement Tesla’s OAuth 2.0 flow using Flask and Python
- Retrieve and securely store access/refresh tokens
- Authenticate as a registered partner application
- Query the Fleet API for real-time vehicle data
- Design for eventual dashboard visualization and scheduled logging

---

## 🛠 Tech Stack

| Tool           | Purpose                                           |
|----------------|---------------------------------------------------|
| `Flask`        | Handles login, callback, and local server logic  |
| `requests`     | Performs HTTPS API calls                         |
| `Tesla OAuth`  | Supports secure token exchange                   |
| `bash`         | Assists with setup and token automation          |
| `Cloudflare`   | Tunnel to securely expose the local server       |
| *(Planned)*    | SQLite or CSV for vehicle log persistence        |

---

## 🔐 OAuth Flow Summary

1. User starts login on local Flask server
2. Redirected to Tesla's OAuth authorize endpoint
3. Tesla redirects back with a one-time code
4. Flask server exchanges code for access and refresh tokens
5. Server makes authorized API requests using the token

---

## 📦 Fleet API Endpoints

| Endpoint                 | Description                         |
|--------------------------|-------------------------------------|
| `/api/1/vehicles`        | Returns list of vehicles            |
| `/api/1/vehicle_data`    | Returns vehicle telemetry (planned) |
| `/api/1/partner_accounts`| Registers app with Tesla backend    |

---

## 📁 Documentation Structure

See the [`/docs`](./) directory for:

- `architecture.md` — App/server structure
- `authentication.md` — Token flow & client secrets
- `partner-registration.md` — PEM key setup and Tesla domain linking
- `vehicle-api.md` — Vehicle data endpoints & usage
- `development-log.md` — Progress notes & future plans

---

## 🔍 Status

This project is under active development and infrastructure setup. 
Token exchange and initial endpoint testing are functional. Partner registration and vehicle telemetry access in progress.

---

## 🤝 Feedback & Contributions

While this is a personal learning project, insights, suggestions, and shared experience with Tesla’s APIs are welcome.

---

## 🌱 About This Project

Tesla Fleet Tracker reflects a hands-on approach to systems understanding and secure integration. It represents a growing skillset in API work, backend engineering, and infrastructure visibility.
