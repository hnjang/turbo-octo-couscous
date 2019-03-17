#!/usr/bin/python3

from pprint import pprint

def solution(genres, plays):
    s_genres = set(genres)
    pcount_genres = dict()
    for g in s_genres:
        pcount_genres[g] = 0
    # find play count of each genre
    for i, p in enumerate(plays):
        pcount_genres[genres[i]] += p
    l_pcount_genres = [[k, pcount_genres[k]] for k in pcount_genres]
    sorted_genres = sorted(l_pcount_genres, key=lambda x: x[1], reverse=True)

    # build sorted_song
    songs = [[i, c] for i, c in enumerate(plays)]
    sorted_songs = sorted(songs, key=lambda x: x[1], reverse=True)
    # pprint(sorted_songs)

    result = []
    for g in sorted_genres:
        cnt = 0
        for s in sorted_songs:
            if g[0] == genres[s[0]]:
                result.append(s[0])
                cnt += 1
                if cnt >= 2: break
    return result

print(solution(["classic", "pop", "classic", "classic", "pop"], [
    500, 600, 150, 800, 2500]))
