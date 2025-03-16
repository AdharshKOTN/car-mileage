# 🛠️ Development Log — Tesla Fleet Tracker

A chronological journal of progress and planned work for the Tesla Fleet Tracker project.

---

## 📅 March 15, 2025 — Authentication Flow + Environment Prep

**Accomplished:**
- Set up Flask server locally for handling login and callback routes.
- Implemented OAuth 2.0 login flow with Tesla’s `authorize` endpoint.
- Successfully retrieved `access_token` and `refresh_token` from Tesla.
- Investigated proper URL encoding of OAuth scopes.
- Validated that `localhost:5000` works as a redirect URI during OAuth testing.
- Explored statefulness of Flask development server.

**Learned:**
- `urlencode` behavior with tuples vs dicts
- Importance of controlling double-encoding when forming URLs
- Tesla’s OAuth flow differentiates between redirect URIs and domain validation

**Next Steps:**
- Use acquired tokens to query vehicle list and explore `/vehicles` and `/vehicle_data`
- Implement token refresh logic

---

## 📅 March 16, 2025 — Fleet API Discovery + Partner App Registration Prep

**Accomplished:**
- Identified Tesla's true Fleet API endpoint (`fleet-api.prd.na.vn.cloud.tesla.com`)
- Discovered and tested partner token acquisition via `client_credentials` grant
- Separated auth flow into two scripts: token generation and app registration
- Understood Tesla’s domain verification model: public `.pem` key hosting
- Learned why Tesla’s backend must reach a public domain (not `localhost`)
- Configured DNS settings and validated request failures due to DNS resolution

**Learned:**
- DNS resolution and why `localhost` fails for Tesla backend requests
- Tesla requires `.well-known/appspecific/com.tesla.3p.public-key.pem` hosted at public domain
- Public key ≠ secret key — PEM file must be publicly accessible by Tesla
- Difference between frontend redirect URIs vs backend domain validation
- Explored GitHub documentation strategy beyond a long `README.md`

**Next Steps:**
- Set up Cloudflare Tunnel to securely expose RPi and host PEM key
- Generate and host `secp256r1` public key at required `.well-known` path
- Register domain on Tesla Dev Portal and retry `/partner_accounts` registration
- Begin vehicle data polling after registration is complete

