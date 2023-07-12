import pandas as pd
import spacy
import os

NER = spacy.load("en_core_web_sm")
CHARACTER_DATAFRAME = pd.read_csv("character_list.csv")


class CharacterData:

    def __int__(self):
        self.all_episodes = []


    def from_episode(self):
        self.all_episodes = [i for i in os.scandir('data') if '.txt' in i.name]
        episode = self.all_episodes[1]
        episode_text = open(episode).read()
        self.doc = NER(episode_text)
        self.episode_dataframe()


    def episode_dataframe(self):
        sentence_entity_list = []
        self.entity_list = []

        for i in self.doc.sents:
            self.entity_list = [i.text for i in i.ents]
            sentence_entity_list.append({'sentence': i, 'character': self.entity_list})


        sentence_ent_df = pd.DataFrame(sentence_entity_list)
        filtered_sent_df = sentence_ent_df[sentence_ent_df['character'].map(len) > 0]
        print(filtered_sent_df)


