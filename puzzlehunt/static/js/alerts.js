//custom alert box. takes a message and an object mapping button names to
//  callbacks which should be called when those buttons are clicked.
var createAlert = function (message, buttons) {
  var overlay = $("#alert-overlay");
  var al = $(".alert").empty();

  //grey out page
  overlay.css({"display": "block"});

  //add message to alert box
  var mess = $("<h2>").html(message);
  al.append(mess);

  //add default "Ok" button if none are given
  if (buttons === undefined) {
    buttons = {"Okay": undefined};
  }

  //add all given buttons
  for (button in buttons) {
    var newButton = $("<span>");
    newButton.html(button);
    newButton.addClass("btn btn-info");

    //bind callback from buttons[button] to new button
    (function (callback) {
      newButton.click(function (e) {
        if (callback !== undefined) callback(e);
        al.html("");
        overlay.css({"display": "none"});
      });
    }) (buttons[button]);

    al.append(newButton);
  }
};

var flashColor = function(colorStr, callback) {
  var flashTime = 500; // milliseconds
  var overlay = $("#wrong-answer-overlay");
  if (colorStr === "green") {
    overlay = $("#right-answer-overlay");
  }
  // hide then show overlay
  overlay.css({"display": "block"});
  setTimeout(function(){
    overlay.css({"display": "none"});
    if (callback) callback();
  }, flashTime);
};

// makes the overlay flash red really quickly
var flashRed = function(callback) {
  flashColor("red", callback);
};

// makes the overlay flash green really quickly
var flashGreen = function(callback) {
  flashColor("green", callback);
};

