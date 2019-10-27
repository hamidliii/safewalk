def get_best_path(origin: list, destination: list, api_key: str, safety_priority = True):
    import requests

    GMAPS_DIRECTIONS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json?origin={},{}&' \
                               'destination={},{}&mode=walking&alternatives=true&key={}'.format(origin[1], origin[0], destination[1],
                                                                              destination[0], api_key)

    print(GMAPS_DIRECTIONS_API_URL)
    try:
        response = requests.get(GMAPS_DIRECTIONS_API_URL)
        response_json = response.json()

        routes = []

        for route in response_json['routes']:
            legs = []
            for leg in route['legs']:
                for step in leg['steps']:
                    x = step['end_location']['lng']
                    y = step['end_location']['lat']
                    legs.append([x, y])
            routes.append(legs)

        return routes

    except:
        print('ERROR')
        return None
