var images = {};
var next_image = undefined;

$(document).ready(
		function() {
			set_content_album_links_height();
			load_images();
			$(".content_thumbnail img").click(
					function() {
						var ii = $(this);
						if ($(".content_picture img").attr("alt") == ii.attr("alt").substring(0, ii.attr("alt").indexOf("-"))) {
							return;
						}
						next_image = this;
						load_image();
					});
			$(".content_picture").click(load_next_image);
			setTimeout("start_sliding()", 7000);
		});

function start_sliding() {
	$(".content_picture").click();
	setTimeout("start_sliding()", 7000);
}

function load_next_image() {
	var next_position = $("img[alt^='" + $(this).children("img").attr("alt") + "-']").parent().index();
	if (next_position < 10) {
		next_image = $(".content_thumbnail").eq(next_position).children("img");
	} else {
		next_image = $(".content_thumbnail").eq(0).children("img");
	}
	load_image();
	// $(".content_thumbnail").eq($("img[alt^='5600398738051520754-']").parent().index()+1)
	// $("img[alt|=" + $(this).attr("alt") + "]");
}

function load_images() {
	var tns = $(".content_thumbnail");
	for (tn in tns) {
		var alt = tns.eq(tn).find("img").attr("alt");
		if (alt) {
			var v = alt.substring(0, alt.indexOf("-"));
			var vv = alt.substring(alt.indexOf("-") + 1);
			image = new Image(522, 392);
			image.alt = v;
			image.src = vv;
			images[v] = image;
		}
	}
}

function load_image() {
	var div = $(".content_picture");
	div.fadeOut(200, function() {
		$(".content_picture img").replaceWith(images[$(next_image).attr("alt").split("-")[0]]);
		$(this).fadeIn(200);
	});

}

function set_content_album_links_height() {
	var obj = $(".content_album_links");
	obj.css("margin-top", 350 - (18 * $(".content_album_links li").length - 1));
	obj.css("display", "block");
}