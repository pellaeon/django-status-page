$('document').ready(function() {
	$('#status > .ui.segment').click(function(e) {
		$(this).next('.transition').toggleClass('hidden');
		$(this).next('.transition').toggleClass('visible');
	});
});
