import pandas as pd
import networkx as nx

def create_graph(): 
    # csv 파일을 읽어서 DataFrame으로 변환합니다.
    data = pd.read_csv("series.csv")

    people_data = pd.read_csv("people.csv")
    actor_name_dict = {row["tmdb_id"]: row["name"] for _, row in people_data.iterrows()}


    # 그래프를 생성하고 초기화합니다.
    graph = nx.Graph()

    # 각 행에 대해 같은 작품에 출연한 배우들을 그래프에 추가합니다.
    for index, row in data.iterrows():
        movie_title = row['original_name']
        cast_ids = row['cast_ids']

        # cast_ids가 NaN인 경우 무시하고 다음 행으로 이동합니다.
        if pd.isnull(cast_ids):
            continue

        cast_ids = str(cast_ids).split(', ')
        cast_ids = [int(x) for x in cast_ids]

        # 같은 작품에 출연한 배우들 간의 연결을 추가합니다.
        for i in range(len(cast_ids)):
            for j in range(i + 1, len(cast_ids)):
                if graph.has_edge(cast_ids[i], cast_ids[j]):
                    continue
                graph.add_edge(cast_ids[i], cast_ids[j], movie=movie_title)

    return graph