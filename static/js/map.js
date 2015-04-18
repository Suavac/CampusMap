window.onload=function(){
    getBuildings();
    initialize();
}

$('#saveButton').on('click', function () {
    var $btn = $(this).button('loading')
    saveCoord()
    $(this).button('reset');
})


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

function saveCoord(){

    var request = new XMLHttpRequest();

    var param = '../edit-map-json/?message=newCoord' + '&room=' +  getCookie("room") + '&lat=' + lat + '&lng=' + lng;

    request.open('GET', param, false);
    request.send(null);

    if(request.responseText == 'success'){

        console.log("message received")
    }

}

function getBuildings(){
    //displayCookies();
    var request = new XMLHttpRequest();

    var param = '../edit-map-json/?message=buildings';

    request.open('GET', param, false);
    request.send(null);

    buildings = JSON.parse(request.responseText);

    sel = document.getElementById('buildingSelect');

    for(var i=0; i < buildings.buildings.length; i++){
        var op = document.createElement("option");
        op.innerHTML = "" + buildings.buildings[i];
        sel.setAttribute('onchange', 'onBuildingSelect(this)');
        sel.appendChild(op);
    }
}

function onBuildingSelect(select) {
    var selectedOption = select.options[select.selectedIndex]
    getRooms(selectedOption.value)
}

function getRooms(building){

    console.log(building)

    var param = '../edit-map-json/?message=' + 'rooms' + '&building=' + building;

    var request = new XMLHttpRequest();
    request.open('GET', param, false);  // `false` makes the request synchronous
    request.send(null);

    rooms = JSON.parse(request.responseText);

    sel = document.getElementById('roomSelect');
    sel.disabled = false;

    //Set every other element int the dropdown
    for(var i = 0; i < rooms.rooms.length; i++){
        var op = document.createElement("option");
        op.innerHTML = "" + rooms.rooms[i];
        sel.setAttribute('onchange', 'onRoomSelect(this)');
        sel.appendChild(op);
    }
}

function onRoomSelect(select) {
    var selectedOption = select.options[select.selectedIndex]
    loadPin(selectedOption.value)
    room = selectedOption.value;
}

function loadPin(room){
    console.log(room);

    var param = '../edit-map-json/?message=' + 'coord' + '&room=' + room;

    var request = new XMLHttpRequest();
    request.open('GET', param, false);  // `false` makes the request synchronous
    request.send(null);

    coords = JSON.parse(request.responseText);

    marker.setPosition(new google.maps.LatLng(coords.lat, coords.lng));
    map.setCenter(new google.maps.LatLng(coords.lat, coords.lng));

    lat = coords.lat;
    lng = coords.lng;

    document.getElementById('saveButton').disabled = false;
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
        //console.debug('new position is '+event.latLng.lat()+' / '+event.latLng.lng());
    });

    google.maps.event.addListener(marker, 'dragend', function(event) {
        //console.debug('final position is '+event.latLng.lat()+' / '+event.latLng.lng());
        lat = event.latLng.lat();
        lng = event.latLng.lng();
    });
}