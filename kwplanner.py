from typing import List
from .clientwrapper import KeywordPlanIdeaService, KeywordPlanService
from google.ads.googleads.client import GoogleAdsClient


class KeywordPlanner:
    def __init__(self,
                 customer_id: str,
                 googleads_client: GoogleAdsClient,
                 site_url: str = None,
                 location_codes: List[str] = None,
                 language_id: str = None,
                 ):
        self.metrics = KeywordPlanService(googleads_client=googleads_client,
                                          customer_id=customer_id,
                                          location_codes=location_codes,
                                          language_id=language_id)

        self.ideas = KeywordPlanIdeaService(googleads_client=googleads_client,
                                            customer_id=customer_id,
                                            site_url=site_url,
                                            location_codes=location_codes,
                                            language_id=language_id)


def googleads_client_from_yaml(googleads_yaml_string: str) -> GoogleAdsClient:
    return GoogleAdsClient.load_from_string(yaml_str=googleads_yaml_string)


def keyword_planner_from_yaml(googleads_yaml_string: str,
                              customer_id: str,
                              site_url: str = None,
                              location_codes: List[str] = None,
                              language_id: str = None,
                              ) -> KeywordPlanner:
    googleads_client = googleads_client_from_yaml(googleads_yaml_string=googleads_yaml_string)
    return KeywordPlanner(customer_id=customer_id,
                          googleads_client=googleads_client,
                          site_url=site_url,
                          location_codes=location_codes,
                          language_id=language_id
                          )
