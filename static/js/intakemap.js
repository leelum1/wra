// Mapbox access token
mapboxgl.accessToken = 'pk.eyJ1IjoibGVlbHVtMSIsImEiOiJjamFzNHM0cmo0bmduMnFwbHh0MXNweW5jIn0.1fUr70BuY4Kk4BERLB5Pkg';

//Initialize map object
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/basic-v9',
  center: [easting, northing],
  zoom: 12
});

//Constrain map extent
map.setMaxBounds([[-62.2, 9.8],[-60.5, 11.0]]);

//Scale
var scale = new mapboxgl.ScaleControl({
    maxWidth: 80,
    unit: 'metric'
});
map.addControl(scale);

//Initialize overlay layers
map.on('load', function() {
  map.addSource('Intakes-98jk1d', {
        type: 'vector',
        url: 'mapbox://leelum1.5ibafbjm'
    });

  map.addLayer({
      'id': 'Intakes',
      'type': 'circle',
      'source': 'Intakes-98jk1d',
      'source-layer': 'Intakes-98jk1d',
      'layout': {
          'visibility': 'visible',
      },
      'paint': {
        'circle-radius': 5,
        'circle-color': 'blue'
      }
    });
});

map.on('mouseenter', 'Intakes', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a cursor.
map.on('mouseleave', 'Intakes', function () {
    map.getCanvas().style.cursor = '';
});
