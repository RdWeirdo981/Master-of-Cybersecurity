console.log('Loading Lambda HTML');

exports.handler = function(event, context) {
    


    var html = '<html>\
                <style>\
                p {text-align: center;}\
                </style>\
                \
                <script>\
            	    var authen_part = window.location.hash;\
                    var access_token = authen_part.split("access_token=")[1];\
                    if (!access_token) {\
                        alert("Unauthorized!");\
            	        window.location.replace("https://image3detection2for1assignment.auth.us-east-1.amazoncognito.com/signup?client_id=3rntv25lge865d1njcqsutssem&response_type=token&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://yv3pcqir0a.execute-api.us-east-1.amazonaws.com/ImageDetection/mainpage");\
                    }\
            	</script>\
                \
                <body style="background-color:coral;">\
                <h1 style="font-size:20px"><center> Successfully Logged out ! </center></h1>\
                <p style="font-size:20px">Do you want to login again? <a \
                href="https://image3detection2for1assignment.auth.us-east-1.amazoncognito.com/login?client_id=3rntv25lge865d1njcqsutssem&response_type=token&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://yv3pcqir0a.execute-api.us-east-1.amazonaws.com/ImageDetection/mainpage"\
                >Login</a></p>\
                </body>\
                </html>';
    context.succeed(html);
};
