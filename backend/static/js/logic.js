function sendImage() {
    if (localStorage.image) {
            $.ajax({
                    // Your server script to process the upload
        url: 'image',
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
renderStyle(getStyle());
function renderStyle(style) {
  url_path = 'static/style/';
  format_img = url_path +  style + '.jpg';
  document.getElementById('style').innerHTML = 
    '<img src="'+format_img+'"/>';
}
  $('#styleDropdown').on('change', function(e) {
    renderStyle(e.target.options[e.target.selectedIndex].text)
  });
