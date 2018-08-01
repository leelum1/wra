// Mapbox access token
mapboxgl.accessToken = 'pk.eyJ1IjoibGVlbHVtMSIsImEiOiJjamFzNHM0cmo0bmduMnFwbHh0MXNweW5jIn0.1fUr70BuY4Kk4BERLB5Pkg';

//Initialize map object
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/basic-v9',
  center: [-61.4, 10.45],
  zoom: 8
});

//Constrain map extent
map.setMaxBounds([[-62.2, 9.8],[-60.3, 11.4]]);

//Scale
var scale = new mapboxgl.ScaleControl({
    maxWidth: 80,
    unit: 'metric'
});
map.addControl(scale);

//Initialize overlay layers
map.on('load', function() {
  map.addSource('Watersheds-3dt1kb', {
        type: 'vector',
        url: 'mapbox://leelum1.26t26vhq'
    });

  map.addLayer({
      'id': 'Watersheds',
      'type': 'fill',
      'source': 'Watersheds-3dt1kb',
      'source-layer': 'Watersheds-3dt1kb',
      'layout': {
          'visibility': 'visible',
      },
      'paint': {
          'fill-color': 'rgba(0, 0, 0, 0)',
          'fill-outline-color': 'rgba(200, 100, 240, 1)'
      }
  });

  map.addLayer({
    "id": "watersheds-highlighted",
    "type": "fill",
    'source': 'Watersheds-3dt1kb',
    'source-layer': 'Watersheds-3dt1kb',
    "paint": {
        "fill-outline-color": "#484896",
        "fill-color": "#6e599f",
        "fill-opacity": 0.75
    },
    "filter": ["in", "NAME", ""]
  });
});

// Change the cursor to a pointer.
map.on('mouseenter', 'Watersheds', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a cursor.
map.on('mouseleave', 'Watersheds', function () {
    map.getCanvas().style.cursor = '';
});
