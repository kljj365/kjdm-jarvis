"""KJDM OpenJarvis Tools — all tools exported for jarvis skill install."""
from .crm_contacts import kjdm_search_contacts, kjdm_create_contact
from .crm_pipeline import kjdm_pipeline_summary, kjdm_search_opportunities
from .crm_sms import kjdm_send_bulk_sms, kjdm_send_direct_sms
from .crm_social import kjdm_schedule_social_post
from .crm_courses import kjdm_list_courses

KJDM_TOOLS = [
    kjdm_search_contacts,
    kjdm_create_contact,
    kjdm_pipeline_summary,
    kjdm_search_opportunities,
    kjdm_send_bulk_sms,
    kjdm_send_direct_sms,
    kjdm_schedule_social_post,
    kjdm_list_courses,
]

__all__ = ["KJDM_TOOLS"] + [t.__name__ for t in KJDM_TOOLS]
