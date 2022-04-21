import pandas as pd

# At the time of production, developers.google.com/adwords maintains a csv file with a list of "Criterion Ids"
# which specify geo target locations for ad campaigns.

# Generally, we're only interested in campaigns targeting entire countries (for the purpose of our keyword research)
# It is more convenient to use 3-letter iso_country codes, so we run this script to obtain a csv which can be used a
# dictionary to look up a criterion id based on a 3-letter code.

# The csv file output will have columns "name", "iso_country_code", "location_id"

# The path for the geotargets csv file may need to be changed if the has been updated.
# A path to the geotargets csv should be linked from the URL below:
# https://developers.google.com/google-ads/api/reference/data/geotargets


def main():
    google_ads_df = pd.read_csv("https://developers.google.com/adwords/api/docs/appendix/geo/geotargets-2022-03-31.csv")
    iso_df = pd.read_csv("country_iso_codes.csv")

    google_ads_df = google_ads_df[google_ads_df["Target Type"] == "Country"]
    df = pd.merge(google_ads_df, iso_df, how="left", left_on="Country Code", right_on="Alpha-2 code")

    df = df[["Name", "Alpha-3 code", "Criteria ID"]].rename(columns={"Criteria ID": "location_id", "Name": "name", "Alpha-3 code": "iso_country_code"})

    df.to_csv("google_ads_location_ids.csv", index=False)


if __name__ == "__main__":
    main()
