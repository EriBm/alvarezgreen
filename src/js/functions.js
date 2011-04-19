function set_content_album_links_height() {
	$(".content_album_links").css("margin-top",
			350 - (18 * $(".content_album_links li").length - 1));
}