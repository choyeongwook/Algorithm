def solution(genres, plays):
    
    dic = dict()
    all_plays = dict()
    array = []
    
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if dic.get(genre) is None:
            dic[genre] = []
            all_plays[genre] = 0
            
        all_plays[genre] += play
        dic[genre].append((i, play)) #  {"classic": [(1, 200)]}
    
    array = []
    for key in dic:
        array.append((key, all_plays[key]))
        dic[key].sort(key=lambda x: (-x[1], x[0]))
    array.sort(key=lambda x: -x[1])
    # print(array)
    # print(dic)

    result = []
    for key, play in array:
        result.append(dic[key][0][0])
        if len(dic[key]) >= 2:
            result.append(dic[key][1][0])
    
    return result