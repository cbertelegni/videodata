// window.onload =  startApp;

progress_bar_loading = 0;
	function startApp(video){
		// video = new VideoActions("video");
		var play_pause = $("#play_pause"),
			add_point = $("#add_point"),
			content_bar = $("#content_bar"),
			progress_bar = $("#progress-bar"),
			mark_tmpl = $("#mark_tmpl").html(),
			tmpl_row_tag = $("#tmpl_row_tag").html(),
			popup = $(".cont_popup");

		play_pause.on("click", function(e){
			e.preventDefault();
			play_or_pause(video, play_pause, progress_bar);
			
		});

		add_point.on('click', function(e) {
			e.preventDefault();
			video.pause();
			if (progress_bar_loading) {
				window.clearInterval(progress_bar_loading);
			};

			play_pause.html('<span class="glyphicon glyphicon-play">');
			$("input[name='start_time']").val(video.currentTime());
			$("input[name='end_time']").val(video.currentTime() + 4);
			// play_or_pause(video, play_pause, progress_bar);
			popup.fadeIn();
		});


		 // confirm_marck *****
		 $("#confirm_marck").on('click', function(e) {
		 	e.preventDefault();
		 	var data ={};
		 	var form = $("#form").serialize().split("&");
			form.forEach(function(x){ 
				var d = x.split("=");
				data[d[0]]=d[1];
			});
			// console.log(data)
			// data.timestart = video.v.currentTime;
			add_mark(mark_tmpl, video, content_bar, data, popup, tmpl_row_tag);
		 	
		 });
		
	
		// popup****
		 $(".cont_popup .cancelar").on("click", function(e){
		 	e.preventDefault();
		 	popup.fadeOut('fast');
		 	document.forms.form.reset()
		 });

	}


	function play_or_pause(video, btn, progress_bar, up_to){
		if(!video.paused()){
			video.pause();
			btn.html('<span class="glyphicon glyphicon-play">');
			window.clearInterval(progress_bar_loading);
		}else{
			video.play();
			btn.html('<span class="glyphicon glyphicon-pause">');
			progress_bar_loading = setInterval(update_bar, 1000)
		}

		function update_bar(up_to){
			up_to ? up_to = up_to : up_to = get_porcent_progres(video);
			if(up_to <= 100)
				progress_bar.css("width", up_to + "%");
			console.log("update_bar: " + up_to);
		}
	}

	function add_mark(tmpl, v, cont_bar, data, popup, tmpl_row_tag){
		// v.pause();
		// console.log(data)
		var mark = $(tmpl);
		
		mark.data(data)
			.css({left: get_porcent_progres(video)+"%"});
		// addd clas for track this data

		cont_bar.append(mark);
		row = tmpl_row_tag
				.replace("{$quien$}", data.name)
				.replace("{$que$}", data.short_desc)
				.replace("{$descripcion$}", data.description);

		// console.log(v.currentTime());

		// console.log(location.href +v.currentTime())
		var tag_id = null;
		$.post(location.href + "crear_tag/" , data, function(data_response, textStatus, xhr) {
			console.log(data_response)
			var _tag_id = "tag_id" + v.currentTime();
			mark.addClass(_tag_id);
			
			$("#list_tags").append($(row).addClass(_tag_id).data("tag_id", _tag_id));
			// $(tmpl_row_tag);


		});


		popup.fadeOut();
		document.forms.form.reset()
	}


	function get_porcent_progres(video){
		return video.currentTime() * 100 / video.duration();
	};

	// function VideoActions(video_id){
	// 		this.v = document.getElementById(video_id);
	// 	};

	// 	VideoActions.prototype.pause = function(){
	// 			this.v.pause();
	// 		}

	// 	VideoActions.prototype.play = function(){
	// 			this.v.play();
	// 		}

	// 	VideoActions.prototype.is_play = function(){
	// 			// return true if video is play;
	// 			return !this.v.paused && !this.ended;
	// 		}
		
	// 	VideoActions.prototype.get_porcent_progres = function(){
	// 			// return the porcent progress of video
	// 			return this.v.currentTime * 100 / this.v.duration;
	// 		}


		/*
		VideoActions.prototype.get_time = function(){
				return this.v.currentTime;
			}

		VideoActions.prototype.get_duration = function(){
				return this.v.duration;
			}
		*/

		// VideoActions.prototype.on_ended = function(v, callback){
		// 	// se dispara con el final del video
		// 		return v.ended;
			
		// 	}
