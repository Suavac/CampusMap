function createTable(title){
			
      document.write("<b>" + response.title + "</b>");
			var div = document.createElement('div');
			var table = document.createElement('table');
			
			div.className = 'container';
			table.className = "table table-bordered table-striped table-condensed text-center";
			
			var trh = document.createElement('tr');


			var tbody = document.createElement('tbody')


            var strings = ['Time/Day', 'Monday', 'Tuesday',
                            'Wednesday', 'Thursday', 'Friday'];

            for (var i = 0; i < 6; i++){
                trh.appendChild(document.createElement('th'));
                trh.lastChild.innerHTML = (strings[i]);

            }

			
			tbody.appendChild(trh);
			table.appendChild(tbody);
			
      var tr; 
      var td;
     
      
      for(var i=1; i<=11; i++){
        tr = document.createElement('tr');
        td = document.createElement('th');
        td.innerHTML = time(i);
        //tr.id = i;
        tr.appendChild(td);
        if(i%1 == 0){
          var cell = tr.insertCell(-1);
          cell.innerHTML = i;
          cell.id = i;
        }

        if(i%1 == 0){
          var cell = tr.insertCell(-1);
          cell.innerHTML = 11+i;
          cell.id = 11 + i;
        }       
        
        if(i%1 == 0){
          var cell = tr.insertCell(-1);
          cell.innerHTML = 22+i;
          cell.id = 22 + i;
        }      
        
        if(i%1 == 0){
          var cell = tr.insertCell(-1);
          cell.innerHTML = 33+i;
          cell.id = 33 + i;
        }      
        
        if(i%1 == 0){
          var cell = tr.insertCell(-1);
          cell.innerHTML = 44+i;
          cell.id = 44 + i;
        }       
        tbody.appendChild(tr);
        table.appendChild(tbody);
        
        
      }
			
			div.appendChild(table);
			document.body.appendChild(div);
      
      
      for(var i=1; i<=55; i++){
      var cell = document.getElementById(i);
        if(response.timetable[i].cellID = cell.id){
            if(response.timetable[i].mod == null){
              cell.innerHTML = "";
            }else{
            
            cell.innerHTML = response.timetable[i].mod + " " + response.timetable[i].title + "<br>" +
                             response.timetable[i].room + "<br>" +
                             response.timetable[i].lect;
            cell.style.backgroundColor = response.timetable[i].colour;
           }
        
        }
      }
		}
		
		function time(r){
				var time;
				
				if(r==1){time = "09:00 AM";}
				if(r==2){time = "10:00 AM";}
				if(r==3){time = "11:00 AM";}
				if(r==4){time = "12:00 AM";}
				if(r==5){time = "1:00 PM";}
				if(r==6){time = "2:00 PM";}
				if(r==7){time = "3:00 PM";}
				if(r==8){time = "4:00 PM";}
				if(r==9){time = "5:00 PM";}
				if(r==10){time = "6:00 PM";}
				if(r==11){time = "7:00 PM";}
				
				return time;
		}



function tableCreate() {

        var body = document.getElementsByTagName("body")[0];
        var tbl     = document.createElement("table");
        var tblBody = document.createElement("tbody");



        // for every hour
		for (var i = 1; i <= 11; i++) {

            // create a row
			var row = document.createElement("tr");

            // for every row, create 5 days
            for (var j = 1; j <= 5; j++){

                var cell = document.createElement("td");

                // loop over all elements in time table, looking for a match
                for (var k = 0; k < response.timetable.length; k++){

                    // place in cell
                    if ((response.timetable[k].day == j) && (response.timetable[k].time == i )){

                        var cellText = (response.timetable[k].room + "<br>" +
                                        response.timetable[k].mod + "<br>" +
                                        response.timetable[k].lect + "<br>");

                        break;

                    // otherwise, something default
                    } else {

                        var cellText = "Empty"
                    }

                }

                cell.innerHTML = cellText;

                row.appendChild(cell);

            }

			tblBody.appendChild(row);

		}

        tbl.appendChild(tblBody);

        body.appendChild(tbl);

        tbl.setAttribute("border", "2");
    }