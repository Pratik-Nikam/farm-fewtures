function setup(){
    // to send a request in vanilla js, we use fetch
    fetch("/setup", {
        method: "POST",
    }).then((_res) => { 
        window.location.href = "/";
     });
}