// // AJAX for posting
// function create_exam() {
//     console.log("create post is working!") // sanity check
//
//     function getCookie(name) {
//         var cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             var cookies = document.cookie.split(';');
//             for (var i = 0; i < cookies.length; i++) {
//                 var cookie = jQuery.trim(cookies[i]);
//                 // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//
//     var csrftoken = getCookie('csrftoken');
//
// // Setup ajax connections safetly
//
//     function csrfSafeMethod(method) {
//         // these HTTP methods do not require CSRF protection
//         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//     }
//
//     $.ajaxSetup({
//         beforeSend: function (xhr, settings) {
//             if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
//             }
//         }
//     });
//
//
//     // var file = $("#id_event_img").prop('files')[0];
//
//     var formdata = new FormData();
//
//     formdata.append("exam-name", $('#exam-name').val());
//     $.ajax({
//         url : "create_exam/", // the endpoint
//         type : "POST", // http method
//         data : formdata, // data sent with the post request
//         processData: false,
//         contentType: false,
//
//         // handle a successful response
//         success : function(json) {
//             $('#exam-name').val(''); // remove the value from the input
//             console.log(json); // log the returned json to the console
//             console.log("success"); // another sanity check
//         },
//
//         // handle a non-successful response
//         error : function(xhr,errmsg,err) {
//             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//         }
//     });
// };
//
// // create exam
// $('#create-exam-form').on('submit', function(event){
//     event.preventDefault();
//     console.log("form submitted!")  // sanity check
//     create_exam();
// });