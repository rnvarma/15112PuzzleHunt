// puzzle 0 code

var showDiv = function(elem) {elem.addClass("show").removeClass("hidden")}
var hideDiv = function(elem) {elem.addClass("hidden").removeClass("show")}

// PART 1

$("#submit-1").click(function(event) {
	var answerInput = $("#answerInput-1").val();
	if (true) {
		flashRed(function(){
			hideDiv($("#question-1"));
			showDiv($("#continue-1"));
		});
	};
});

$("#hint-1").click(function(event) {
	createAlert("If anything wrong is right, then type anything, "+
		"without fear of being wrong, and you'll be right.");
});

$("#continue-btn-1").click(function(event) {
	hideDiv($("#continue-1"));
	showDiv($("#question-2"));
	$("#part-title").html("Part 2");
});

// PART 2

$("#submit-2").click(function(event) {
	var answerInput = $("#answerInput-2").val();
	if (answerInput.indexOf("used the hint") !== -1) {
		flashGreen(function(){
			hideDiv($("#question-2"));
			showDiv($("#continue-2"));
		});
	}
	else {
		flashRed();
	}
});

$("#hint-2").click(function(event) {
	createAlert("Enter \"I used the hint\".");
});

$("#continue-btn-2").click(function(event) {
	hideDiv($("#continue-2"));
	showDiv($("#question-3"));
	$("#part-title").html("Part 3");
});

// PART 3

$("#submit-3").click(function(event) {
	var answerInput = $("#answerInput-3").val();
	if (answerInput === "42") {
		flashGreen(function(){
			hideDiv($("#question-3"));
			showDiv($("#continue-3"));
		});
	}
	else {
		flashRed();
	}
});

$("#hint-3").click(function(event) {
	createAlert("Try googling if you are unsure and something seems"+
		" to have a reference to something else.<br>By the way - this"+
		" answer is also known as \"the answer to life the universe"+
		" and everything\"!");
});

$("#continue-btn-3").click(function(event) {
	$("#part-title").html("ACTIVATE NEXT QUESTION!");
});



