import pandas as pd
import spacy
import os

NER = spacy.load("en_core_web_sm")
CHARACTER_DATAFRAME = pd.read_csv("character_list.csv")


class CharacterData:

    def __int__(self):
        self.all_episodes = []
        self.window_size = 5


    def from_episode(self):
        """Extract epsiode transcript from data folder"""

        self.all_episodes = [i for i in os.scandir('data') if '.txt' in i.name]
        episode = self.all_episodes[1]
        episode_text = open(episode).read()
        self.doc = NER(episode_text)
        self.episode_dataframe()


    def episode_dataframe(self):
        """Create data frame with only sentences which contain
        a character name using NLP"""

        sentence_entity_list = []
        self.entity_list = []

        for i in self.doc.sents:
            self.entity_list = [i.text for i in i.ents]
            sentence_entity_list.append({'sentence': i, 'character': self.entity_list})

        sentence_ent_df = pd.DataFrame(sentence_entity_list)
        self.sentence_dataframe = sentence_ent_df[sentence_ent_df['character'].map(len) > 0]


    def get_names(self):

        for i in range(self.sentence_dataframe.index[-1]):
            end_i = min(i+5, self.sentence_dataframe.index[-1])
            character_list = sum((self.sentence_dataframe.loc[i: end_i].character), [])

            self.unique_character = [character_list[i] for i in range(len(character_list))
                                     if (i==0) or character_list[i] != character_list[i-1]]

            print(self.unique_character)