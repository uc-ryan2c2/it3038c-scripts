var dns = require('dns');

function hostnamelookup(hostname){
    dns.lookup(hostname, function(err, addresses, family) {  //this is a call back function
        console.log(addresses)
    });
}

if (process.argv.length < 3) {
    console.log("usage: " + __filename + " hostname.com")
    process.exit(-1)
}

var hostname = process.argv[2]
console.log(`checking IP of: ${hostname}`)
hostnamelookup(hostname)

