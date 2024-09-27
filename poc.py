"""
Created On: 09-27-2024
Updated On: -
Author: Chaitanya Chadha
"""

import utils.utilities as ut

corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]

print("RAG POC")
user_input = input("What is your query?: ")
query_result = ut.return_response(user_input, corpus_of_documents)
print(query_result)
