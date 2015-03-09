
window.onload==function(){
    initialize()
}


sampleJSON = {"markers":[
    {"lat":53.278944, "lng":-9.058583}
]}

function initialize() {
    var mapOptions = {
        center: {lat: 53.277700, lng: -9.062016},
        zoom: 18
    };
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    var marker = new google.maps.Marker({
        position: {lat: 53.277700, lng: -9.062016},
        map: map,
        title: 'Hello World!'
    });

}

google.maps.event.addDomListener(window, 'load', initialize);