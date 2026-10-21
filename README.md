## DR RICK

Full-stack developer based in Okinawa, Japan. I build small web products end to end
and run them myself on self-hosted Linux boxes — no managed platform in front of them.

Most of my work lives in private repositories, so this page is the index.

---

### What I run in production

| Project | What it is | Stack |
| --- | --- | --- |
| [bikrant666.com.np](https://bikrant666.com.np) | Personal site + bilingual (EN/JA) technical blog, with an admin surface and a staging environment | Flask, Postgres, nginx |
| [dropchat](https://chat.bikrant666.com.np) | Embeddable live-chat widget — drop one script tag into any site. Accounts, AI-assisted replies, transcript search | Python, Postgres, WebSocket |
| [futsal-platform](https://futsal.bikrant666.com.np) | Booking and scheduling for a futsal venue | Flask, Postgres |
| vpn-dashboard | Admin dashboard for a self-hosted WireGuard network — peer provisioning, user sync, DNS-level ad filtering | Flask, WireGuard, AdGuard |
| data-collector | Scheduled scraping and aggregation service | TypeScript, Node |
| phoenix-android-server | Headless Android automation server driven over HTTP | Python, ADB |
| signin-relay | Chat-bot relay that hands out short-lived sign-in links | Python, Google Chat API |

---

### Stack

**Languages** Python · TypeScript · JavaScript · PHP · SQL · Bash · PowerShell

**Backend** Flask · FastAPI · Node · Postgres · SQLite · REST APIs · WebSockets

**Frontend** Vanilla JS · React · Tailwind · server-rendered Jinja templates

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

Roughly 650 commits and 300k+ lines added across 12 repositories in the last four months —
mostly in Python and TypeScript. Private repos, so GitHub's graph on this page stays quiet.

---

Reach me through the contact form on [bikrant666.com.np](https://bikrant666.com.np).
