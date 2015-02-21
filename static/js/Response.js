/**
 * Created by Richard on 19/02/2015.
 */

// If you look at 11:00am on our timetable you'll see two classes at once.
// I'm gonna say we just skip this scenario for now, it's too much extra work
// for proof of concept.

// Sample data for Monday on our timetable
response = {

        "code" : "2BCT",
        "title" : "B.Sc. in Computer Science & Information Technology",
        "year" : "2014/2015",
        "semester" : "Year 2, Semester 2",
        "timetable" : [

            {
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "ENG G017",
            "lect"  : "H Melvin",
            "lab"   : false,
            "day"   : 1,
            "time"  : 1,
			"colour" : "#0FFF7B"},

            {
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "IT106",
            "lect"  : "H Melvin",
            "lab"   : true,
            "day"   : 1,
            "time"  : 2,
			"colour" : "#0FFF7B"},

            {
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "IT106",
            "lect"  : "H Melvin",
            "lab"   : true,
            "day"   : 1,
            "time"  : 3,
			"colour" : "#0FFF7B"},

            {
            "mod"   : "CT255",
            "title" : "Next Generation Technology",
            "room"  : "AC213",
            "lect"  : "M Schukat",
            "lab"   : false,
            "day"   : 1,
            "time"  : 4,
			"colour" : "#FFDF0F"},

            {
            "mod"   : "CT255",
            "title" : "Next Generation Technology",
            "room"  : "AC213",
            "lect"  : "M Schukat",
            "lab"   : true,
            "day"   : 1,
            "time"  : 5,
			"colour" : "#FFDF0F"},

            {
            "mod"   : "CT255",
            "title" : "Next Generation Technology",
            "room"  : "AC213",
            "lect"  : "M Schukat",
            "lab"   : true,
            "day"   : 1,
            "time"  : 6,
			"colour" : "#FFDF0F"},

            {
            "mod"   : "CT255",
            "title" : "Next Generation Technology",
            "room"  : "IT125G",
            "lect"  : null,
            "lab"   : false,
            "day"   : 1,
            "time"  : 8,
			"colour" : "#FFDF0F"},

			{
            "mod"   : "CT216",
            "title" : "Software Engineering",
            "room"  : "Finnegan PC Suite",
            "lect"  : "J Duggan",
            "lab"   : true,
            "day"   : 2,
            "time"  : 2,
			"colour":"#FF871F"},
			
			{
            "mod"   : "CT216",
            "title" : "Software Engineering",
            "room"  : "Finnegan PC Suite",
            "lect"  : "J Duggan",
            "lab"   : true,
            "day"   : 2,
            "time"  : 3,
			"colour":"#FF871F"},
			
			{
            "mod"   : "CT216",
            "title" : "Software Engineering",
            "room"  : "AC216",
            "lect"  : "J Duggan",
            "lab"   : false,
            "day"   : 2,
            "time"  : 4,
			"colour":"#FF871F"},
			
			{
            "mod"   : "CT216",
            "title" : "Software Engineering",
            "room"  : "IT125",
            "lect"  : "J Duggan",
            "lab"   : false,
            "day"   : 2,
            "time"  : 6,
			"colour":"#FF871F"},
			
			{
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "ENG G046",
            "lect"  : "H Melvin",
            "lab"   : false,
            "day"   : 3,
            "time"  : 2,
			"colour" : "#0FFF7B"},
			
			{
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "SC002 Larmour Theatre",
            "lect"  : "H Melvin",
            "lab"   : false,
            "day"   : 3,
            "time"  : 4,
			"colour" : "#0FFF7B"},
			
			{
            "mod"   : "MA203",
            "title" : "Linear Algebra",
            "room"  : "Cairnes Theatre",
            "lect"  : "SJ Park",
            "lab"   : false,
            "day"   : 3,
            "time"  : 5,
			"colour":"#1FFFBC"},
			
			{
            "mod"   : "CT229",
            "title" : "Programming II",
            "room"  : "IT102",
            "lect"  : "M Madden",
            "lab"   : true,
            "day"   : 3,
            "time"  : 8,
			"colour":"#59A1FF"},
			
			{
            "mod"   : "CT229",
            "title" : "Programming II",
            "room"  : "IT102",
            "lect"  : "M Madden",
            "lab"   : true,
            "day"   : 3,
            "time"  : 9,
			"colour":"#59A1FF"},
			
			{
            "mod"   : "CT231",
            "title" : "Professional Skills",
            "room"  : "Charles Mc Munn Theatre",
            "lect"  : "J Griffith/M Fox/P Byrne",
            "lab"   : false,
            "day"   : 4,
            "time"  : 3,
			"colour":"#BEC1C4"},
			
			{
            "mod"   : "CT231",
            "title" : "Professional Skills",
            "room"  : "Charles Mc Munn Theatre",
            "lect"  : "J Griffith/M Fox/P Byrne",
            "lab"   : false,
            "day"   : 4,
            "time"  : 4,
			"colour":"#BEC1C4"},
			
			{
            "mod"   : "MA203",
            "title" : "Linear Algebra Tutorial",
            "room"  : "IT204",
            "lect"  : "SJ Park",
            "lab"   : false,
            "day"   : 4,
            "time"  : 5,
			"colour":"#1FFFBC"},
			
			{
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "IT106",
            "lect"  : "H Melvin",
            "lab"   : true,
            "day"   : 4,
            "time"  : 8,
			"colour" : "#0FFF7B"},
			
			{
            "mod"   : "CT248",
            "title" : "Introduction to Modelling",
            "room"  : "IT106",
            "lect"  : "H Melvin",
            "lab"   : true,
            "day"   : 4,
            "time"  : 9,
			"colour" : "#0FFF7B"},
			
			{
            "mod"   : "CT229",
            "title" : "Programming II",
            "room"  : "IT250",
            "lect"  : "M Madden",
            "lab"   : false,
            "day"   : 5,
            "time"  : 2,
			"colour":"#59A1FF"},
			
			{
            "mod"   : "MA203",
            "title" : "Linear Algebra",
            "room"  : "AM150",
            "lect"  : "SJ Park",
            "lab"   : false,
            "day"   : 5,
            "time"  : 3,
			"colour":"#1FFFBC"},
			
			{
            "mod"   : "CT229",
            "title" : "Programming II",
            "room"  : "IT125G",
            "lect"  : "M Madden",
            "lab"   : false,
            "day"   : 5,
            "time"  : 5,
			"colour":"#59A1FF"},
			
			{
            "mod"   : "CT255",
            "title" : "Next Generation Technology",
            "room"  : "Finnegan PC Suite",
            "lect"  : "H Melvin",
            "lab"   : true,
            "day"   : 5,
            "time"  : 6,
			"colour" : "#FFDF0F"},

        ]
    }
