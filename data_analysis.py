import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/SF_Crime_finalized.csv')

from gmaps import get_best_path
api_key = 'AIzaSyD1TuCWSJbEL2vwQjYNk9xaIRi43CUHDtk'

routes = get_best_path([-122.41052032, 37.783723], [-122.41531786, 37.76069344], api_key)

from algorithm import cluster, min_sum
centers = cluster(df.X, df.Y)
print('Number of cluster centers: ', len(centers))

print(centers)

best_route = min_sum(routes, centers)

print(best_route)