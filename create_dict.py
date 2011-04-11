import helper_dict

# create_dict.py
# CS51 final project
# Receives two lists of tokens (i.e. lists of strings), one from the spam corpus and one
# from the non-spam corpus, and creates a dictionary mapping each token
# to the probability that an email containing that token is spam

def _helper_dict(spamlist, nonspamlist)

  spam_dict = helper_dict.create(spamlist)
  nonspam_dict = helper_dict.create(nonspamlist)

  # use graham's method to turn that into one hashtable
  #    
