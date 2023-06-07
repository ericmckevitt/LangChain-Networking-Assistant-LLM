import os
import requests


def scrape_linkedin_profile(linked_profile_url: str):
    """
    Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """

    # Everything needed to send request
    api_endpoint = f"https://nubela.co/proxycurl/api/v2/linkedin?url={linked_profile_url}&fallback_to_cache=on-error&use_cache=if-present&skills=include&inferred_salary=include&personal_email=include&personal_contact_number=include&twitter_profile_id=include&facebook_profile_id=include&github_profile_id=include&extra=include"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # Make the request
    response = requests.get(
        api_endpoint, params={"url": linked_profile_url}, headers=header_dic
    )

    # Clean payload to reduce token count
    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
