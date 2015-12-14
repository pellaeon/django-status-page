$('document').ready(function() {
	$('#status > .ui.segment.nonsecondary').click(function(e) {
		$(this).nextUntil('.nonsecondary', '.transition').toggleClass('hidden');
		$(this).nextUntil('.nonsecondary', '.transition').toggleClass('visible');
	});
});
