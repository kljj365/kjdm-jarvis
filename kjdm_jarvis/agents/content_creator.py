"""KJDM Daily Content Creator Agent — generates and schedules social posts.

Schedule in ~/.openjarvis/config.yaml:
  agents:
    - name: kjdm_content_creator
      schedule: "0 9 * * *"
      timezone: America/Chicago
"""
import datetime
from ..tools.crm_social import kjdm_schedule_social_post

# 7-day content rotation
CONTENT_ROTATION = {
    0: {  # Monday
        "theme": "Ambassador / Multiplication",
        "caption": "What if YOUR business had 100 people selling for you — and you paid them nothing until they made a sale? That's the KJDM Ambassador model. Done beats perfect. The machine is running. \n\n#KJDM #Ambassador #SmallBusiness"
    },
    1: {  # Tuesday
        "theme": "Business Owner Transformation",
        "caption": "You didn't start your business to answer phones and chase leads all day.\n\nYou built something real. Let's make sure it works for you 24/7.\n\nAutomated follow-up. Instant responses. Every lead captured — even while you sleep.\n\nThat's KJDM. You run the business. We handle everything else.\n\n#SmallBusiness #MarketingAutomation #KJDM"
    },
    2: {  # Wednesday
        "theme": "Product Spotlight",
        "caption": "Did you know you can have a fully automated marketing system for less than Netflix?\n\n$97/month. CRM, SMS, email, social scheduling, AI chat, and review management — all running while you focus on your actual business.\n\nThat's the KJDM Growth Plan. DM GROWTH to see it. \n\n#Marketing #Automation #KJDM"
    },
    3: {  # Thursday
        "theme": "STL / Local Focus",
        "caption": "St. Louis small businesses, this one's for you.\n\nYou're competing against chains with marketing budgets 100x yours. We level the playing field — AI tools, automated follow-up, and a website that actually converts.\n\nLocal pride. National-level tools. That's KJDM.\n\n#StLouis #STL #SmallBusiness #KJDM"
    },
    4: {  # Friday
        "theme": "Mindset / Motivation",
        "caption": "The plan is never complete. That's not a problem — that's the point.\n\nDone beats perfect. In motion beats in planning. The rep beats the rehearsal.\n\nStop waiting. Start moving. The machine doesn't wait for perfect — it runs.\n\n#KJDM #Mindset #Entrepreneur #DoneBeats Perfect"
    },
    5: {  # Saturday
        "theme": "Social Proof / Results",
        "caption": "One of our clients went live with their KJDM website in 24 hours. Within the first month, they got 2 new customers that paid for the whole year.\n\n$109. 24 hours. ROI in 30 days.\n\nThat's not marketing hype. That's the system working.\n\n#ClientResults #WebDesign #KJDM"
    },
    6: {  # Sunday
        "theme": "Direct CTA / Offer",
        "caption": "Free website. $97/year hosting. Live in 24 hours.\n\nThat's the KJDM Starter. No contracts. No complexity. Just your business online, working for you.\n\nDM \"WEBSITE\" or visit kljj365.com to get started today.\n\n#FreeWebsite #KJDM #SmallBusiness"
    },
}


async def run_content_creator() -> dict:
    """Generate and schedule today's KJDM social post at 9 PM CDT."""
    today = datetime.date.today()
    weekday = today.weekday()
    content = CONTENT_ROTATION[weekday]

    # Schedule for 9 PM CDT today (02:00 UTC next day)
    schedule_dt = datetime.datetime.combine(
        today + datetime.timedelta(days=1),
        datetime.time(2, 0, 0),  # 9 PM CDT = 02:00 UTC
        tzinfo=datetime.timezone.utc,
    )
    schedule_iso = schedule_dt.isoformat().replace("+00:00", "Z")

    result = await kjdm_schedule_social_post(
        caption=content["caption"],
        schedule_iso=schedule_iso,
    )

    return {
        "date": today.isoformat(),
        "theme": content["theme"],
        "scheduled_for": schedule_iso,
        "post_result": result,
    }
