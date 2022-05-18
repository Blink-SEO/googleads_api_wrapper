from typing import List
from .clientwrapper import KeywordPlanIdeaService, KeywordPlanService


class KeywordPlaner:
    def __init__(self,
                 googleads_client,
                 customer_id: str,
                 site_url: str,
                 location_codes: List[str] = None,
                 language_id: str = None,
                 ):
        self.ideas = KeywordPlanIdeaService(googleads_client=googleads_client,
                                            customer_id=customer_id,
                                            site_url=site_url,
                                            location_codes=location_codes,
                                            language_id=language_id)

        self.metrics = KeywordPlanService(googleads_client=googleads_client,
                                          customer_id=customer_id,
                                          location_codes=location_codes,
                                          language_id=language_id)
