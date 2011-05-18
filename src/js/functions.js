var images = {};

$(document).ready(function() {
	set_content_album_links_height();
	load_images();
});

function load_images() {
	var tns = $(".content_thumbnail");
	for (tn in tns) {
		var alt = tns.eq(tn).find("img").attr("alt");
		if (alt) {
			var v = alt.split("-");
			image = new Image(522, 392);
			image.src = v[1];
			images[v[0]] = image;
		}
	}
}

function load_image(img) {
	var current_image = $(".content_picture img");
	var div = $(".content_picture");
	div.fadeOut();
	current_image.replaceWith(images[$(img).attr("alt").split("-")[0]]);
	div.fadeIn();
}

function set_content_album_links_height() {
	var obj = $(".content_album_links");
	obj.css("margin-top", 350 - (18 * $(".content_album_links li").length - 1));
	obj.css("display", "block");
}