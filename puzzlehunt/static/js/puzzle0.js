// puzzle 0 code

var showDiv = function(elem) {elem.addClass("show").removeClass("hidden")}
var hideDiv = function(elem) {elem.addClass("hidden").removeClass("show")}

var flashRed = function() {
	
};

$("#submit-1").click(function(event) {
	var answerInput = $("#answerInput-1").val();
	if (true) {
		hideDiv($("#question-1"));
		showDiv($("#continue-1"));
	};
});

$("#continue-btn-1").click(function(event) {
	hideDiv($("#continue-1"));
	showDiv($("#question-2"));
	$("#part-title").html("Part 2");
});

$("#submit-2").click(function(event) {
	var answerInput = $("#answerInput-2").val();
	if (answerInput === "") {
		hideDiv($("#question-1"));
		showDiv($("#continue-1"));
	};
});



$("#continue-btn-2").click(function(event) {
	hideDiv($("#continue-2"));
	showDiv($("#question-3"));
	$("#part-title").html("Part 3");
});




$("#continue-btn-3").click(function(event) {
	$("#part-title").html("YOU'RE DONE!!!");
});
