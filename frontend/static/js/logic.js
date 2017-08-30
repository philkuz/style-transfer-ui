function sendImage() {
    if (localStorage.image) {
			$.ajax({
					// Your server script to process the upload
        url: 'http://localhost:5001/image',
					type: 'POST',

					// Form data
					data: {
						imgBase64: localStorage.getItem('image'),
            style: getStyle(),
					},
          success: function(data) {
            renderImage(data);
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

function renderImage(data_uri) {
    format_data = "data:image/jpeg;base64," + data_uri;
				document.getElementById('style-transfer').innerHTML = 
					'<img src="'+format_data+'"/>';
}
function getStyle() {
  style =$('#styleDropdown').find(":selected").text();
  console.log(style);
  return  style;
}

  // $('#styleDropdown').live('change', function(e) {
  //   // TODO change the style image displayed
  //   // e.target.options[e.target.selectedIndex].text
  // });
