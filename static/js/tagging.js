window.onload =  startApp;

	function startApp(){
		video = new VideoActions("video");
		var play_pause = $("#play_pause"),
			add_point = $("#add_point"),
			content_bar = $("#content_bar"),
			progress_bar = $("#progress-bar"),
			mark_tmpl = $("#mark_tmpl").html(),
			popup = $(".cont_popup");
		play_pause.on("click", function(e){
			e.preventDefault();
			play_or_pause(video, play_pause, progress_bar);
			
		});

		add_point.on('click', function(e) {
			e.preventDefault();
			video.pause();
			$("input[name='timestart']").val(video.v.currentTime);
			// play_or_pause(video, play_pause, progress_bar);
			popup.fadeIn();
		});

		
	
		// popup****
		 $(".cont_popup .close").on("click", function(e){
		 	e.preventDefault();
		 	popup.fadeOut('fast');
		 	document.forms.form.reset()
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
			add_mark(mark_tmpl, video, content_bar, data, popup);
		 	
		 });
	}


	function play_or_pause(video, btn, progress_bar, up_to){
		if(video.is_play()){
			video.pause();
			btn.html("Play");
			window.clearInterval(progress_bar_loading);
		}else{
			video.play();
			btn.html("Pause");
			progress_bar_loading = setInterval(update_bar, 1000)
		}

		function update_bar(up_to){
			up_to ? up_to = up_to : up_to = video.get_porcent_progres();
			if(up_to <= 100)
				progress_bar.css("width", up_to + "%");
			console.log("update_bar: " + up_to);
		}
	}

	function add_mark(tmpl, v, cont_bar, data, popup){
		// v.pause();
		// console.log(data)
		var mark = $(tmpl);
		mark.data(data)
			.css({left: v.get_porcent_progres()+"%"});
		cont_bar.append(mark);
		popup.fadeOut();
		document.forms.form.reset()
	}


	function add_tooltip_for_mark(mark){
		console.log(mark.data())
	}


	function VideoActions(video_id){
			this.v = document.getElementById(video_id);
		};

		VideoActions.prototype.pause = function(){
				this.v.pause();
			}

		VideoActions.prototype.play = function(){
				this.v.play();
			}

		VideoActions.prototype.is_play = function(){
				// return true if video is play;
				return !this.v.paused && !this.ended;
			}
		
		VideoActions.prototype.get_porcent_progres = function(){
				// return the porcent progress of video
				return this.v.currentTime * 100 / this.v.duration;
			}


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
