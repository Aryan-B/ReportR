'use strict';

import './popup.css';

(function() {
  // We will make use of Storage API to get and store `count` value
  // More information on Storage API can we found at
  // https://developer.chrome.com/extensions/storage

  // To get storage access, we have to mention it in `permissions` property of manifest.json file
  // More information on Permissions can we found at
  // https://developer.chrome.com/extensions/declare_permissions
  function myFunction() {
    var form = document.getElementById("useCasePostForm")
    var originalContent = form.innerHTML
    form.innerHTML = "<h1 class='title' style='color:#649000;'>Report was sent!!</h1>"
    setTimeout(function() {
      form.innerHTML = originalContent
    }, 2000)
  }
  
  var xj = new XMLHttpRequest();

  document.addEventListener('DOMContentLoaded', function () {
    console.log("the doc loaded")
    var form = document.getElementById("useCasePostForm")
    form.addEventListener('submit',function(e){
        e.preventDefault()
        var link = document.getElementById("link").value;
        var reason = document.getElementById("reason").value;

        xj.open("POST", "https://073c-128-189-189-133.ngrok.io/report", true);
        xj.setRequestHeader("Content-Type", "application/json");
        xj.send(JSON.stringify({ 'link': link, 'reason': reason  }));
        xj.onreadystatechange = function () { if (xj.readyState == 4) { console.log(xj.responseText); } }
        form.reset()
        myFunction()
    })
});
})();
