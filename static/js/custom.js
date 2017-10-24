$(document).ready(function(){
    // get job details
    $('.get-job-details').click(function(){
        $('.modal-loader').show();
        $.ajax({
            type: "POST",
            url: "/get-job-details/",
            data: { "item": $(this).attr('data-attr') },
            success: function(data) {
                $('body').append(data);
                $('#myModal').modal('show');
            }
        }).done(function(){
                $('.modal-loader').hide();
            });
    });

    //on modal hidden remove modal
    $(document).on('hidden.bs.modal', '#myModal', function (e) {
        $('#myModal').remove();
    });
    $(document).on('hidden.bs.modal', '#JobApplicationAjax', function (e) {
        $('.modal-dialog').empty();
    });

    // get job application modal
    $('.apply-job').click(function(event){
        event.preventDefault();
        job_slug = $(this).attr('data_slug');
        $('.modal-loader').show();
        $.ajax({
            type: "GET",
            url: "/jobs/" + job_slug + "/apply/",
            success: function(data) {
                $('.modal-dialog').append(data);
                $('#JobApplicationAjax').modal('show');
            }
        }).done(function(){
                $('.modal-loader').hide();
            });
    });

    // post job application
    $(document).on( "submit", ".apply-job-form", function( event ) {
        event.preventDefault();
        var formData = new FormData(this);
        job_slug = $(this).attr('data-slug');
        $('.modal-loader').show();
        $('.modal-dialog').empty();
        $.ajax({
            type: "POST",
            url: "/jobs/" + job_slug + "/apply/",
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
            success: function(data) {
                $('.modal-dialog').append(data);
                if($('.alert-message').hasClass('bg-success')){
                    $('.apply-job-form').remove();
                }
            }
        }).done(function(){
                $('.modal-loader').hide();
            });
    });

    <!--Start of Zendesk Chat Script-->
//    window.$zopim||(function(d,s){var z=$zopim=function(c){z._.push(c)},$=z.s=
//    d.createElement(s),e=d.getElementsByTagName(s)[0];z.set=function(o){z.set.
//    _.push(o)};z._=[];z.set._=[];$.async=!0;$.setAttribute("charset","utf-8");
//    $.src="https://v2.zopim.com/?5Ah6KuoFgpyjy5U3eu7LWHnm3lIk8YOo";z.t=+new Date;$.
//    type="text/javascript";e.parentNode.insertBefore($,e)})(document,"script");
    <!--End of Zendesk Chat Script-->

    //prognroll initilization
    $("body").prognroll({
        height: 2, //Progress bar height
        color: "#111", //Progress bar background color
        custom: false //If you make it true, you can add your custom div and see it's scroll progress on the page
      });

    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});