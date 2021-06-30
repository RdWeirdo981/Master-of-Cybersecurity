console.log('Loading Lambda HTML');

exports.handler = function(event, context) {

    var fs = require('fs'); 
    // read html file
    fs.readFile('index.html', 'utf8', function(err, data){
        context.succeed(data);
    });
    
};
