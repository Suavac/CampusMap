
//Global variables to store data about timetable selected
    var department, course, year, semester;

    //Builds up URL to be sent as json request
    function buildURL(message, dept, course, year, semester){
        var msg = '../json/?message=' + message + "&department=" + dept + "&course=" + course + "&year=" + year + "&semester=" + semester;

        return msg;
    }

    //Gets a list of departments from the database
    function getDepartments(){
        var request = new XMLHttpRequest();
        var message = buildURL("departments",null,null,null,null)
        request.open('GET', message, false);
        request.send(null);

        departments = JSON.parse(request.responseText);

        sel = document.getElementById('departmentSelect');

        //Creates selects in department dropdown with onclick events that call getCourses for that department
        for(var i=0; i<departments.departments.length; i++){
            var op = document.createElement("option");
            op.innerHTML = "" + departments.departments[i];
            sel.setAttribute('onchange', 'onDepartmentSelection(this)');
            sel.appendChild(op);
        }
    }

    function onDepartmentSelection (select) {
        var selectedOption = select.options[select.selectedIndex]
        getCourses(selectedOption.value)
    }

    function getCourses(dept){

        department = dept;

        var request = new XMLHttpRequest();
        var message = buildURL("courses",dept,null,null,null);
        request.open('GET', message, false);  // `false` makes the request synchronous
        request.send(null);

        courses = JSON.parse(request.responseText);
        console.log(courses);

        sel = document.getElementById('courseSelect');

        //Clear dropdown each time a new department is chosen
        while(sel.firstChild){
            sel.removeChild(sel.firstChild);
        }

        //Set the first element in the dropdown
        var option = document.createElement("option");
        option.innerHTML = "Select a course";
        sel.appendChild(option);

        //Set every other element in the dropdown
        for(var i = 0; i<courses.courses.length; i++){
            var op = document.createElement("option");
            op.innerHTML = "" + courses.courses[i];
            //sel.setAttribute('onchange', 'OnSelectionChange(this)')
            sel.setAttribute('onchange', 'onCourseSelection(this)')
            sel.appendChild(op);
        }
    }

    function onCourseSelection (select) {
        var selectedOption = select.options[select.selectedIndex]
        getYears(selectedOption.value)
    }

    //Loads years by course. Allows for courses of various lengths without errors
    //ie: arts is 3 years long vs engineering is 4. This would throw an error when selected using the filters with static year values
    function getYears(course){
        var message = buildURL("years", null, course, null, null);
        var request = new XMLHttpRequest();
        request.open('GET', message, false);
        request.send(null);

        years = JSON.parse(request.responseText);

        sel = document.getElementById('yearSelect');

         while(sel.firstChild){
            sel.removeChild(sel.firstChild);
        }
        var option = document.createElement("option")
        option.innerHTML = "Select a year"
        sel.appendChild(option)

        //uses length of the request to generate year values, not the actual data in the request
        for(var i=0; i<years.years.length; i++){
            var op = document.createElement("option");
            op.innerHTML = i+1;
            sel.appendChild(op);
        }
    }