function set_content_album_links_height() {
	var obj = $(".content_album_links"); 
	obj.css("margin-top",
			350 - (18 * $(".content_album_links li").length - 1));
	obj.css("display", "block");
}

function photo_selection(src) {
	$(".content_picture img").attr('src', src);
}