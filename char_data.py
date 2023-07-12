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
        a character name using spaCy"""

        sentence_entity_list = []
        self.entity_list = []

        for i in self.doc.sents:
            for j in i.ents:
                self.entity_list.append(j.text)
            # self.entity_list = [j.text for j in i.ents] #problem here -> empty list, [] always being saved last
            sentence_entity_list.append({'sentence': i, 'character': self.entity_list})

        sentence_ent_df = pd.DataFrame(sentence_entity_list)
        print(sentence_ent_df)
        sentence_ent_df['character'] = sentence_ent_df['sentence'].apply(lambda x: self.filter_names(self.entity_list['character'], CHARACTER_DATAFRAME))
        print(sentence_ent_df)
        # self.sentence_dataframe = sentence_ent_df[sentence_ent_df['character'].map(len) > 0]
        # print(self.sentence_dataframe)


    def filter_names(self, ent_list, char_df):
        """Filter out non main character name entities"""

        return [i for i in ent_list if i in list(char_df.character_name)]



    def get_names(self):

        for i in range(self.sentence_dataframe.index[-1]):
            end_i = min(i+5, self.sentence_dataframe.index[-1])
            character_list = sum((self.sentence_dataframe.loc[i: end_i].character), [])

            self.unique_character = [character_list[i] for i in range(len(character_list))
                                     if (i==0) or character_list[i] != character_list[i-1]]

            print(self.unique_character)