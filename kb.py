import graph
import actor_name_dict
import networkx as nx

def find_kevin_bacon_number_with_movies(graph, source_id, target_id, actor_name_dict):
    try:
        path = nx.shortest_path(graph, source_id, target_id)
        result = [actor_name_dict[source_id]]
        for i in range(len(path) - 1):
            movie_title = graph[path[i]][path[i + 1]]["movie"]
            result.append(movie_title)
            result.append(actor_name_dict[path[i + 1]])
        return " -> ".join(str(x) for x in result)
    except nx.NetworkXNoPath:
        return "No path found between {} and {}.".format(source_id, target_id)
    except KeyError:
        return "Actor ID not found in the actor_name_dict."


# Example usage
id1 = 75913 # 하정우
id2 = 73249 # 이정재
print(find_kevin_bacon_number_with_movies(graph.create_graph(), id1, id2, actor_name_dict.get_dict()))