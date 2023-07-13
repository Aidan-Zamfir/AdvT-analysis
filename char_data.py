import matplotlib.pyplot as plt
from pathlib import Path
import networkx as nx
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
        #should add method to itterate over each episode,
        #create df of all epsiodes,
        #and compare data from all.

        self.all_episodes = [i for i in os.scandir('data') if '.txt' in i.name]
        episode = self.all_episodes[10]
        episode_text = open(episode).read()
        self.doc = NER(episode_text)
        self.episode_dataframe()


    def episode_dataframe(self):
        """Create data frame with only sentences which contain
        a character name using spaCy"""

        sentence_entity_list = []
        self.entity_list = []

        for i in self.doc.sents:
            self.entity_list = [j.text for j in i.ents]
            sentence_entity_list.append({'sentence': i, 'character': self.entity_list})
            sentence_ent_df = pd.DataFrame(sentence_entity_list)

        sentence_ent_df['character'] = sentence_ent_df['character'].apply(lambda x: self.filter_names(x, CHARACTER_DATAFRAME))
        self.sentence_dataframe = sentence_ent_df[sentence_ent_df['character'].map(len) > 0]


    def filter_names(self, ent_list, char_df):
        """Filter out non 'main character' entities"""

        return [i for i in ent_list if i in list(char_df.character_name)]


    def get_names(self):
        """Filter through character entities &
        create a relationship dataframe"""


        self.relation_ships = []

        for i in range(self.sentence_dataframe.index[-1]):
            end_i = min(i+5, self.sentence_dataframe.index[-1])
            character_list = sum((self.sentence_dataframe.loc[i: end_i].character), [])

            self.unique_character = [character_list[i] for i in range(len(character_list))
                                     if (i==0) or character_list[i] != character_list[i-1]]

            #compare character 'a' with 'b'
            if len(self.unique_character) > 1:
                for idx, a in enumerate(self.unique_character[:-1]):
                    b = self.unique_character[idx +1]
                    self.relation_ships.append({'source': a, 'target': b,})

        self.relationship_df = pd.DataFrame(self.relation_ships)
        self.relationship_strength()

    def relationship_strength(self):
        """Remove duplicate relationships & create
        relationship weight between characters in df"""

        self.relationship_df['value'] = 1
        self.relationship_df = self.relationship_df.groupby(['source','target'], sort=False, as_index=False).sum()

    def network_rel(self):
        G = nx.from_pandas_edgelist(self.relationship_df, source='source',
                                    target='target', edge_attr='value', create_using=nx.Graph())

        pos = nx.kamada_kawai_layout(G)
        nx.draw(G, with_labels=True, node_color='blue', edge_cmap=plt.cm.Blues, pos=pos)
        plt.show()

    def run(self):
        self.from_episode()
        self.get_names()
        self.network_rel()