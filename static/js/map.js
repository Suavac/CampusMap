window.onload=function(){

    initialize();

};

//$('#saveButton').on('click', function () {
//   var $btn = $(this).button('loading');
//    saveCoord();
//    $(this).button('reset');
//});




var map = null;
var marker = null;
var room = null;
var lat = null;
var lng = null;

function initialize() {

    var mapOptions = {
        center: {lat: 53.278, lng: -9.061608463525772},
        zoom: 17
    };

    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        marker = new google.maps.Marker({
        position: {lat: 53.27665459354239, lng: -9.061608463525772},
        map: map,
        draggable: true
    });



    google.maps.event.addListener(marker, 'drag', function(event) {

    });

    google.maps.event.addListener(marker, 'dragend', function(event) {
        //console.debug('final position is '+event.latLng.lat()+' / '+event.latLng.lng());
        lat = event.latLng.lat();
        lng = event.latLng.lng();


    });

    google.maps.event.addListener(marker, 'dragend', function(event) { // save new position of the marker
        saveCoord();
    });


}

