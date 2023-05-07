import networkx as nx
import operator
import actor_name_dict
import graph

actor_name_dict =  actor_name_dict.get_dict()
graph = graph.create_graph()

# Degree Centrality: 연결된 노드 수를 기준으로 중심성을 계산합니다.
degree_centrality = nx.degree_centrality(graph)
# 정렬하여 상위 5명의 배우를 출력합니다.
sorted_degree_centrality = sorted(degree_centrality.items(), key=operator.itemgetter(1), reverse=True)
top_5_actors = [(actor_name_dict[actor_id], centrality) for actor_id, centrality in sorted_degree_centrality[:5]]
print("Top 5 actors by Degree Centrality:", top_5_actors)

# Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(graph)
sorted_eigenvector_centrality = sorted(eigenvector_centrality.items(), key=operator.itemgetter(1), reverse=True)
top_5_actors_eigenvector = [(actor_name_dict[actor_id], centrality) for actor_id, centrality in sorted_eigenvector_centrality[:5]]
print("Top 5 actors by Eigenvector Centrality:", top_5_actors_eigenvector)

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(graph)
sorted_closeness_centrality = sorted(closeness_centrality.items(), key=operator.itemgetter(1), reverse=True)
top_5_actors_closeness = [(actor_name_dict[actor_id], centrality) for actor_id, centrality in sorted_closeness_centrality[:5]]
print("Top 5 actors by Closeness Centrality:", top_5_actors_closeness)

# PageRank
pagerank = nx.pagerank(graph)
sorted_pagerank = sorted(pagerank.items(), key=operator.itemgetter(1), reverse=True)
top_5_actors_pagerank = [(actor_name_dict[actor_id], rank) for actor_id, rank in sorted_pagerank[:5]]
print("Top 5 actors by PageRank:", top_5_actors_pagerank)

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(graph)
sorted_betweenness_centrality = sorted(betweenness_centrality.items(), key=operator.itemgetter(1), reverse=True)
top_5_actors_betweenness = [(actor_name_dict[actor_id], centrality) for actor_id, centrality in sorted_betweenness_centrality[:5]]
print("Top 5 actors by Betweenness Centrality:", top_5_actors_betweenness)



