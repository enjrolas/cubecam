var compiled=false;
var accessToken, username, nickname, coreID;  //global vars holding the user's accesstoken and email

$(function(){
	login("alex@lookingglassfactory.com", "lookatthatglass");
    });

function compile(){
    $.post("/compile/", 
	   {"code":$("#code").val()},
	   function(data){
	       console.log(data);
	       var callback = function(err, data) {
		   if (err) {
		       console.log('An error occurred while compiling the code:', err);
		   } else {
		       console.log('Code compilation started successfully:', data);
		   }
	       };
	       spark.compileCode(["/media/tempfile"], callback);

	   });

}

function flash(){
    spark.flashCore('CORE_ID',
		    ['./path/to/your/file1', './path/to/your/file2'],
		    function(err, data) {
			if (err) {
			    console.log('An error occurred while flashing the core:', err);
			} else {
			    console.log('Core flashing started successfully:', data);
			}
		    });
}

//login attempts to log into spark's server with the email/password combination
//retrieves the account's access token, and sets site-wide cookies with the user's
//email and access token.
function login( email, password)
{
    var loginPromise = window.spark.login({ username: email, password: password });
    loginPromise.then(function(data){
	handleLoginResponse(data);
		     },
		      function(error){
			  handleLoginError(error);
		      });
}

function handleLoginResponse(data){

	  accessToken=data.access_token;
	  console.log(accessToken);
}

function handleLoginError(error) {
        if (error.message === 'invalid_client') {
          displayLoginError('Invalid username or password.');
        } else if (error.cors === 'rejected') {
          displayLoginError('Request rejected.');
        } else {
          displayLoginError('Unknown error.');
          console.log(error);
        }
}