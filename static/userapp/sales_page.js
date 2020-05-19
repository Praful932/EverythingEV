$(document).ready(function() {
	$(".menu").on("click", function() {
		$(".main_option").toggleClass("show");
		$("#menu").fadeOut(function() {
			$("#menu").text($("#menu").text() == "More" ? "Less" : "More").fadeIn();
			$("#menu_icon").text($("#menu_icon").text() == "menu" ? "close" : "menu").fadeIn();
		});
	});
});