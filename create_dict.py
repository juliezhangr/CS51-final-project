# create_dict.py
# CS51 final project
# Receives two lists of tokens (i.e. lists of strings), one from the spam corpus and one
# from the non-spam corpus, and creates a dictionary mapping each token
# to the probability that an email containing that token is spam


# takes an array of tokens and creates a dictionary mapping 
# each token to the number of occurrences of that token
def _helper_dict(tokenlist):
    tokencount = [tokenlist.count(p) for p in tokenlist]
    dictionary = dict(zip(tokenlist,tokencount))
    return dictionary

# uses _helper_dict to create two dicts mapping words to occurrences - one for the  
# spam tokens and one for the nonspam tokens. Then uses those dicts the main dict using algorithm
# described by paul graham which maps tokens to probability that an email with that token is spam
def create_dict(spamlist, nonspamlist)
  spam_dict = _helper_dict(spamlist)
  nonspam_dict = _helper_dictnonspamlist)
  
  # pseudocode:
  # create new dictionary corpusdict 
  # for each word which appears in either spam_dict or nonspam_dict:
      # g = tokencount of that word in the nonspam_Dict times 2
      # b = lookup the tokencount of that word in the spam_dict
      # nbad = number of emails used to create spam_dict
      # ngood = number of emails used to create nonspam_dict
      # if g + b > 5:
            # word(key) =  min(1, b/nbad) / (min(1, b/nbad) + min(1, g/ngood))  
      # return corpusdict
