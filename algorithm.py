def cluster(x_data: list, y_data: list):
    from sklearn.cluster import MiniBatchKMeans
    import numpy as np
    import pandas as pd

    points_list = np.column_stack((x_data, y_data))

    ## TEST
    print('Clustering training starts')
    from time import time
    time0 = time()

    clustering = MiniBatchKMeans(n_clusters=20).fit(points_list)

    ## TEST
    print('Training ended. Time: ', time() - time0)

    import matplotlib.pyplot as plt
    plt.scatter(clustering.cluster_centers_[:, 0], clustering.cluster_centers_[:, 1],
                marker='x', s=169, linewidths=3,
                color='r', zorder=10, label='Crime cluster center')
    plt.scatter(x_data, y_data, color='b', alpha=0.01)
    plt.scatter([],[], color='b', label='Crime location')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Historical crime locations in San Francisco Downtown')
    plt.legend()
    plt.savefig('sf_clusters.png')
    plt.show()


    ## returns clusters centroids
    return clustering.cluster_centers_


'''
    routes - the list of routes
    each route is the list of points
    each point is a list of two numbers - X and Y coordinates
    
    cluster_centers - the list of points (in the same format as above)
    
    return: route with the least min-sum assessment
'''


def min_sum(routes: list, cluster_centers: list, safety_preference = True):

    # function to calculate difference between two points
    def distance(point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5



    min_route = 0

    import math
    min_route_value = math.inf
    min_route_length_value = math.inf
    min_route_safety_value = math.inf

    for route in routes:
        # calculating the length of the route
        length_sum = 0
        for point_index in range(0, len(route) - 1):
            length_sum += distance(route[point_index], route[point_index + 1])

        # calculating the safety value of the route
        safety_sum = 0
        for point in route:
            for cluster_center in cluster_centers:
                safety_sum += distance(point, cluster_center)
        safety_sum /= -len(route) * len(cluster_centers)

        current_route_value = length_sum + safety_sum

        if (current_route_value < min_route_value
            or current_route_value == min_route_value
            and (safety_preference and safety_sum < min_route_safety_value
                 or not safety_preference and length_sum < min_route_length_value)):
            min_route = route
            min_route_value = current_route_value
            min_route_safety_value = safety_sum
            min_route_length_value = length_sum

    return min_route