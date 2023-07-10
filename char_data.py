import pandas as pd
import spacy
import os

NER = spacy.load("en_core_web_sm")

class CharacterData:

    def __int__(self):
        self.character_dataframe = pd.read_csv("character_list.csv")
        self.sentence_entity_list = []
        self.all_episodes = []


    def from_episode(self):
        self.all_episodes = [i for i in os.scandir('data') if '.txt' in i.name]
        episode = self.all_episodes[0]
        episode_text = open(episode).read()
        self.doc = NER(episode_text)
        self.episode_dataframe()


    def episode_dataframe(self):
        for i in self.doc.sents:
            entity_list = [i.text for i in i.ents]
            self.sentence_entity_list.append({"sentence": i, 'character': entity_list})

        sentence_ent_df = pd.DataFrame(self.sentence_entity_list)
        print(sentence_ent_df)


    def filter_entities(self):
        pass

