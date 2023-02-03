$(document).ready(() => {
    $('.menu-btn').click(() => {
        const menu = $('#slide-menu');
        const filter = $('#filter');
        if (menu.attr('class').split(/\s+/).includes('shown-menu')) {
            // Show slidebar
            filter.addClass('hide');
            menu.removeClass('shown-menu');
        }
        else {
            // Hide slidebar
            filter.removeClass('hide');
            menu.addClass('shown-menu');
            gsap.from('.btn', {
                x: 100,
                stagger: .025
            }).timescale(.8);
        }
    })

    $('#filter').click(() => {
        const menu = $('#slide-menu');
        const filter = $('#filter');
        if (menu.attr('class').split(/\s+/).includes('shown-menu')) {
            // Show slidebar
            filter.addClass('hide');
            menu.removeClass('shown-menu');
        }
    })
})
