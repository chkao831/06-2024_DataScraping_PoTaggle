def aggregate_information_into_json(organization_name:str,
                                    ticker:str,
                                    release_time_quarter: str,
                                    news_release_date: str,
                                    call_date: str,
                                    market_phase: str,
                                    call_time: str,
                                    release_timezone: str,
                                    website: str,
                                    phone_number: str,
                                    passcode: str):
    """This is a function to parse information into the json format"""
    return {
                'Organization Name': {organization_name},
                'Ticker': {ticker},
                'Release Time Quarter': {release_time_quarter},
                'News Release Date': {news_release_date},
                'Call Date': {call_date},
                'MarketPhase': {market_phase}, 
                'Call Time': '{call_time}',
                'Release Timezone': '{release_timezone}',
                'Website': {website},
                'Phone Number': {phone_number},
                'Passcode': {passcode}
            }
