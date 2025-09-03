prompts = ["living thing", "place", "pronoun", "noun", "noun", "appliance", "body part", "word (any word)", "past tense verb", "word", "past tense verb", "adjective", "adjective"]
responses = []

for wordType in prompts:
    wordInput = input("I need a " + wordType + ": ")
    responses.append(wordInput)

story = "There once was a " + responses[0] + " who lived in a(n) " + responses[1] + ". " + responses[2] + " was very happy with the " +   responses[1] + ", where the "  + responses[0] + " dwelled since they were a young " + responses[3] + "."
story_two = " Then one day, a " + responses[4] + " fell forth from the " + responses[5] + " and hit the " + responses[0] + " on the " +  responses[6] + "."
story_three = " This poor " + responses[0] + " was in so much pain that they shouted '"  + str.capitalize(responses[7]) + "!' and then " + responses[8] + "."
story_four =  "'" + str.capitalize(responses[9]) + "!', shouted the "  + responses[4] + ". I " + responses[10] + " that "  + responses[11]   + " " + responses[12]  + " " + responses[0] +". Ah well'."

print(story + story_two + story_three + story_four)