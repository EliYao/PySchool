$(function(){
	var $signIn = $(".SignIn");
	var $signUp = $(".SignUp");
	$signUp.remove();
	var $toggleBtn = $(".floatR a");
	$toggleBtn.click(function(){
		if($signUp.is(":visible")){
			$signUp.replace($signIn);
		} else{
			$signIn.replace($signUp);
		}
		return false;
	})	
});