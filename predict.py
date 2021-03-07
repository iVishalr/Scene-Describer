from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re
import json
import sys

def load_json():
    with open('../vis.json', 'r') as data_file:
        json_data = data_file.read()
    data = json.loads(json_data)
    timestamps_dict = dict()
    for timestamp in data:
        key_temp = timestamp["image_id"]
        key = ""
        for letters in key_temp:
            if letters == '-':
                key = key+":"
            else:
                key+=letters
        key = key[:-4]
        timestamps_dict[key] = timestamp["caption"]
    return timestamps_dict

def predict(time_stamps):
    def pre_process(s):
        temp = s
        extract_weighted_words = [words.lower() for words in temp.split() if words.isupper()]
        s=s.lower()
        s = s.replace(r'[^\w\d\s]', ' ')
        s = s.replace(r'\s+', ' ')
        s = s.replace(r'^\s+|\s+?$', '')
        s = s.replace(',','')
        s = s.replace('.','')
        for i in range(len(extract_weighted_words)):
            extract_weighted_words[i] = extract_weighted_words[i].replace(r'[^\w\d\s]', ' ')
            extract_weighted_words[i] = extract_weighted_words[i].replace(r'\s+', ' ')
            extract_weighted_words[i] = extract_weighted_words[i].replace(r'^\s+|\s+?$', '')
            extract_weighted_words[i] = extract_weighted_words[i].replace(',','')
            extract_weighted_words[i] = extract_weighted_words[i].replace('.','')
        words = word_tokenize(s)
        stop_words = set(stopwords.words("english"))
        filteredSentence = list()
        filtered_weighted = []
        for w in words:
            if w not in stop_words:
                filteredSentence.append(w)
        for w in extract_weighted_words:
            if w not in stop_words:
                filtered_weighted.append(w)
        lemmaSentence = list()
        lemmaWeighted = []
        wordnet_lemmatizer = WordNetLemmatizer()
        for w in filteredSentence:
            lemmaSentence.append(wordnet_lemmatizer.lemmatize(w))
        for w in filtered_weighted:
            lemmaWeighted.append(wordnet_lemmatizer.lemmatize(w))
        return lemmaSentence,lemmaWeighted
    def get_similarity (X_set,Y_set):
        rvector = X_set + Y_set
        l1 =[];l2 =[]
        for w in rvector: 
            if w in X_set: l1.append(1) # create a vector 
            else: l1.append(0) 
            if w in Y_set: l2.append(1) 
            else: l2.append(0) 
        c = 0
        # cosine formula  
        for i in range(len(rvector)): 
                c+= l1[i]*l2[i] 
        cosine = c / float((sum(l1)*sum(l2))**0.5) 
        return cosine*100

    for key,value in time_stamps.items():
        time_stamps[key],_ = pre_process(value)
    # print(sys.argv[1])
    s, weighted_words = pre_process(sys.argv[1])
    print("WEIGHTED-WORDS",weighted_words)
    for key in time_stamps:
        i = 0
        for words in weighted_words:
            if words.lower() in time_stamps[key] and i<3:
                temp = [words.lower(),words.lower(),words.lower()]
                time_stamps[key] = time_stamps[key]+ temp[:3-i]
                i+=1
    #print(time_stamps)
    frequency_count = {}
    max_freq = 0
    average_similarity = dict()
    max_similarity = 0
    for timestamps in time_stamps:
        similarity = get_similarity(list(set(s)),list(time_stamps[timestamps]))
        if(max_similarity<similarity):
            max_similarity = similarity
        average_similarity[timestamps] = similarity
    flag = 1
    flag1=True
    # print(average_similarity)
    # print(max_similarity)
    TimeStamps = dict()
    TimeStamps["Time_Stamps"] = []
    TimeStamps["Recommended"] = ""
    for time in average_similarity:
        if max_similarity == 0.0:
            break
        if average_similarity[time] == max_similarity and flag1:
            TimeStamps["Recommended"] = time
            flag = 0
            flag1=False
        if average_similarity[time] >= 60.0 and average_similarity[time] != max_similarity:
            TimeStamps["Time_Stamps"].append(time)
    # print(TimeStamps)
    if(flag):
        print("No suitable timestamp")
    with open('../timestamp.json', 'w') as f:
        json.dump(TimeStamps, f, sort_keys=True)
    f.close()
vis_dict = load_json()
predict(vis_dict)
