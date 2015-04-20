
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

    // function used for deleting records from database

    function getRecordDetails( url, action ) {// parameter is the name of the template

        var rowUniqueIdentifier;
        $(document).ready(function () { // get values from the selected row (table residing on the template)
                $('#test').on('click', 'tr', function (event) {
                        rowUniqueIdentifier = $(this).children().map(function () {
                        return $.trim($(this).html())
                    }).get();


                    if(action=='delete'){
                       bootbox.confirm("Are you sure want to delete "+ rowUniqueIdentifier[0] +" "+ url+" ? ", function(result) { // confirm deletion
                        if(result){
                              deleteRecord(url , rowUniqueIdentifier);
                            } else {
                           //$('#largeModal').modal('hide');
                            return;
                        }
                        });
                    }
                    else if(action == 'edit'){
                    }
                    else{
                    }
                });
            });



    }

    function deleteRecord( url ,rowUniqueIdentifier ) {

        var request = new XMLHttpRequest();
        if(url=='timetable' || url=='TimeEntry') { // timetable records in uniquely identified by 3 values
            var param = '../timetable/?message=delete' + '&course=' + rowUniqueIdentifier[0]+ '&year=' + rowUniqueIdentifier[1] + '&semester=' + rowUniqueIdentifier[2];
        }
        else{ // other table's records can be identified by their primary key
            var param = '../'+url+'/?message=delete' + '&toDelete=' + rowUniqueIdentifier[0];
        }


        request.open('GET', param, false);
        request.send(null);
        location.reload();

    }

    function deleteRecord( url ,rowUniqueIdentifier ) {

        var request = new XMLHttpRequest();
        if(url=='timetable' || url=='TimeEntry') { // timetable records in uniquely identified by 3 values
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

        //initialize(); // initialize map

        $(document).ready(function () {
            $('#test').on('click', 'tr', function (event) {
                var texts = $(this).children().map(function(){
                    return $.trim($(this).html())
                }).get();

                document.cookie = "room="+texts[0]+"; expires=0; path=/"; // create Cookie file

                loadPin(texts[0]);

                //$('#largeModal').modal('show');

                // the initial start of the map with given pin doesnt center correctly
                // this fixes this problem for every new map display
                var newMapLocation=false;

                google.maps.event.addListener(map, 'idle', function() { // fox for map not loading fully

                        google.maps.event.trigger(map, 'resize');
                    if(!newMapLocation){
                        map.setCenter(marker.getPosition());
                        newMapLocation=true;
                    }


                });
            });
        });

    }

    function loadPin(room){
        console.log(room);

        var param = '../edit-map-json/?message=' + 'coord' + '&room=' + room;

        var request = new XMLHttpRequest();
        request.open('GET', param, false);  // `false` makes the request synchronous
        request.send(null);

        var coords = JSON.parse(request.responseText);
        var lat = coords.lat;
        var lng = coords.lng;

        marker.setPosition(new google.maps.LatLng(coords.lat, coords.lng));
        map.setCenter(marker.getPosition());


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


