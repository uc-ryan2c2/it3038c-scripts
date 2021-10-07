process.stdout.write("hello, what is your name? ")

process.stdin.on('data', function(data){ //this is a call back function.  This acts like an imput from the user
    console.log("hello " + data.toString())
    process.exit()

})

process.on('exit', function(){
    console.log("thanks for the info!")
})


