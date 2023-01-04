# googleads_api_wrapper
A python wrapper for the google ads api python library, including Keyword Plan Service and Keyword Plan Idea Service.

A YAML file must be obtained for you own Google Ads Keyword Planner account. A `KeywordPlanner` object can then be created by reading in the file.

`keyword_planner: KeywordPlanner = kwplanner.keyword_planner_from_yaml(googleads_yaml_string)`


`KeywordPlanner` has two main attributes: 
 - `KeywordPlanner.metrics`
 - `KeywordPlanner.ideas`