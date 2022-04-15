import app as a
from app import app
import unittest
# from unittest.mock import MagicMock
import json
from flask import Flask

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




class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

    def test_tokenize(self):
        tokenized_string = a.tokenize("This is book")
        assert tokenized_string[0] == "This"
        assert tokenized_string[1] == "is"
        assert tokenized_string[2] == "book"

    def test_check_emoticon_and_convert_to_lower(self):
        #happy emoji
        emoji_array = a.check_emoticon_and_convert_to_lower("^_^")
        assert emoji_array[0] == "^"
        assert emoji_array[1] == "_"
        assert emoji_array[2] == "^"

    def test_preprocess_string_NLP(self):
        string_without_emojis_and_uppercases = a.preprocess_string_NLP("The NonOkay String ^_^ $_$")
        assert string_without_emojis_and_uppercases == "the nonokay string"
        




    def test_personality_predict(self):
        x = {"username":"@avkc007"}
        y = json.dumps(x)

        response = app.test_client().post('/predict_personality', data = y, content_type = 'application/json')
        data = json.loads(response.get_data(as_text=True))
        assert data['title'] == 'INFJ'
        assert data["description"] == dict_personalities['INFJ']
        try:
            json_obj = data
            print("A valid JSON")
        except ValueError as e:
            print("Not a valid JSON")


        
        # mock_predict_personality = mock.Mock(return_value = y)
        # tester = app.test_client(self)
        # response = tester.get('/predict_personality', content_type='html/text')
        # self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()