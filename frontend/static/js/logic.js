function sendImage() {
    if (localStorage.image) {
			console.log('sending');
			$.ajax({
					// Your server script to process the upload
					url: 'send_back',
					type: 'POST',

					// Form data
					data: {
						imgBase64: localStorage.getItem('image'),
					},

					// Tell jQuery not to process data or worry about content-type
					// You *must* include these options!
					// cache: false,
					// contentType: false,
					// processData: false,

		});
	} else{
		console.log('not sending');
	}
}
