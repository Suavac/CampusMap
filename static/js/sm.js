

    var rowUniqueIdentifier;

    function getRecordDetails( url ) {

        $(document).ready(function () {
            $('#test').on('click', 'tr', function (event) {
                var texts = $(this).children().map(function () {
                    return $.trim($(this).html())
                }).get();
                rowUniqueIdentifier=texts[0];
                deleteRecord();
                location.reload();
            });
        });

    function deleteRecord() {

        var request = new XMLHttpRequest();

        var param = '../'+url+'/?message=delete' + '&toDelete=' + rowUniqueIdentifier;

        request.open('GET', param, false);
        request.send(null);

        if (request.responseText == 'success') {

           console.log("message received")
        }

        }
    }

    function getRoomDetails() {

        $(document).ready(function () {
            $('#test').on('click', 'tr', function (event) {
                var texts = $(this).children().map(function(){
                    return $.trim($(this).html())
                }).get();

            document.cookie = "room="+texts[0]+"; expires=0; path=/";

            loadPin(texts[0]);
            });
        });
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