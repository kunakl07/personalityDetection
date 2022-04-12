import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template
import csv
import array
import pandas
import pickle
import os
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer
import tweepy
import sys
import os
import nltk 
import re
import numpy as np
import string
import csv
from itertools import islice
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import nltk
nltk.download('stopwords')
import nltk
from unidecode import unidecode
nltk.download('punkt')



dict_personalities = {
    'INFP': 'The dreamer, INFPs are the friendly, idealistic people-understanders among the 16 personality types. They are good at being alone, think deeply about the world, make emotion-based decisions, and live spontaneously and flexibly. INFPs are good listeners, reserved with their own well-considered opinions and deeply empathetic with their fellow human beings. They have a firm moral compass, but judge kindly and with understanding. INFPs can be expected to offer creative ideas and valuable advice - but they are not the type to devise and follow the grand master plan. INFPs include writers, designers, musicians, consultants, and many other successful creatives and innovators.',
    'ENFP': "The free spirit. ENFPs are the activists among the Myers-Briggs types. They enjoy being the center of attention, analyze themselves and the world with a clear mind, but decide and act emotionally and spontaneously. Free spirits love life - and let the spark jump over to others! They can handle chaos well; rules and conventions are not their thing. The firmly established personal value system of a ENFP is usually not entirely in line with that of society; they make no secret of their sympathy for underdogs and their rejection of the wrong life. Boredom is a red rag, they like to leave the detail work to others - but that's not a problem either, because they can motivate people! ENFPs include serial founders, social movement initiators, inspirational speakers ... and many fascinating personalities who don't fit into any pigeonhole.",
    "INFJ": "The Sensei INFJ's are something like the wise visionaries in the MBTI spectrum. They rest within themselves, have a deep understanding of people and contexts, make value- and emotion-based decisions - and strive for orderly structures in their lives and actions. INFJ's can comprehensively analyze situations and thus foresee future developments with often astonishing accuracy. Advice and ideas from a INFJ have a hand and a foot - even if they are often surprising. The quiet idealists like to take life paths that accommodate their need for structure. This can be a position in an organization whose values they identify with (judge, teacher, advisor in important functions) - or a solitary lookout where they can build their edifices of thought undisturbed.",
    "ENFJ": "The charismatic leader. ENFJ's combine the analytical, idealistic, and structure-loving traits of a INFJ with a need for fellowship with others. This makes them born leaders - unlike the equally charismatic ENFPfor whom the thing quickly becomes too dull, remains a ENFJ tirelessly and can thus also motivate his fellow men in the long term. ENFJ's develop big, well-thought-out ideas and enjoy being at the forefront of a movement or organization. They are smart, empathetic leaders who take a genuine interest in the development of their people - but naturally insist on performance. Not only can they speak impressively and engage others, but they can also be hands-on. Whether in the executive suite or in the scouts -. ENFJ's almost always act as influential and popular leaders.",
    "INTJ": "The Scientist. The INTJ thinks analytically and without prejudice, makes strictly rational decisions, acts in a planned and structured manner - and prefers to be alone with his thoughts. This makes the thoughtful order lover the ideal mastermind behind the scenes. The analyses of a INTJ are precise, his plans worked out to the last detail. When it serves the greater good, his decisions can sometimes leave someone or something by the wayside.... Their profound knowledge and their often astonishing abilities predestine the perfectionistic INTJ's for careers as scientists, political advisors, management consultants or wide-ranging specialists in various other fields.",
    "ENTJ": "The Commander. ENTJ's are unprejudiced in both their thinking and their decisions, logical and rational, planned and structured in their actions - and they are great community types. What they lack in charisma, they make up for in natural authority. When all is said and done, they can prove to be surprisingly likeable raconteurs with a penchant for casual conviviality. The born leaders confidently assume responsibility and love to set the tone. Many other personality types willingly subordinate themselves to them - their competence and the value of their contributions are simply undeniable. ENTJ's are therefore often found in prominent positions (and in the history books): as CEOs, strategists and exceptional politicians, as emperors and generals.",
    "INTP": "The brooding man Not a very easy guy to INTPIn the privacy of his own home, he likes to ponder obsessively about the big picture. He wants to understand - and goes unusual, but often also unusually fruitful ways. He tends to have little sense for banalities like tidying up, making a living and irrational figures (= other personality types) - but if you don't resent his harsh comments and don't let the chaos surrounding him scare you off, you can learn a lot from him. Not everyone INTP is an Einstein - but the ranks of the brooding mavericks include scientists, philosophers and gifted programmers as well as numerous bizarre characters.",
    "ENTP": "The Debater What the INTP with himself, the ENTP on the big stage: In the competition of ideas and world views, the ENTPs and enjoy taking their fellow debaters apart by every trick in the book. The merciless analysts love to hear themselves talk and love the attention; their openness and sharp minds impress, but don't only make them friends. For long-term projects, these quickly distracted nerds lack staying power, but they're brilliant impulse generators. With the right other types on board, ENTPs are dream team members: no inconsistency in the project description escapes them, and among the ideas they liberally scatter is not infrequently a diamond in the rough.",
    "ISTJ": " The Duty Filler There are few personality types who are so often and willingly entrusted with important tasks as the ISTJ. Rather sparing with words, are ISTJ's People of action, willing and able to perform, custodians and disseminators of important factual and expert knowledge, recognized specialists - and 100 % reliable. Their manner is dry but not without humor, they are loyal friends, partners and neighbors, and are among the best types of employees imaginable. In leading positions, which they reach by their abilities but never by elbowing, they act fair, reserved and efficient.",
    "ESTJ": "The school principal The extroverted twin of the ISTJ feels a duty towards other people or society: find your life's mission ESTJs often in leading positions, where they make sure that the shop runs smoothly and no one is left behind. As pragmatists, they can capture little with lofty ideas (favorite saying: Whoever has visions should go to the doctor - and are thus a stabilizing counterweight to all NF do-gooders. The job may not always be grateful, but a ESTJ follows through. The self-confident conservative insists on following the rules and applies strict standards to others, and even stricter ones to himself. His praise is a special distinction for many, but rebels and dreamers will have a hard time with him",
    "ISFJ": "The Protector Whom a ISFJ has given his heart once, he has a friend for life. ISFJs do not play themselves into the foreground, judge the world mostly practically, have internalized social norms, judge based on feelings and values and feel most comfortable when everyone is happy and things have their harmonious order. In the family and in the close circle of colleagues or friends come ISFJ's out of themselves - and can then really perk up. No birthday goes unremembered, no unlucky person goes unconsoled. Social professions are the ISFJs' preferred metier, but their friendly, steady presence, reliability and empathy are an enrichment for every team.",
    "ESFJ": " The sympathizer Open-minded and gregarious, with a firmly held, mostly conservative worldview and lots of common sense, emotional and experiential in their decisions, and with well-ordered inner and outer lives. In the sitcom of everyday life like ESFJs sometimes be the target of good-natured jokes aimed at their perhaps not-so-sparkling remarks and stubborn insistence on conforming to norms. But that can be pretty much a matter of indifference to the born likable - because they're often the ones with the attractive partner, the good-looking kids, and the fanciest house on the block. ESFJs are the best neighbors and colleagues, unwaveringly warm and helpful. Even more than the ISFJ, they are attracted to the social professions -. ESFJs are great teachers, for example, but also good lawyers.",
    "ISFP": "The epicure The inner focus of a ISFPcoupled with sensory perception of the world, emotionality and openness makes this type a true bon vivant: no other personality type can appreciate the great and small pleasures of the world so deeply. ISFPs can't get enough of new experiences and new soulmates. Environmental degradation, ugly environments, and obvious suffering bother them differently than many other types, so you'll find a relatively large number of eco-activists (but without megaphones) and dropouts among the epicureans. Often have ISFPs have an artistic streak - they love to create beautiful things, dress decidedly unconventionally and generally place great value on aesthetics. Many ISFPs work with their hands in one way or another, office jobs are not for them at all.",
    "ESFP": " The Entertainer Among the 16 personality types, the entertainer is the one whose extroversion stands out the most. Here is someone who is truly born for the limelight. Spontaneous, light-hearted, full of energy, with a fine antenna for others - the ESFP needs and loves his audience, and the audience needs and loves him. The Enthusiasm of a ESFP is relatively easy to awaken, and its joy is contagious. The ability to carry others along and convince them is something ESFPs can put to good use in many professions and vocations. Whether it's a showman or an activist, selling luxury cars or organic vegetables at the market - as long as the ESFP enjoys it, he will shine in many positions.",
    "ISTP": "The Engineer The introverted engineer has little sense for speculation and makes head-based judgments and decisions. In his opinion, he detests senseless rules. The natural spontaneity and sensuality of ISTPs is kept in check by their head preference when making decisions: While the gut (F) types among the adventurers easily get excited about all sorts of lofty goals, the engineer likes to turn to more tangible things. ISTPs are great craftsmen - and, for example, very solid musicians. Any profession that can be broadly characterized as a craft can be ISTPs potentially fill out perfectly. If the head-based career chosen doesn't quite match their emotional preferences, a craft hobby or a challenging solo sport can provide the important balance.",
    "ESTP": "The founder The founder is the sociable engineer - with him a sober view of the world, analytical judgment, flexibility in action and a certain creative impatience come together with a great need for the bath in the crowd.The ESTP has the idea for a gimmick that makes everyday life easier, builds the prototype, founds the company, organizes the production of the sample collection - and then wins the Höhle der Löwen competition. Hesitation is not his thing, nor are far-reaching plans for the future or fundamental considerations. Optimism, technical brilliance, a solution-oriented approach and self-confident charm: this doer mentality is tailor-made for the business world; accordingly, many successful entrepreneurs are to be found there. ESTPs."
}



with open('newfrequency300.csv', 'rt') as f:
    csvReader=csv.reader(f)
    mydict={rows[1]: int(rows[0]) for rows in csvReader}

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)


regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]


def tokenize(s):
    tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
    return tokens_re.findall(s)


def check_emoticon_and_convert_to_lower(s, lowercase=False):
    tokens = tokenize(s)
    emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


def preprocess_string_NLP(s):
    s= unidecode(s)
    POSTagger=check_emoticon_and_convert_to_lower(s)
    tweet=' '.join(POSTagger)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in POSTagger:
        if w not in stop_words:
            filtered_sentence.append(w)
    
    stemmed_sentence=[]
    stemmer2 = SnowballStemmer("english", ignore_stopwords=True)

    for w in filtered_sentence:
        stemmed_sentence.append(stemmer2.stem(w))

    temp = ' '.join(c for c in stemmed_sentence if c not in string.punctuation) 
    preProcessed=temp.split(" ")
    final=[]
    for i in preProcessed:
        if i not in final:
            if i.isdigit():
                pass
            else:
                if 'http' not in i:
                    final.append(i)
    temp1=' '.join(c for c in final)
    return temp1

def getTweets(user):

    ckey='znG2TH0IgDuFRWpcsuxGR1gTY'
    csecret='PkAV2Me4JgRVyDvv5BUj4kHkWmHSNQ8aFf8Ubow0XxfWdw3qMf'
    atoken='1496973350450589715-UlE0eeqMLl1B7LbVBdfbqalHNTfxY1'
    asecret='HkTHaMnyTe9OauZxd0ZjL9H0blUc3dbkLn9odJftDg3VO'

    auth=tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api=tweepy.API(auth)

    csvFile = open('user.csv', 'a', newline='')
    csvWriter = csv.writer(csvFile)
    # try:
    for i in range(0,4):
        tweets = api.user_timeline(screen_name = user, count = 1000, include_rts=True, page=i)
        for status in tweets:
            tw=preprocess_string_NLP(status.text)
            if tw.find(" ") == -1:
                tw="blank"
            csvWriter.writerow([tw])
    # except tweepy.error.TweepError:
        # print("Failed to run the command on that user, Skipping...")
    csvFile.close()



app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict_personality", methods = ["POST"])
def predict_personality():
    
    username = request.form["twitter_handle"]
    print("Mien ho don", username)
    getTweets(username)
    
    print(username)

    
    with open('newfrequency300.csv','rt') as f:
        csvReader=csv.reader(f)
        mydict={rows[1]: int(rows[0]) for rows in csvReader}
    
    with open('user.csv','rt') as f:
        csvReader=csv.reader(f)
        print("read f/ile", csvReader)
        tweetList=[rows[0] for rows in csvReader]
    vectorizer=TfidfVectorizer(vocabulary=mydict, min_df=1)
    x=vectorizer.fit_transform(tweetList).toarray()
    print(x)
    df=pd.DataFrame(x)


    model_IE = pickle.load(open("BNIEFinal.sav", 'rb'))
    model_SN = pickle.load(open("BNSNFinal.sav", 'rb'))
    model_TF = pickle.load(open('BNTFFinal.sav', 'rb'))
    model_PJ = pickle.load(open('BNPJFinal.sav', 'rb'))

    answer=[]
    IE=model_IE.predict(df)
    SN=model_SN.predict(df)
    TF=model_TF.predict(df)
    PJ=model_PJ.predict(df)


    b = Counter(IE)
    value=b.most_common(1)
    print(value)
    if value[0][0] == 1.0:
        answer.append("I")
    else:
        answer.append("E")

    b = Counter(SN)
    value=b.most_common(1)
    print(value)
    if value[0][0] == 1.0:
        answer.append("S")
    else:
        answer.append("N")

    b = Counter(TF)
    value=b.most_common(1)
    print(value)
    if value[0][0] == 1:
        answer.append("T")
    else:
        answer.append("F")

    b = Counter(PJ)
    value=b.most_common(1)
    print(value)
    if value[0][0] == 1:
        answer.append("P")
    else:
        answer.append("J")
    mbti="".join(answer)
    print(mbti)
    return {mbti: dict_personalities[mbti]}

    #return render_template('index.html', prediction_text = 'Personality_type is $ {}'.format(dict_personalities[mbti]))

if __name__ == '__main__':
    app.run(host = "0.0.0.0", threaded = True,  port = 5000)
    username = request.form.values()
    getTweets(username)



