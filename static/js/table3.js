function createTable(title){
			
      document.write("<b>" + response.title + "</b>");
			var div = document.createElement('div');
			var table = document.createElement('table');
			
			div.className = 'container';
			table.className = "table table-bordered table-striped table-condensed text-center";
			
			var trh = document.createElement('tr');
			
			var th1 = document.createElement('th');
			var th2 = document.createElement('th');
			var th3 = document.createElement('th');
			var th4 = document.createElement('th');
			var th5 = document.createElement('th');
			var th6 = document.createElement('th');
			
			var tbody = document.createElement('tbody')
			
			th1.innerHTML = ('Time/Day');
			th2.innerHTML = ('Monday');
			th3.innerHTML = ('Tuesday');
			th4.innerHTML = ('Wednesday');
			th5.innerHTML = ('Thursday');
			th6.innerHTML = ('Friday');
			
			trh.appendChild(th1);
			trh.appendChild(th2);
			trh.appendChild(th3);
			trh.appendChild(th4);
			trh.appendChild(th5);
			trh.appendChild(th6);
			
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