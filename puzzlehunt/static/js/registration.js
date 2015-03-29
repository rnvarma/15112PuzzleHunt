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
    $.ajax({
      type: 'POST',
      url: "/register",
      data: post_data,
      success: function() {
        window.location.href = "/";
      }
    })
  });
});