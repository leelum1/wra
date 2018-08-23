// Mapbox access token
var token = 'pk.eyJ1IjoibGVlbHVtMSIsImEiOiJjamFzNHM0cmo0bmduMnFwbHh0MXNweW5jIn0.1fUr70BuY4Kk4BERLB5Pkg';
mapboxgl.accessToken = token;

function compare(a,b) {
  if (a.properties.Name < b.properties.Name)
    return -1;
  if (a.properties.Name > b.properties.Name)
    return 1;
  return 0;
};

//Remove duplicate features from rendered tiles
function getUniqueFeatures(array, comparatorProperty) {
  var existingFeatureKeys = {};
  var uniqueFeatures = array.filter(function(el) {
      if (existingFeatureKeys[el.properties[comparatorProperty]]) {
          return false;
      } else {
          existingFeatureKeys[el.properties[comparatorProperty]] = true;
          return true;
      }
  });
  uniqueFeatures.pop();
  return uniqueFeatures.sort(compare);
}

//Layer features
function LayerDetail(layer){
  var features = map.queryRenderedFeatures(layer);
  if (layer == 'Watersheds' || layer == 'Rainfall' || layer == 'Rivers' || layer == 'Intakes' || layer == 'Streamflow' || layer == 'Reservoirs'){
    var uniqueFeatures = getUniqueFeatures(features, "Name");
  } else if(layer =='Wells'){
    var uniqueFeatures = getUniqueFeatures(features, "Index");
  }
  renderListings(uniqueFeatures, layer);
  $(".map-overlay").toggle();
};

//Layer control
function ToggleLayer(layer){
  var visibility = map.getLayoutProperty(layer, 'visibility');
  var arrow = document.getElementById(layer + "arrow")

  if (visibility == 'visible') {
      map.setLayoutProperty(layer, 'visibility', 'none');
      $("button:contains(" + layer + ")").toggleClass('active');
      // if (layer == 'Watersheds'){
      //   map.setFilter("watersheds-highlighted", ['in', 'NAME', ""])};
      if (layer == 'Rivers'){
        map.setLayoutProperty('RiverSymbols', 'visibility', 'none')};
      if (layer == 'Isohyetal'){
        map.setLayoutProperty('IsohyetalSymbols', 'visibility', 'none')};
      $('.map-overlay').attr('style','display:none');
      if (arrow) {
        arrow.disabled = true;
      }
  } else {
      $("button:contains(" + layer + ")").toggleClass('active');
      map.setLayoutProperty(layer, 'visibility', 'visible');
      if (layer == 'Rivers'){
        map.setLayoutProperty('RiverSymbols', 'visibility', 'visible')};
      if (layer == 'Isohyetal'){
        map.setLayoutProperty('IsohyetalSymbols', 'visibility', 'visible')};
      if (arrow) {
        arrow.disabled = false;
      }
  }
};

//Zoom out
function zoomOut(){
  map.flyTo({center: [-61.5, 10.5], zoom: 8});
};

//Map Preview
function setMapPreview() {
  var bounds = map.getBounds().toArray();
  bounds = [bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1]];

  // The size of the desired map.
  var size = [80, 80];

  // Calculate a zoom level and centerpoint for this map.
  var vp = geoViewport.viewport(bounds, size, 0, 24, 512); //viewport(bounds, dimensions, minzoom, maxzoom, tileSize)

  // Construct a static map url
  // https://www.mapbox.com/developers/api/static/
  document.getElementById('basemenu').src =
    'https://api.mapbox.com/styles/v1/mapbox/' + styles[1] + '/static/' +
    vp.center.join(',') + ',' + vp.zoom + ',' +
    map.getBearing() + ',' + map.getPitch() + '/' +
    size.join('x') + '?' +
    'attribution=false&logo=false&access_token=' + token
}

var styles = ['basic-v9', 'satellite-v9']

//Initialize map object
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/' + styles[0],
  center: [-61.5, 10.5],
  zoom: 8
});

//Constrain map extent
map.setMaxBounds([[-62.2, 9.8],[-60.3, 11.4]]);

//Scale
var scale = new mapboxgl.ScaleControl({
    maxWidth: 100,
    unit: 'metric'
});
map.addControl(scale);


//Geolocation control
map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    trackUserLocation: true
}));

var previewUpdate

map.on('render', function() {
  clearTimeout(previewUpdate)
  previewUpdate = setTimeout(setMapPreview, 100)
});

function switchBase() {
  styles.push( styles.shift() )
  map.setStyle('mapbox://styles/mapbox/' + styles[0])
  var buts = document.getElementsByClassName("main-layer")
  for (var i = 0; i < buts.length; i++) {
    buts[i].classList.remove("active");
  }
};

var allLayers = [{
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.26t26vhq'
    },
  layer: {
      id: 'Watersheds',
      type: 'fill',
      source: 'Watersheds-3dt1kb',
      'source-layer': 'Watersheds-3dt1kb',
      layout: {
          'visibility': 'none',
      },
      paint: {
          'fill-color': 'rgba(0, 0, 0, 0)',
          'fill-outline-color': 'rgba(200, 100, 240, 1)'
      }
    }
  }, {
  // layer: {
  //   "id": "watersheds-highlighted",
  //   "type": "fill",
  //   'source': 'Watersheds-3dt1kb',
  //   'source-layer': 'Watersheds-3dt1kb',
  //   "paint": {
  //       "fill-outline-color": "#484896",
  //       "fill-color": "#6e599f",
  //       "fill-opacity": 0.75
  //   },
  //   "filter": ["in", "NAME", ""]
  //   }
  // }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.8zrmbkd9'
    },
  layer: {
      'id': 'Rainfall',
      'type': 'circle',
      'source': 'Rainfall-3f50n1',
      'source-layer': 'Rainfall-3f50n1',
      'layout': {
          'visibility': 'none',
      },
      'paint': {
        'circle-radius': 5,
        'circle-color': 'red'
      }
    }
  }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.cx1mwqqk'
    },
  layer: {
      'id': 'Rivers',
      'type': 'line',
      'source': 'Rivers-3omzdt',
      'source-layer': 'Rivers-3omzdt',
      "minzoom": 8,
      "layout": {
          "line-join": "round",
          "line-cap": "round",
          'visibility': 'none',
      },
      "paint": {
          "line-color": "#1163C8",
          "line-width": 2
      }
    }
  }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.5ibafbjm'
    },
  layer: {
      'id': 'Intakes',
      'type': 'circle',
      'source': 'Intakes-98jk1d',
      'source-layer': 'Intakes-98jk1d',
      'layout': {
          'visibility': 'none',
      },
      'paint': {
        'circle-radius': 5,
        'circle-color': 'blue'
      }
    }
  }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.dyeznxxb'
    },
  layer: {
      'id': 'Streamflow',
      'type': 'circle',
      'source': 'Streamflow_Gauge-0sezec',
      'source-layer': 'Streamflow_Gauge-0sezec',
      'layout': {
          'visibility': 'none',
      },
      'paint': {
        'circle-radius': 5,
        'circle-color': 'green'
      }
    }
  }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.cvyxss9u'
    },
  layer: {
      'id': 'Reservoirs',
      'type': 'fill',
      'source': 'Reservoirs-3wyc0r',
      'source-layer': 'Reservoirs-3wyc0r',
      'layout': {
          'visibility': 'none',
      },
      'paint': {
        'fill-color': '#97ABF3',
        'fill-outline-color': '#7793F5'
      }
    }
  }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.6mr1616t'
    },
  layer: {
      'id': 'Thiessen',
      'type': 'fill',
      'source': 'Thiessen-6jar6e',
      'source-layer': 'Thiessen-6jar6e',
      'layout': {
          'visibility': 'none',
      },
      'paint': {
          'fill-color': 'rgba(0, 0, 0, 0)',
          'fill-outline-color': 'rgba(255, 165, 0, 1)'
      }
    }
  }, {
  source: {
        type: 'vector',
        url: 'mapbox://leelum1.02uifkos'
    },
  layer: {
      'id': 'Isohyetal',
      'type': 'line',
      'source': 'Isohyetal-4gmub3',
      'source-layer': 'Isohyetal-4gmub3',
      "layout": {
          "line-join": "round",
          "line-cap": "round",
          'visibility': 'none',
      },
      "paint": {
          "line-color": "#ff69b4",
          "line-width": 2
      }
    }
  }
];

map.on('style.load', function() {
    for (var i = 0; i < allLayers.length; i++) {
        var me = allLayers[i];
        map.addSource(me.layer.source, me.source);
        map.addLayer(me.layer)
    }
    renderListings([]);

    map.addLayer({
      "id": "RiverSymbols",
      "type": "symbol",
      "source": "Rivers-3omzdt",
      'source-layer': 'Rivers-3omzdt',
      "minzoom": 8,
      "layout": {
        "symbol-placement": "line",
        "text-font": ["Open Sans Italic"],
        "text-field": '{Name}' + " River", // part 2 of this is how to do it
        "text-size": 12,
        "text-anchor": "bottom",
        "text-max-angle": 30,
        "visibility": 'none'
      }
    });

    map.addLayer({
      'id': 'Rivers-highlighted',
      'type': 'line',
      'source': 'Rivers-3omzdt',
      'source-layer': 'Rivers-3omzdt',
      "minzoom": 8,
      "layout": {
          "line-join": "round",
          "line-cap": "round",
      },
      "paint": {
          "line-color": "#F60F08",
          "line-width": 2
      },
      "filter": ["in", "Name", ""]
    });

    map.addLayer({
      "id": "IsohyetalSymbols",
      "type": "symbol",
      "source": "Isohyetal-4gmub3",
      'source-layer': 'Isohyetal-4gmub3',
      "minzoom": 8,
      "layout": {
        "symbol-placement": "line",
        "text-font": ["Open Sans Italic"],
        "text-field": '{Contour}' + " mm", // part 2 of this is how to do it
        "text-size": 12,
        "text-anchor": "bottom",
        "text-max-angle": 30,
        "visibility": 'none'
      }
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

// Change the cursor to a pointer.
map.on('mouseenter', 'Rainfall', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a cursor.
map.on('mouseleave', 'Rainfall', function () {
    map.getCanvas().style.cursor = '';
});

// Change the cursor to a pointer.
map.on('mouseenter', 'Intakes', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a cursor.
map.on('mouseleave', 'Intakes', function () {
    map.getCanvas().style.cursor = '';
});

// Change the cursor to a pointer.
map.on('mouseenter', 'Streamflow', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a cursor.
map.on('mouseleave', 'Streamflow', function () {
    map.getCanvas().style.cursor = '';
});

// Change the cursor to a pointer.
map.on('mouseenter', 'Reservoirs', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a cursor.
map.on('mouseleave', 'Reservoirs', function () {
    map.getCanvas().style.cursor = '';
});


//Mouse coordinates
map.on('mousemove', function (e) {
    document.getElementById('coords').innerHTML = JSON.stringify(e.lngLat);
});

//Remove mouse coordinates on leave
$( "#map" ).mouseleave(function() {
  $( "#coords" ).html("");
});

//Attribute selector
var listingEl = document.getElementById('feature-listing');

// Create a popup, but don't add it to the map yet.
var popup = new mapboxgl.Popup({});

// map.on('mouseenter', 'Isohyetal', function(e) {
//     // Change the cursor style as a UI indicator.
//     map.getCanvas().style.cursor = 'pointer';
//
//     var coordinates = e.lngLat;
//     var description = e.features[0].properties.Contour;
//
//     popup.setLngLat(coordinates)
//         .setHTML(description + " mm")
//         .addTo(map);
// });
//
// map.on('mouseleave', 'Isohyetal', function() {
//     map.getCanvas().style.cursor = '';
//     popup.remove();
// });
