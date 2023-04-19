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
  var random = getRandomInt(0,2);
  var wiki_text = data['Wiki'];
  var gpt_text = data['Gpt'];
  var sport = data['Sport'];
  
  let left = document.getElementById('left_button');
  let right = document.getElementById('right_button');
  let left_sport = document.getElementById('left_sport');
  let right_sport = document.getElementById('right_sport');

  left.style.display = "block";
  right.style.display = "block";
  
  if (random == 1) {
    left.innerHTML = wiki_text;
    left.value = 'wiki';
    left_sport.innerHTML = sport;

    right.innerHTML = gpt_text;
    right.value = 'gpt';
    right_sport.innerHTML = sport;
  } 
  else {
    right.innerHTML = wiki_text;
    right.value = 'wiki';
    right_sport.innerHTML = sport;
  
    left.innerHTML = gpt_text;
    left.value = 'gpt';
    left_sport.innerHTML = sport;
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

document.getElementById('left_button').addEventListener('click', function() {
  var value = document.getElementById('left_button').value;
  if (value === 'gpt') {
    score++;
    start().then(data => {
      g_json = data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  } else {
    score = 0;
    start().then(data => {
      g_json = data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  }
  document.getElementById('score').innerHTML = 'Score: ' + score;
});

document.getElementById('right_button').addEventListener('click', function() {
  var value = document.getElementById('right_button').value;
  if (value === 'gpt') {
    score++;
    start().then(data => {
      g_json =data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  } else {
    score = 0;
    start().then(data => {
      g_json = data;
      newText(data);
  }).catch(error => {
    console.error(error);
  });
  }
  document.getElementById('score').innerHTML = 'Score: ' + score;
});







