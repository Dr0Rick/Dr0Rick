## DR RICK

Full-stack developer based in Okinawa, Japan. I build small web products end to end
and run them myself on self-hosted Linux boxes — no managed platform in front of them.

Most of my work lives in private repositories, so this page is the index.

---

### What I run in production

| Project | What it is | Stack |
| --- | --- | --- |
| [bikrant666.com.np](https://bikrant666.com.np) | Personal site + bilingual (EN/JA) technical blog, with an admin surface and a staging environment | FastAPI, Postgres, React/Vite |
| [dropchat](https://chat.bikrant666.com.np) | Embeddable live-chat widget — drop one script tag into any site. Accounts, AI-assisted replies, transcript search | FastAPI, Postgres, WebSocket |
| [futsal-platform](https://futsal.bikrant666.com.np) | Booking and scheduling for a futsal venue | FastAPI, Postgres |
| vpn-dashboard | Admin dashboard for a self-hosted WireGuard network — peer provisioning, user sync, DNS-level ad filtering | FastAPI, WireGuard, AdGuard |
| data-collector | Scheduled scraping and aggregation service | TypeScript, Node |
| phoenix-android-server | Headless Android automation server driven over HTTP | Python, ADB |
| signin-relay | Chat-bot relay that hands out short-lived sign-in links | Python, Google Chat API |

---

### Stack

**Languages** Python · TypeScript · JavaScript · PHP · SQL · Bash · PowerShell

**Backend** FastAPI · Uvicorn · Node · Postgres · SQLite · REST APIs · WebSockets

**Frontend** React · TypeScript · Vite · Tailwind

**Infrastructure** Oracle Cloud (ARM + AMD) · Ubuntu · nginx · systemd · WireGuard ·
Cloudflare DNS/TLS · GitHub Actions · rsync deploys · Adminer

**Practices** Conventional commits · PR-per-change on the main project · health-endpoint
checks after every deploy · Telegram/chat control planes for long-running bots

---

### How I work

- **Ship to a real box.** Every project above is reachable on a URL right now, not a demo gif.
- **Operate what I build.** Provisioning, TLS, DNS, backups, monitoring and the 1 GB
  memory ceiling are part of the job, not someone else's.
- **Automate the boring part.** Scheduled jobs, scrapers and bots that run unattended
  for months, with a chat command surface so they can be paused without an SSH session.
- **Verify live.** A green CI run is not a deploy; a health endpoint answering 200 is.

---

### Numbers

582 contributions in 2026 — 479 commits, 90 pull requests and 13 repositories created —
against roughly 327,000 lines added and 16,000 deleted. Mostly Python and TypeScript,
across 55 active days at about 10 commits a day.

Nearly all of it sits in private repositories, which is why this page exists as the index.

---

### Writing

I keep a bilingual technical blog at [bikrant666.com.np](https://bikrant666.com.np) —
English and 日本語, roughly 45 posts in each. They are practical how-to guides pulled
straight out of the work above: provisioning a VM from nothing, wiring TLS and DNS,
and keeping a FastAPI app and a Postgres instance alive together on a 1 GB box.

---

Reach me through the contact form on [bikrant666.com.np](https://bikrant666.com.np).
