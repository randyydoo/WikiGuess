var score = 0;
var g_json

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
function start() {
  return fetch('/get_text')
    .then(response => {
    console.log(response);
      return response.json();
    })
    .then(data => {
      console.log(data);
      return data;
    })
    .catch(error => {
      console.error(error);
    });
}

// Function to set text for left and right buttons
function newText(data) {
  var num = g_json["Random"];
  var wiki_text = g_json['Wiki'];
  var gpt_text = g_json['Gpt'];
  
  let left = document.getElementById('left_button');
  let right = document.getElementById('right_button');

  document.getElementById('score').innerHTML = "Score: " + score

  left.style.display = "block";
  right.style.display = "block";
  
  if (num == 1) {
    left.innerHTML = wiki_text;
    left.value = 'wiki';
    

    right.innerHTML = gpt_text;
    right.value = 'gpt';
  } 
  else {
    right.innerHTML = wiki_text;
    right.value = 'wiki';
  
    left.innerHTML = gpt_text;
    left.value = 'gpt';
  }
}


document.getElementById("start").addEventListener("click", function() {
  start().then(data => {
    g_json = data;
    newText(data);
}).catch(error => {
  console.error(error);
});
});

document.getElementById('left_button').addEventListener('click', function(event) {
  if (event.target.value == "gpt") {
    score++;
    start().then(data => {
      g_json = data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  } else {
    score = 0;
    alert("Incorrect");
    start().then(data => {
      g_json = data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  }
});

document.getElementById('right_button').addEventListener('click', function(event) {
  if (event.target.value == "gpt") {
    score++;
    start().then(data => {
      g_json =data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  } else {
    alert("Incorrect")
    score = 0;
    start().then(data => {
      g_json = data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  }
});







