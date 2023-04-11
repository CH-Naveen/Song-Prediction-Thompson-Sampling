import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from playlist_selection import PlayListSelection

class SongPredict:

    index =0
    def main(self):
        sp = SongPredict()
        
        d = 4
        given_playlist = [1, 2, 3, 4]
        playlist_name = {1: 'dinner_track',
                    2: 'party_track',
                    3: 'sleep_track',
                    4: 'workout_track'}
        songs_selected = []
        numbers_of_rewards_1 = [0] * d
        numbers_of_rewards_0 = [0] * d
        total_reward = 0
        for _ in range(0, 10000):
            song = 0
            max_random = 0
            for i in range(0, d):
                random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
                if random_beta > max_random:
                    max_random = random_beta
                    song = i
            
            songs_selected.append(song)
            print("")
            print('%s playlist was recomended in the previous stage' % playlist_name.get(song))
            reward = sp.playlist_choosen(given_playlist, 0, song)
            if reward == 1:
                numbers_of_rewards_1[song] = numbers_of_rewards_1[song] + 1
            else:
                numbers_of_rewards_0[song] = numbers_of_rewards_0[song] + 1 
                
            total_reward = total_reward + reward


    def playlist_choosen (self,given_playlist,previous_playlist,play_list):
        sp= SongPredict()


        if play_list !=0:

            p1 = PlayListSelection(play_list)
            song_name, artist, genere = p1.main()
            ask_user = int(input('Do you like  %s  song by  %s  from  %s playlist (0/1): ' %(song_name,artist,genere)))

            if ask_user == 1:
                return 1
            else:
                return 0

        else:
            now_playlist_selected = random.choice(given_playlist)
            if now_playlist_selected != previous_playlist:
                p3 = PlayListSelection(now_playlist_selected)
                song_name, artist, genere = p3.main()
                ask_user = int(input('Do you like " %s " song by " %s " from " %s " playlist (0/1): ' %(song_name,artist,genere)))

                if ask_user == 1:
                    return 1
                else:
                    return 0
            else: return sp.playlist_choosen(given_playlist, previous_playlist, 0)


s = SongPredict()
s.main()
















