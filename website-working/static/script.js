var vid = document.getElementById("myVideo");
	// window.onload=vid.play();

	var t0 = 20;
	var t1 = 40;
	

	var canswers = [4,2]
	var answers = []

	vid.addEventListener("timeupdate", function(){
	    if(this.currentTime >=t0 && this.currentTime <= (t0+0.2)) {
	        this.pause();
	        window.location.href='#confirm-modal0';
	        // vid.removeEventListener("timeupdate", function(){});
	        // return false;
	    }

	    if(this.currentTime >=t1 && this.currentTime <= (t1+0.2)) {
	        this.pause();
	        window.location.href='#confirm-modal1';
	        // vid.removeEventListener("timeupdate", function(){});
	    }


	});

	function funcc() {
		if (document.getElementById('a4').checked) {
			answers[0] = 1;
		}
		else {
			answers[0] = 0;
		}
		document.getElementById("confirm-modal0").style.display = "none";
		vid.currentTime=(t0+0.3);
		vid.play()
	}


	function funcc1() {
		if (document.getElementById('b2').checked) {
			answers[1] = 1;
		}
		else {
			answers[1] = 0;
		}
		document.getElementById("confirm-modal1").style.display = "none";
		vid.currentTime=(t1+0.3);
		vid.play()
	}
