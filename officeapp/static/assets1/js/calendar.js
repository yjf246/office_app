'use strict';
(function (jQuery) {
    function changeView(value) {
        switch (value) {
            case 'day':
                window.cal.changeView('day', true);
                break;
            case 'week':
                window.cal.changeView('week', true);
                break;
            case 'month':
                window.cal.changeView('month', true);
                break;
        }
    }

    function randerRangeText() {
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        const startDate = window.cal.getDateRangeStart()
        const endDate = window.cal.getDateRangeEnd()
        const year = startDate.getFullYear()
        const month = months[startDate.getMonth()]
        console.log(window.cal.getDateRangeEnd())
        console.log(month, year)
        console.log('cal-range-render')
    }

    function createSchedule(){
        window.cal.createSchedules(model)
        //     [
        //     {
        //         id: '1',
        //         calendarId: '1',
        //         title: 'my schedule',
        //         category: 'time',
        //         dueDateClass: '',
        //         start: '2024-01-22 09:41:35.392491',
        //         end: '2024-01-22 10:41:35.392491'
        //     },
        //     {
        //         id: '2',
        //         calendarId: '1',
        //         title: 'second schedule',
        //         category: 'time',
        //         dueDateClass: '',
        //         start: '2024-01-24 09:41:35.392491',
        //         end: '2024-01-25 10:41:35.392491'
        //     },

        // ])  
    }

    window.cal = new tui.Calendar('#calendar', {
        defaultView: 'day',
        taskView: true,
        template: {
            monthDayname: function(dayname) {
                return '<span class="calendar-week-dayname-name">' + dayname.label + '</span>';
            }
        }
    });
    window.addEventListener('resize', function() {
        window.cal.render();
    });
    $('#cal-type').on('change', function() {
        changeView($(this).val())
    })
    $('#cal-next').on('click', function() {
        window.cal.next()
    })

    $('#cal-prev').on('click', function() {
        window.cal.prev()
    })
    console.log(randerRangeText())
    createSchedule();
})(jQuery);