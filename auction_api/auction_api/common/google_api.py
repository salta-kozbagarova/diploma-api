import googlemaps

class GoogleAPI:

    google_api_key = 'AIzaSyDn6hHtKruXaizSEWtiG07pF-si5nRsOKg'

    gmaps = googlemaps.Client(key=google_api_key)

    @staticmethod
    def get_lat_lon(address):
        geocode_result = GoogleAPI.gmaps.geocode(address)
        if geocode_result:
            return geocode_result[0].get('geometry').get('location')
        return None



