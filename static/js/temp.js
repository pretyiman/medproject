jQuery(document).ready(function ($) {
    console.log("document loaded");


    // Menu Hamburger
    $('.navbar-toggler').on('click', function () {
        $(this).parents('.ws-main-header').toggleClass('_open');
    });
});