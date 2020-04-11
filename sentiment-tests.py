from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

train = [("Is your name Enquirer?", "inquisitive"), ("How dare you be named Enquirer!", "outrage"), ("You can't be named Enquirer...", "doubt")]
desired_emotions = ["inquisitive"]

def evaluate_message(message, dataset, desired_emotions, neg_limit, partisan_limit, censor_mode=False):
#    full_message = TextBlob(message)
    cl = NaiveBayesClassifier(dataset)
    classified_message = TextBlob(message, classifier=cl)

    if censor_mode == True:
        final_message = []
        for s in classified_message.sentences:
            print(s)
            print(s.sentiment)
            print(s.classify())
            if (s.classify() in desired_emotions) and (s.sentiment[0] > neg_limit) and (abs(s.sentiment[1]) <  partisan_limit):
                final_message.append(str(s))
        return " ".join(final_message)
    else:
        print (classified_message)
        print (classified_message.sentiment)
        print (classified_message.classify())
        if (classified_message.classify() in desired_emotions) and (classified_message.sentiment[0] > neg_limit) and (abs(classified_message.sentiment[1]) <  partisan_limit):
            return True
        else:
            return False

print("\n%s" % evaluate_message("I freaking hate you. What's your name?", train, desired_emotions, -0.5, 1, censor_mode=False))
