movies = {
    '冲上云霄': ['吴镇宇','胡杏儿','胡定燕'],
    '同盟': ['陈展鹏','胡定燕'],
    '施公奇案': ['欧阳震华','佘诗曼']
}

actor = input('whihc actor you wan choice')

for movie in movies:
    actors = movies[movie]
    # actors = movies[0]
    #print(actors)
    if actor in actors:
        print(actor + '出演了电影' + movie)