window.onload=function(){

    initialize();

};

//$('#saveButton').on('click', function () {
//   var $btn = $(this).button('loading');
//    saveCoord();
//    $(this).button('reset');
//});

// script reads value (rooms code name) from the cookie set in room template
function getCookie(name) {
    var nameEQ = name + "=";
    //alert(document.cookie);
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1);
    if (c.indexOf(nameEQ) != -1) return c.substring(nameEQ.length,c.length);
    }
return null;
}



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

    // Quick fix for map not loading fully during the first start
    var fixed = false;
    google.maps.event.addListener(map, 'idle', function() { // fox for map not loading fully

            google.maps.event.trigger(map, 'resize');
            if(!fixed){
                google.maps.event.addListenerOnce(map, 'tilesloaded' , function(){
                    map.setCenter(marker.getPosition());
                fixed=true;
                });

            }

    });
}

function saveCoord(){

    var request = new XMLHttpRequest();

    var param = '../edit-map-json/?message=newCoord' + '&room=' +  getCookie("room") + '&lat=' + lat + '&lng=' + lng;

    request.open('GET', param, false);
    request.send(null);

    if(request.responseText == 'success'){

        console.log("message received")
    }

}