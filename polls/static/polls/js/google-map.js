
var google;

function initMap() {
    // Basic options for a simple Google Map
    // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
    // var myLatlng = new google.maps.LatLng(40.71751, -73.990922);
    var myLatlng = new google.maps.LatLng(-33.450832,-70.660248);
    // 39.399872
    // -8.224454
    
    var mapOptions = {
        // How zoomed in you want the map to start at (always required)
        zoom: 15,

        // The latitude and longitude to center the map (always required)
        center: myLatlng,

        // How you would like to style the map. 
        scrollwheel: false,
        styles: [{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#b1b881"},{"lightness":100}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#b1b881"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#b1b881"},{"lightness":90}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#b1b881"},{"lightness":50},{"weight":1.2}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#b1b881"},{"lightness":25}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#b1b881"},{"lightness":21}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#b1b881"},{"lightness":7}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#b1b881"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#b1b881"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#b1b881"},{"lightness":16}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#b1b881"},{"lightness":19}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#b1b881"},{"lightness":17}]}]
    };

    

    // Get the HTML DOM element that will contain your map 
    // We are using a div with id="map" seen below in the <body>
    var mapElement = document.getElementById('map');

    // Create the Google Map using out element and options defined above
    var map = new google.maps.Map(mapElement, mapOptions);
    
    var addresses = ['Brooklyn'];

    for (var x = 0; x < addresses.length; x++) {
        $.getJSON('http://maps.googleapis.com/maps/api/geocode/json?address='+addresses[x]+'&sensor=false', null, function (data) {
            var p = data.results[0].geometry.location
            var latlng = new google.maps.LatLng(p.lat, p.lng);
            new google.maps.Marker({
                position: latlng,
                map: map,
                icon: 'img/loc.png'
            });

        });
    }
    var marker_church = new google.maps.Marker({
        position: {lat: -33.4522328, lng: -70.6608088}, map: map, label:"I"
    });
    var marker_party = new google.maps.Marker({
        position: {lat: -33.449643, lng: -70.6576672}, map: map, label:"F"
    });
}
google.maps.event.addDomListener(window, 'load', init);

// Initialize and add the map
/*function initMap() {
    // The location of Uluru
    var uluru = {lat: -25.344, lng: 131.036};
    // The map, centered at Uluru
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 4, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
  }*/