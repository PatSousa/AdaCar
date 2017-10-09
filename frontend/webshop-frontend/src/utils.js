//export default function setupCSRF(){
//  /* AJAX calls after form change */
//  const csrftoken = Cookies.get('csrftoken');
//
//  function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//  }
//
//  function beforeSend(xhr, settings) {
//    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//        xhr.setRequestHeader('X-CSRFToken', csrftoken);
//    }
//  }
//
//  $.ajaxSetup({beforeSend: beforeSend});
//}
//
