function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
  $(".register-button").click(function() {
    var post_data = {}
    $(".registration-input").each(function() {
      post_data[$(this).attr("data-field")] = $(this).val();
    });
    if (!post_data["password"]) {
      $(".password-field").addClass("no-pw-error");
      return;
    }
    console.log(post_data);
    var csrftoken = getCookie('csrftoken');
    $.ajax({
      type: 'POST',
      beforeSend: function (xhr) {
        xhr.withCredentials = true;
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      },
      url: "/register",
      data: post_data,
      success: function() {
        window.location.href = "/";
      },
      async: true
    })
  });
});