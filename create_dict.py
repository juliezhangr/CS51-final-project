# create_dict.py
# CS51 final project
# Receives two lists of tokens (i.e. lists of strings), one from the spam corpus and one
# from the non-spam corpus, and creates a dictionary mapping each token
# to the probability that an email containing that token is spam

#NBAD and NGOOD are global variables which are the number of emails used in the spam and nonspam corpuses
NBAD = 5;
NGOOD = 5;

# takes an array of tokens and creates a dictionary mapping 
# each token to the number of occurrences of that token
# def _helper_dict(tokenlist):
  #  tokencount = [tokenlist.count(p) for p in tokenlist]
  #  dictionary = dict(zip(tokenlist,tokencount))
  #  return dictionary

# uses _helper_dict to create two dicts mapping words to occurrences - one for the  
# spam tokens and one for the nonspam tokens. Then uses those dicts the main dict using algorithm
# described by paul graham which maps tokens to probability that an email with that token is spam
def create_dict(spamlist, nonspamlist):
  spam_dict = count(spamlist)
  nonspam_dict = count
  (nonspamlist)
  
  # pseudocode:
   
  corpus_dict = dict(spam_dict.items() + nonspam_dict.items());

  final_dict = {}
  for key in corpus_dict.keys():
    
    # g is two times the token count of the key in the nonspam dict 
    # (or 0 if it's not in the nonspam dict)
    # we multiply by two to bias against false positives  
    g = 0
    if key in nonspam_dict:
      g = 2 * nonspam_dict[key]   

    # b is two the token count of the key in the spam dict 
    # (or 0 if it's not in the spam dict)
    b = 0
    if key in spam_dict:
      b = spam_dict[key]   
 
    # calculates the probability that each word is spam
    # 3 is an arbitrary threshold for now, will increase when corpus grows
    if g + b > 0: 
      final_dict[key] = max(0.01, min(0.99,(min(1.0, float(b)/NBAD) / (min(1.0, float(g)/NGOOD) + min(1.0, float (b)/NBAD))))) 
  
  return final_dict
