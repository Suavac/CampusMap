function createTable(response) {

    var div = document.createElement('div');
    var table = document.createElement('table');

    div.className = 'container';
    table.className = "table table-bordered table-striped table-condensed text-center";

    var trh = document.createElement('tr');

    var tbody = document.createElement('tbody');

    var rowHeader = ['Time/Day', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday'];

    for (var i = 0; i < 6; i++) {
        trh.appendChild(document.createElement('th'));
        trh.lastChild.innerHTML = (rowHeader[i]);
    }

    tbody.appendChild(trh);
    table.appendChild(tbody);

    var colHeader = [
        "09:00 AM", "10:00 AM", "11:00 AM", "12:00 AM",
        "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM",
        "5:00 PM", "6:00 PM", "7:00 PM"
    ];

    // for every hour
    for (var i = 1; i <= 11; i++) {

        // create a row
        var row = document.createElement("tr");

        // start with a time
        row.appendChild(document.createElement("th"));
        row.lastChild.innerHTML = colHeader[i - 1];

        // for every row, create 5 days
        for (var j = 1; j <= 5; j++) {

            var cell = document.createElement("td");

            // loop over all elements in time table, looking for a match
            for (var k = 0; k < response.timetable.length; k++) {

                // place in cell
                if ((response.timetable[k].day == j) && (response.timetable[k].time == i )) {

                    var cellText = (
                    response.timetable[k].room + "<br>" +
                    response.timetable[k].mod + "<br>" +
                    response.timetable[k].lect + "<br>");
					cell.style.backgroundColor = response.timetable[i].colour;

                    break; // important

                    // otherwise, something default
                } else {

                    var cellText = "Empty"
                }

            }
            cell.innerHTML = cellText;
            row.appendChild(cell);
        }
        tbody.appendChild(row);
    }

    div.appendChild(table);
    return div;

}