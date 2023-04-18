var score = 0;

document.getElementById("start").addEventListener("click", function() {
  fetch("/get_text")
    .then(response => response.json())
    .then(data => {
      newText(data);
    })
    .catch(error => console.error(error));
});

document.getElementById('left_button').addEventListener('click', function() {
  var value = document.getElementById('left_button').value;
  if (value === 'gpt') {
    score++;
  } else {
    score = 0;
  }
  document.getElementById('score').innerHTML = 'Score: ' + score;
});

document.getElementById('right_button').addEventListener('click', function() {
  var value = document.getElementById('right_button').value;
  if (value === 'gpt') {
    score++;
  } else {
    score = 0;
  }
  document.getElementById('score').innerHTML = 'Score: ' + score;
});

// Function to set text for left and right buttons
function newText(data) {
  var wiki_text = data['Wiki'];
  var gpt_text = data['Gpt'];
  var sport = data['Sport'];
  var random = data["Random"]
  
  let left = document.getElementById('left_button');
  let right = document.getElementById('right_button');
  let left_sport = document.getElementById('left_sport');
  let right_sport = document.getElementById('right_sport');
  let score = document.getElementById('score');

  left.style.display = "block";
  right.style.display = "block";
  score.innerHTML = 'Score: ' + score;
  
  if (random == 1) {
    left.innerHTML = wiki_text;
    left.value = 'wiki';
    left_sport.innerHTML = sport;

    right.innerHTML = gpt_text;
    right.value = 'gpt';
    right.innerHTML = sport;
  } else {
    right.innerHTML = wiki_text;
    right.value = 'wiki';
    right_sport.innerHTML = sport;

    left.innerHTML = gpt_text;
    left.value = 'gpt';
    left.innerHTML = sport;
  }
}







