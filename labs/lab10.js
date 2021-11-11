var express = require('express')
var app = express()
var config = require('config')
const fs = require('fs')

app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))


//This will display the contents of the json file
app.get('/api', function(request, response){
  const jsonString = fs.readFileSync("./widgets.json");
  const data = JSON.parse(jsonString);
  response.send(data);

});
app.get('/', function(request, response) {
  if (config.util.getEnv("NODE_ENV")=== "Testing"){

    response.send('<b>You are working in the <em>TEST</em> environment.')

  }

  else if (config.util.getEnv("NODE_ENV") === "Heroku Test") { 

        response.send('Hello! My name is Connor Ryan <br> You are working in the <em>TEST</em> environment that is in Heroku.<br> <a href="/api">Click here for API</a>') 
    
      } 
    
      else if (config.util.getEnv("NODE_ENV") === "Production") { 
    
        response.send('<b>You are working in Production</b>') 
    
      } 
    
      else { 
    
        response.send('<b>Environment is unknown</b>') 
    
      }
  //response.send('<b>Hello World! My name is = <em>' + process.env.MYNAME + '</em> <br /> My Node environment is : ' + config.util.getEnv('NODE_ENV'))
})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
