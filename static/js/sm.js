
// function used for deleting records from database

    function getRecordDetails( url ) {// parameter is the name of the template

        if (confirm("Are You Sure?") == true) { // confirm deletion
            $(document).ready(function () { // get values from the selected row (table residing on the template)
                $('#test').on('click', 'tr', function (event) {
                        var rowUniqueIdentifier = $(this).children().map(function () {
                        return $.trim($(this).html())
                    }).get();

                           deleteRecord(url , rowUniqueIdentifier);

                });
            });
        } else {
            return;
        }
    }

    function deleteRecord( url ,rowUniqueIdentifier ) {

        var request = new XMLHttpRequest();
        if(url=='timetable') { // timetable records in uniquely identified by 3 values
            var param = '../timetable/?message=delete' + '&course=' + rowUniqueIdentifier[0]+ '&year=' + rowUniqueIdentifier[1] + '&semester=' + rowUniqueIdentifier[2];
        }
        else{ // other table's records can be identified by their primary key
            var param = '../'+url+'/?message=delete' + '&toDelete=' + rowUniqueIdentifier[0];
        }


        request.open('GET', param, false);
        request.send(null);
        location.reload();


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
