import twitter

api = twitter.Api(consumer_key='yoiO2TaQieEEPqYnxc1Z2psMa',
                      consumer_secret='z7iZvzznu4mOZdtW0Tmkcuzf2BSpNbzixnaZ9qeTrNVInCfFoh',
                      access_token_key='3248255634-prUKd6kdkXGBMmZxmDcya1LEEZ6zKKLPCA79eqV',
                      access_token_secret='O31W2rtfAnc3KWdakedNJcEOzoomzVuoiufVZqAdJQGQQ')

print api.VerifyCredentials()

statusTweets = api.GetUserTimeline(screen_name='nesh170',count=2)
print [str(s.text) for s in statusTweets]
