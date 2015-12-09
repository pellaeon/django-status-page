$('document').ready(function() {
	$('#status > .ui.segment').click(function(e) {
		$(this).nextUntil('.nonsecondary', '.transition').toggleClass('hidden');
		$(this).nextUntil('.nonsecondary', '.transition').toggleClass('visible');
	});
});
