var images = {};
var next_image = undefined;
var intervalID = undefined;

$(document).ready(
		function() {
			set_container_album_links_height();
			load_images();
			$(".container_thumbnail img").click(
					function() {
						var ii = $(this);
						if ($(".container_picture img").attr("alt") == ii.attr("alt").substring(0, ii.attr("alt").indexOf("-"))) {
							return;
						}
						next_image = this;
						load_image();
						clearInterval(intervalID);
					});
			$(".container_picture > img").click(load_next_image);
			$(".container_picture").click(clearInterval(intervalID));
			$(window).focus(function() {
				intervalID = setInterval("start_sliding()", 10000);
			});
			$(window).blur(function() {
			    clearInterval(intervalID);
			});
			intervalID = setInterval("start_sliding()", 10000);
		});

function start_sliding() {
	$(".container_picture > img").click();
//	setInterval("start_sliding()", 7000);
}

function load_next_image() {
	var next_position = $("img[alt^='" + $(this).children("img").attr("alt") + "-']").parent().index();
	if (next_position < 10) {
		next_image = $(".container_thumbnail").eq(next_position).children("img");
	} else {
		next_image = $(".container_thumbnail").eq(0).children("img");
	}
	load_image();
}

function load_images() {
	var tns = $(".container_thumbnail");
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
	var div = $(".container_picture");
	div.fadeOut(200, function() {
		$(".container_picture img").replaceWith(images[$(next_image).attr("alt").split("-")[0]]);
		$(this).fadeIn(200);
	});

}

function set_container_album_links_height() {
	var obj = $(".container_album_links");
	obj.css("margin-top", 350 - (18 * $(".container_album_links li").length - 1));
	obj.css("display", "block");
}