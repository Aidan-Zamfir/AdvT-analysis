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
        print(sentence_ent_df)
        print("=======================") #works up to this point. Bellow is error
        sentence_ent_df['character'] = sentence_ent_df['sentence'].apply(lambda x: self.filter_entities(self.entity_list, CHARACTER_DATAFRAME))

        print(sentence_ent_df)


    def filter_entities(self, entity_list, character_df):
        return [i for i in entity_list if i in list(character_df.character_name)]

