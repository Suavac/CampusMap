

    var rowUniqueIdentifier;

    function getRecordDetails( url ) {
        var x;
        if (confirm("Are You Sure?") == true) { // confirm deletion
            $(document).ready(function () {
                $('#test').on('click', 'tr', function (event) {
                    var texts = $(this).children().map(function () {
                        return $.trim($(this).html())
                    }).get();
                    rowUniqueIdentifier = texts[0];
                    deleteRecord(url);
                    location.reload();
                });
            });
        } else {
            return;
        }
    }

    function deleteRecord( url ) {

        var request = new XMLHttpRequest();

        var param = '../'+url+'/?message=delete' + '&toDelete=' + rowUniqueIdentifier;

        request.open('GET', param, false);
        request.send(null);

        if (request.responseText == 'success') {

           console.log("message received")
        }

    }

    function editRoomLocation() {

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



    function deleteTimetable() {

       $(document).ready(function () {
               $('#test').on('click', 'tr', function (event) {
                   var texts = $(this).children().map(function () {
                        return $.trim($(this).html())
                   }).get();
                   var course = texts[0];
                   var year = texts[1];
                   var semester = texts[2];
                   var request = new XMLHttpRequest();

                   var param = '../timetable/?message=delete' + '&course=' + course + '&year=' + year + '&semester=' + semester;

                   request.open('GET', param, false);
                   request.send(null);
                   location.reload();
               });
          });
       }
