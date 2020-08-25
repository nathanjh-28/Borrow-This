console.log('borrow me!')

// import bulmaCalendar from '../bulma-calendar/dist/js/bulma-calendar.min.js'

// Initialize all input of date type.
const calendars = bulmaCalendar.attach('[type="date"]');
const dateTimeCals = bulmaCalendar.attach('[type="datetime-local"]');

// Loop on each calendar initialized
calendars.forEach(calendar => {
	// Add listener to date:selected event
	calendar.on('date:selected', date => {
		console.log(date);
	});
});

dateTimeCals.forEach(cal => {
    cal.on('datetime-local:selected', date =>{
        console.log(date)
    })
})

// To access to bulmaCalendar instance of an element
const element = document.querySelector('#my-element');
if (element) {
	// bulmaCalendar instance is available as element.bulmaCalendar
	element.bulmaCalendar.on('select', datepicker => {
		console.log(datepicker.data.value());
	});
}

