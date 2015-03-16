var library;

$(function(){
  $.get('http://cubecam.l3dcube.com/static/js/l3d-library.js', function(data) {
	  library=data;
      }, 'text');

  //gets default code from the fireworks.js file
  $.get('http://cubecam.l3dcube.com/static/js/fireworks.js', function(data) {
	  $("#code").val(data);
	  formatCode();  //applies codeMirror formatting to the code
	  runSketch();
      }, 'text');	  

  function formatCode()
  {
	  var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
		  lineNumbers: true,
		  styleActiveLine: true,
		  matchBrackets: true
	      });
      editor.setOption("theme", "tomorrow-night-eighties");

  }


    });

