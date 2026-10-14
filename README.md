# KJDM Jarvis

> **Local-first AI command center for Kyle Johnson Digital Marketing**
> Powered by [OpenJarvis](https://github.com/open-jarvis/OpenJarvis) × [copilot.kljj365.com](https://copilot.kljj365.com)

---

## What This Does

KJDM Jarvis gives you a desktop AI agent that runs **locally on your machine** and has direct access to your CRM, pipeline, SMS, social media, and course library.

| Tool | What It Does |
|------|--------------|
| `kjdm_search_contacts` | Search CRM contacts by name, email, phone, or company |
| `kjdm_create_contact` | Create new CRM contacts with tags |
| `kjdm_pipeline_summary` | Live pipeline counts and values per stage |
| `kjdm_search_opportunities` | Find deals by name, stage, or contact |
| `kjdm_send_bulk_sms` | Send bulk SMS campaigns to contact lists |
| `kjdm_send_direct_sms` | Send a personal SMS to one contact |
| `kjdm_schedule_social_post` | Schedule posts to Facebook, Instagram, LinkedIn, Threads, Bluesky |
| `kjdm_list_courses` | List all KJDM ambassador training courses |

---

## Quick Setup

```bash
# 1. Install OpenJarvis
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash

# 2. Install the KJDM skill
jarvis skill install kljj365/kjdm-jarvis

# 3. Set your token
cp .env.example .env
# Edit .env: set KJDM_AI_TOKEN

# 4. Apply KJDM brand theme
cp kjdm_jarvis/theme/kjdm.css ~/.openjarvis/themes/kjdm.css
# In ~/.openjarvis/config.yaml set: theme: kjdm

# 5. Launch
jarvis gui
```

---

## Brand Colors

| Token | Value |
|-------|-------|
| Background | `#090911` |
| Primary (orange) | `#F97316` |
| Text | `#F0F0FF` |
| Font | Inter / JetBrains Mono |

---

## Agents

| Agent | Role |
|-------|------|
| `kjdm_sales_agent` | Pipeline management, deal moves, SMS outreach |
| `kjdm_content_agent` | Daily social content scheduling |
| `kjdm_ambassador_agent` | Ambassador contacts + course access |

---

Built by Kyle Johnson — [kljj365.com](https://kljj365.com) · [copilot.kljj365.com](https://copilot.kljj365.com)
