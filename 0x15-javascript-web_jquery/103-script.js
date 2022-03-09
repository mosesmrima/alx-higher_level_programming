$("document").ready(function() {
function hello() {
    	const lang = $("INPUT#language_code").val();
	const url = `https://fourtonfish.com/hellosalut/?lang=${lang}`;
	$.get(url, function(data) {
	    $("DIV#hello").text(data.hello);
	});
}

    $("INPUT#btn_translate").click(hello);
    $("INPUT#btn_code").focus( function() {
	console.log("hey you");
	$(this).keydown(function(e) {
	    if (e.keyCode === 13) {
		hello();
	    }
	});
    });
});
