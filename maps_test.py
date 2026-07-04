from maps.google_maps import GoogleMaps


maps = GoogleMaps()

maps.search(
    keyword="Plumbers",
    city="Dallas",
    limit=5
)